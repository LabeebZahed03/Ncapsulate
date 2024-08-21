from flask import Flask, request, render_template, redirect, url_for, jsonify
import os
import whisper
from transformers import pipeline
import ffmpeg
import subprocess

app = Flask(
            __name__, 
            template_folder=os.path.join(os.pardir, 'templates'),
            static_folder=os.path.join(os.pardir, 'static'))
app.config['TEMPLATES_AUTO_RELOAD'] = True

UPLOAD_FOLDER = os.path.join(os.pardir, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Logic for Summarizing pipeline
# Extracting audio from video function
def extract_audio(video_path, audio_output_path):
    command = f"ffmpeg -i {video_path} -q:a 0 -map a {audio_output_path}"
    subprocess.call(command, shell=True)

# Models
whisper_model = whisper.load_model("base")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Transcribe Audio using Whisper
def transcribe_audio_with_whisper(audio_path):
    result = whisper_model.transcribe(audio_path)
    transcription = result['text']
    return transcription

# Summarize Text with Prompt Engineering
def summarize_text(text, category="motivational"):
    prompt = ""
    if category == "motivational":
        prompt = f"Summarize the following motivational speech in a concise manner, highlighting the key points and themes discussed:\n\n{text}"
    elif category == "educational":
        prompt = f"Summarize the following educational content in a concise manner, focusing on the main lessons and key takeaways:\n\n{text}"
    else:
        prompt = f"Summarize the following text concisely:\n\n{text}"

    max_chunk_size = 1024  # Token limit for BART
    summaries = []
    for i in range(0, len(prompt), max_chunk_size):
        chunk = prompt[i:i+max_chunk_size]
        summary = summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
        summaries.append(summary)

    combined_summary = " ".join(summaries)

    # Further refine the summary by summarizing the combined result
    final_summary = summarizer(combined_summary, max_length=80, min_length=30, do_sample=False)[0]['summary_text']

    return final_summary

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

            # Extract audio if it's a video file
            audio_path = os.path.join(app.config['UPLOAD_FOLDER'], 'audio.wav')
            if filename.endswith('.mp4'):
                ffmpeg.input(file_path).output(audio_path).run(overwrite_output=True)
            else:
                audio_path = file_path  # Assume it's an audio file

            # Transcribe audio
            transcription = transcribe_audio_with_whisper(audio_path)
            
            # Summarize transcription with prompt engineering
            summary = summarize_text(transcription, category="motivational")  # You can change the category dynamically

            return jsonify({
                'message': 'File uploaded successfully', 
                'filename': filename,
                'transcription': transcription,
                'summary': summary
            })
    
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)
