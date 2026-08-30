from reviewer import review_resume


resume = """
Software Engineer with experience in Python, Java, SQL and FastAPI.
Built REST APIs and worked with backend systems.
Strong knowledge of data structures and algorithms.
"""

job_description = """
We are looking for a Software Engineer with experience in Python,
FastAPI, SQL and AWS. Knowledge of REST APIs and cloud technologies
is preferred.
"""

result = review_resume(resume, job_description)

print(result)