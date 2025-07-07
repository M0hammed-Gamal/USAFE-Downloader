import os
import sys
import types

# Provide dummy modules if real ones are missing
if 'requests' not in sys.modules:
    requests_stub = types.ModuleType('requests')
    def dummy_get(url, allow_redirects=True):
        raise RuntimeError('requests.get should be mocked')
    requests_stub.get = dummy_get
    sys.modules['requests'] = requests_stub

if 'yt_dlp' not in sys.modules:
    yt_dlp_stub = types.ModuleType('yt_dlp')
    class DummyDL:
        def __init__(self, *a, **k):
            pass
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass
        def download(self, *a, **k):
            pass
    yt_dlp_stub.YoutubeDL = DummyDL
    sys.modules['yt_dlp'] = yt_dlp_stub

import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import importlib
USAFE_downloader = importlib.import_module('USAFE_downloader')

def test_download_file(tmp_path, monkeypatch):
    called = {}
    def fake_get(url, allow_redirects=True):
        called['url'] = url
        called['allow_redirects'] = allow_redirects
        return types.SimpleNamespace(content=b'data')
    monkeypatch.setattr(USAFE_downloader.requests, 'get', fake_get)
    USAFE_downloader.download_file('http://e.com/file.pdf', str(tmp_path), 'out.pdf')
    assert called == {'url': 'http://e.com/file.pdf', 'allow_redirects': True}
    assert (tmp_path / 'out.pdf').read_bytes() == b'data'

def test_download_video(tmp_path, monkeypatch):
    events = {}
    class DummyDL:
        def __init__(self, opts):
            events['opts'] = opts
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass
        def download(self, urls):
            events['urls'] = urls
    monkeypatch.setattr(USAFE_downloader, 'yt_dlp', types.SimpleNamespace(YoutubeDL=DummyDL))
    USAFE_downloader.download_video('http://video', str(tmp_path), 'vid')
    assert events['opts']['outtmpl'] == os.path.join(str(tmp_path), 'vid.%(ext)s')
    assert events['urls'] == ['http://video']

def test_hook_prints(capsys):
    USAFE_downloader.hook({'status': 'downloading', '_percent_str': '10%', 'eta': 5})
    out = capsys.readouterr().out
    assert '10%' in out and 'ETA' in out

def test_main_pdf(tmp_path, monkeypatch):
    inputs = iter(['http://ex.com/file.pdf', str(tmp_path), 'name'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    called = {}
    def fake_download_file(url, output, filename):
        called['file'] = (url, output, filename)
    monkeypatch.setattr(USAFE_downloader, 'download_file', fake_download_file)
    monkeypatch.setattr(USAFE_downloader, 'download_video', lambda *a, **k: called.setdefault('video', True))
    USAFE_downloader.main()
    assert called['file'] == ('http://ex.com/file.pdf', str(tmp_path), 'name.pdf')
    assert 'video' not in called

def test_main_video(tmp_path, monkeypatch):
    inputs = iter(['http://ex.com/clip.mp4', str(tmp_path), 'clip'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    called = {}
    monkeypatch.setattr(USAFE_downloader, 'download_file', lambda *a, **k: called.setdefault('file', True))
    def fake_download_video(url, output, filename):
        called['video'] = (url, output, filename)
    monkeypatch.setattr(USAFE_downloader, 'download_video', fake_download_video)
    USAFE_downloader.main()
    assert called['video'] == ('http://ex.com/clip.mp4', str(tmp_path), 'clip')
    assert 'file' not in called
