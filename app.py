from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
from rembg import remove

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'hello'

@app.route('/remove_background', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'})
    
    image_file = request.files['image']
    
    if image_file.filename == '':
        return jsonify({'error': 'No selected image'})
    
    try:
        image_data = image_file.read()
        image_data = base64.b64encode(remove(image_data)).decode('utf-8')
        return jsonify({'result': image_data})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
