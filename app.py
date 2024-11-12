from flask import Flask, request, jsonify
from flask_cors import CORS
import tempfile
from file_processor import process_file
from search import search
import os

app = Flask(__name__)
CORS(app)

@app.route("/search")
def get_search_results():
    link = request.args.get('q')
    if not link:
        return "No link was provided", 400
    return search(link)

@app.route('/upload', methods = ['POST', 'OPTIONS'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    

    # Get the path to the temporary directory
    temp_dir = tempfile.gettempdir()
    full_path = os.path.join(temp_dir, file.filename)
    try:
        file.save(full_path)
        response = process_file(full_path)
    finally:
        os.remove(full_path)
    return response