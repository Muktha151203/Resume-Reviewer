from pdf_parser import extract_text_from_pdf
from similarity import calculate_similarity


resume_text = extract_text_from_pdf("resume.pdf")

job_description = """
We are looking for a software engineer with experience in
Python, Java, SQL, REST APIs, backend development,
Git and software engineering.
"""

score = calculate_similarity(resume_text, job_description)

print(f"Resume-Job Match Score: {score}%")