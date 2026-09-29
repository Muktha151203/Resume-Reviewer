import json
from groq_client import client


def review_resume(resume_text, job_description):

    prompt = f"""
You are reviewing a candidate's resume against a specific job description.

Resume:
{resume_text}

Job Description:
{job_description}

Analyze the candidate ONLY against the provided job description.

Classify important job requirements into three categories:

1. matching_skills:
   Requirements clearly demonstrated in the resume.

2. partial_skills:
   Requirements where the resume shows some related knowledge,
   exposure, or foundational experience, but does not clearly
   demonstrate the full requirement.

3. missing_skills:
   Requirements explicitly mentioned in the job description
   for which there is no supporting evidence anywhere in the resume.

IMPORTANT:
- Do not treat a partial skill as fully matching.
- Do not treat a partial skill as completely missing.
- Do not invent candidate experience.
- Do not invent job requirements.
- Use only evidence contained in the resume.
- If the resume says "fundamentals", "basic knowledge", "exposure",
  "learning", or similar wording, consider the skill PARTIAL unless
  the job requirement is also explicitly at a foundational level.
-- A skill appearing only in the resume's Technical Skills section
  should NOT automatically be classified as a strong match.
- Strong matching evidence should preferably come from professional
  experience, internships, projects, certifications, or clearly
  described hands-on work.
- If a skill is only listed without supporting evidence, classify it
  as PARTIAL rather than MATCHING.
- Projects can count as evidence of a skill, but clearly distinguish
  project experience from professional experience.
- Recommendations must address partial or missing requirements.
- Never recommend that the candidate falsely claim a skill.

Return ONLY valid JSON in exactly this format:

{{
    "overall_assessment": "brief assessment",
    "matching_skills": [],
    "partial_skills": [],
    "missing_skills": [],
    "relevant_experience": [],
    "areas_for_improvement": [],
    "recommendations": []
}}

For matching_skills, partial_skills, and missing_skills:
- Use concise skill or requirement names.
- - Every requirement must appear in exactly ONE category:
  matching_skills, partial_skills, OR missing_skills.
- Never place the same requirement in more than one category.
- If there is no concrete evidence for a requirement, classify it
  as MISSING, not PARTIAL.
- Use PARTIAL only when the resume contains some concrete evidence
  related to the requirement but does not fully satisfy it.

For relevant_experience:
- Mention only concrete experience from the resume that relates
  to the job description.

For areas_for_improvement:
- Mention skills or requirements that are partial or missing.
- Do not claim the candidate lacks something that is actually
  demonstrated in the resume.

For recommendations:
- Give practical actions that would strengthen the candidate's
  evidence for the relevant requirements.

Return JSON only. Do not include Markdown or explanations outside JSON.
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