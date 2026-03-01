from flask import Flask, send_from_directory, send_file
import os

app = Flask(__name__, static_folder='.', static_url_path='')

# Ana sayfa
@app.route('/')
def index():
    return send_file('index.html')

# JS / CSS / diğer dosyalar
@app.route('/<path:path>')
def static_proxy(path):
    file_path = os.path.join('.', path)
    if os.path.exists(file_path):
        return send_from_directory('.', path)
    return 'Not Found', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8501, debug=True)
