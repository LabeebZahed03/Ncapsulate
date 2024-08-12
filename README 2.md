
# Ncapsulate

Ncapsulate is a video and audio summarization tool that leverages state-of-the-art ASR (Automatic Speech Recognition) and summarization models. The application is structured into three main components: frontend, backend, and models. It also includes a virtual environment for managing dependencies.

## Project Structure

- **`frontend/`**: Contains the front-end files for the application. This includes HTML, CSS, and JavaScript files that handle user interactions and display the summarization results.
- **`backend/`**: Contains the Flask application that serves the front end, processes user uploads, handles audio extraction, runs the ASR and summarization models, and returns the results to the user.
- **`models/`**: Contains the saved ASR and summarization models, as well as scripts used for model training and experimentation.
- **`ncapsulateEnv/`**: The virtual environment that contains all the dependencies required for the project.
- **`.gitignore`**: Specifies files and directories that Git should ignore. This includes environment files, compiled binaries, and other unnecessary files.

## Features

- **Audio and Video Summarization**: Users can upload audio or video files, which are then processed to extract the key content in the form of a summary.
- **Automatic Speech Recognition (ASR)**: The application uses Wav2Vec2.0 (or another chosen model) to transcribe speech from audio.
- **Text Summarization**: Summarization is done using transformer-based models like BART, fine-tuned for summarizing transcriptions of audio and video content.

## Installation

### Prerequisites

- Python 3.8+
- Virtualenv
- FFmpeg (for audio extraction from video files)

### Setting Up the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/username/Ncapsulate.git
   cd Ncapsulate
   ```

2. **Set Up the Virtual Environment**:
   ```bash
   python3 -m venv ncapsulateEnv
   source ncapsulateEnv/bin/activate  # On Windows use `ncapsulateEnv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure FFmpeg is Installed**:
   - **MacOS**:
     ```bash
     brew install ffmpeg
     ```
   - **Ubuntu**:
     ```bash
     sudo apt-get install ffmpeg
     ```
   - **Windows**:
     - Download FFmpeg from the [official website](https://ffmpeg.org/download.html) and add it to your system's PATH.

### Running the Application

1. **Start the Flask Server**:
   ```bash
   python backend/app.py
   ```

2. **Access the Application**:
   - Open your browser and navigate to `http://localhost:5000`.

3. **Upload and Summarize**:
   - Upload an audio or video file to generate a summary using the application.

## Project Components

### 1. Frontend
- **HTML/CSS/JavaScript**: The frontend interface where users can upload files and view the summarization results.
- **Responsive Design**: Ensures that the application is accessible across different devices and screen sizes.

### 2. Backend
- **Flask**: A Python web framework that handles the server-side logic.
- **File Handling**: Uploads are processed, and audio is extracted from videos using FFmpeg.
- **ASR and Summarization Integration**: The backend runs the ASR model to convert speech to text and then summarizes the text using a transformer-based model.

### 3. Models
- **Wav2Vec2.0**: Used for converting audio to text.
- **BART**: A transformer-based model used for summarizing text.
- **Model Training**: Scripts and Jupyter notebooks used for training and fine-tuning the models are stored here.

### 4. Virtual Environment
- **ncapsulateEnv**: The virtual environment directory contains all the dependencies required for the project. This ensures that the project runs in a consistent environment across different machines.

### 5. .gitignore
- **Ignored Files**: The `.gitignore` file includes patterns to exclude unnecessary files such as compiled code, environment files, logs, and large binaries that shouldn’t be tracked in the repository.

## Future Work

- **Live Summarization**: Implement a live summarization feature that processes streaming audio/video in real time.
- **User Interface Improvements**: Enhance the frontend interface for better user experience.
- **Model Optimization**: Fine-tune the models further for better accuracy and performance.

## Contribution

If you would like to contribute to this project, please fork the repository and use a feature branch. Pull requests are welcome.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
