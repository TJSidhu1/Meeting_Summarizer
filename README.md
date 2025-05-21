# Meeting_Summarizer is a web application that processes uploaded meeting audio files, transcribes the audio, summarizes the transcript, and extracts action items and decisions automatically. It uses FastAPI for the backend, React for the frontend, and leverages NLP models for summarization and text processing.

Features
Upload meeting audio files (.mp3 or others)

Transcribe audio to text using OpenAI Whisper model

Summarize meeting transcript using Facebook BART summarization model

Extract action items and decisions from transcript using NLP

Display transcript, summary, action items, and decisions in an interactive UI

Tech Stack
Backend: FastAPI, Whisper (audio transcription), Huggingface Transformers (summarization), spaCy (NLP)

Frontend: React, Axios

Audio processing: librosa, numpy

Getting Started
Prerequisites
Python 3.8+

Node.js and npm/yarn

FFmpeg installed (required for Whisper audio processing)


Backend Setup
Create and activate a virtual environment:


python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate


Install Python dependencies:

pip install fastapi uvicorn transformers spacy whisper librosa numpy
python -m spacy download en_core_web_sm



Run the FastAPI backend server:

uvicorn main:app --reload
The backend will be running on http://localhost:8000.

Frontend Setup
Navigate to the frontend directory (where your React app resides):


cd frontend

Install dependencies:

npm install
Start the React development server:


npm start
The frontend will open in your browser at http://localhost:3000.

Usage
Open the frontend app in your browser.

Upload a meeting audio file using the upload form.

The audio file will be sent to the backend, transcribed, summarized, and processed.

The app will display the transcript summary, list of action items, and decisions extracted from the meeting.

File Structure Overview

/backend
  main.py             # FastAPI app handling audio upload and processing
  nlp_utils.py        # NLP processing: summarization, action and decision extraction
  audio_utils.py      # Audio transcription with Whisper and librosa

/frontend
  src/
    App.js            # Main React app component
    components/
      FileUpload.js   # File upload component
      SummaryCard.js  # Displays summary
      ActionItemList.js # Displays action items
      DecisionLogList.js # Displays decisions
    index.js          # React app entry point
