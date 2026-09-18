from fastapi import FastAPI
from pydantic import BaseModel

from pipeline import analyze_resume


app = FastAPI()


class ResumeRequest(BaseModel):
    resume_text: str
    job_description: str


@app.get("/")
def home():
    return {"message": "Resume Reviewer API is running"}


@app.post("/analyze")
def analyze(request: ResumeRequest):

    result = analyze_resume(
        request.resume_text,
        request.job_description
    )

    return result   