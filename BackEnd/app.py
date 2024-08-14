from flask import Flask, request, render_template, redirect, url_for, jsonify
import os

app = Flask(__name__, 
            template_folder=os.path.join(os.pardir, 'templates'),
            static_folder=os.path.join(os.pardir, 'static'))
app.config['TEMPLATES_AUTO_RELOAD'] = True

UPLOAD_FOLDER = os.path.join(os.pardir, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        if file:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Placeholder for processing logic
            # Add logic here to process the file and generate a summary
            
            return jsonify({'message': 'File uploaded successfully', 'filename': filename})
    
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)
