from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from pipeline import analyze_resume
from resume_parser import extract_text_from_pdf
import os


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Resume Reviewer API is running"}


@app.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    if resume.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    file_path = "temp_resume.pdf"

    try:
        with open(file_path, "wb") as buffer:
            buffer.write(await resume.read())

        resume_text = extract_text_from_pdf(file_path)

        if not resume_text.strip():
            raise HTTPException(
                status_code=400,
                detail="Could not extract text from the PDF."
            )

        result = analyze_resume(
            resume_text,
            job_description
        )

        return result

    finally:
        if os.path.exists(file_path):
            os.remove(file_path) 