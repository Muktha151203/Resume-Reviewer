from similarity import calculate_similarity


resume = """
Python Java SQL React Node.js MongoDB
REST APIs backend development software engineering
"""

job_description = """
We are looking for a software engineer with Python,
SQL, React, Node.js and backend development experience.
"""


score = calculate_similarity(resume, job_description)

print(f"Resume-Job Match Score: {score}%")