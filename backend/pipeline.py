from similarity import calculate_similarity
from reviewer import review_resume


def analyze_resume(resume_text, job_description):

    similarity_score = calculate_similarity(
        resume_text,
        job_description
    )

    ai_review = review_resume(
        resume_text,
        job_description
    )

    return {
        "match_score": similarity_score,
        "ai_review": ai_review
    }