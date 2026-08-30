import json
from groq_client import client


def review_resume(resume_text, job_description):

    prompt = f"""
You are reviewing a candidate's resume against a specific job description.

Resume:
{resume_text}

Job Description:
{job_description}

Analyze the resume ONLY against the provided job description.

Return ONLY valid JSON in exactly this format:

{{
    "overall_assessment": "brief assessment",
    "matching_skills": [],
    "missing_skills": [],
    "relevant_experience": [],
    "areas_for_improvement": [],
    "recommendations": []
}}

Rules:
- Use only information provided in the resume and job description.
- List matching skills explicitly present in both.
- List ONLY requirements explicitly mentioned in the job description
  that are missing from the resume.
- Do not invent candidate experience.
- Do not invent job requirements.
- Do not suggest that a candidate claim a skill they do not have.
- Recommendations should be actionable.
- Return JSON only. Do not include Markdown or explanations outside the JSON.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert technical recruiter. "
                    "Be accurate, objective, and strictly grounded "
                    "in the provided resume and job description."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response.choices[0].message.content

    return json.loads(result)