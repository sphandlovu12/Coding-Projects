# flask_app/routes.py

import os
from flask import request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from . import app

UPLOAD_FOLDER = 'uploads/games/'
ALLOWED_EXTENSIONS = {'py', 'zip'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200
    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/game/<path:filename>')
def serve_game(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)