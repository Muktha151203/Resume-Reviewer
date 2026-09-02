from pipeline import analyze_resume


resume = """
Software Engineer with experience in Python,
FastAPI, SQL and REST APIs.
Built backend systems and REST APIs.
"""

job_description = """
We are looking for a Software Engineer with
experience in Python, FastAPI, SQL and REST APIs.
Knowledge of AWS and cloud technologies is preferred.
"""


result = analyze_resume(resume, job_description)

print("\n===== RESUME REVIEW =====\n")

print("Match Score:", result["match_score"])

print("\nAI Review:")
print(result["ai_review"])