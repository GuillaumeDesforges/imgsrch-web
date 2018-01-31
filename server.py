from flask import Flask, render_template, request, jsonify
import os
from imgsrch import Engine
import mimetypes
import uuid

app = Flask(__name__, static_url_path='/static')

print("Loading engine")
engine = Engine("engine.xml")

# debug
app.config['CACHE_TYPE'] = 'null'

#config
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def upload():
    if 'imageFile' not in request.files:
        return 'No file part', 400
    f = request.files['imageFile']
    if f.filename == '':
        return 'No selected file', 400
    file_slug = str(uuid.uuid4())
    file_extension = f.filename.split('.')[-1]
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_slug+'.'+file_extension)
    try:
        f.save(file_path)
        print("Saved file to", file_path)
    except Exception as e:
        return 'Failed to save file', 400
    scores = engine.computeLikelihoods(file_path)
    scores = [{'path': key, 'score': value} for key, value in scores.items()]
    scores = list(sorted(scores, key=lambda x:x['score'], reverse=True))
    return jsonify({'scores': scores}), 200

