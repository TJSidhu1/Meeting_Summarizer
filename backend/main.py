from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from nlp_utils import process_transcript
from audio_utils import transcribe_audio

app = FastAPI()

# Enable CORS (for frontend-backend communication)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process-audio/")
async def process_audio(file: UploadFile = File(...)):
    audio_path = f"temp_{file.filename}"
    with open(audio_path, "wb") as f:
        f.write(await file.read())

    transcript = transcribe_audio(audio_path)
    summary, actions, decisions = process_transcript(transcript)
    print(f"Summary: {summary}")
    print(f"Actions: {actions} (type: {type(actions)})")
    print(f"Decisions: {decisions}")

    return {
        "transcript": transcript,
        "summary": summary,
        "actions": actions,
        "decisions": decisions
    }
