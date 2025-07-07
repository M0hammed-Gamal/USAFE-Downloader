import os
from flask import Flask, request, jsonify, render_template
from USAFE_downloader import download_file, download_video

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json(force=True)
    url = data.get('url')
    output_path = data.get('path') or os.getcwd()
    filename = data.get('filename') or 'output'

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    lower_url = url.lower()
    if lower_url.endswith('.pdf'):
        download_file(url, output_path, filename + '.pdf')
    elif lower_url.endswith(('.mp3', '.mp4', '.avi', '.mkv', '.flv', '.mov')):
        download_video(url, output_path, filename)
    else:
        download_video(url, output_path, filename)

    return jsonify({'message': 'Download triggered'})

if __name__ == '__main__':
    app.run(debug=True)
