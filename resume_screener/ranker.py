"""
ranker.py
---------
Ranks resumes against a job description using TF-IDF vectorization and
cosine similarity, blended with an explicit skills-overlap score.
"""

import re
from dataclasses import dataclass, field
from typing import List

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from resume_screener.skills import extract_skills, skill_overlap


@dataclass
class ResumeResult:
    filename: str
    candidate_name: str
    similarity_score: float      # TF-IDF cosine similarity, 0-100
    skill_match_percent: float   # matched required skills, 0-100
    final_score: float           # blended score, 0-100
    matched_skills: List[str] = field(default_factory=list)
    missing_skills: List[str] = field(default_factory=list)
    all_resume_skills: List[str] = field(default_factory=list)
    raw_text: str = ""


NAME_LINE_RE = re.compile(r"^[A-Z][a-zA-Z.'-]+(?: [A-Z][a-zA-Z.'-]+){0,3}$")


def guess_candidate_name(text: str, fallback: str) -> str:
    """
    Best-effort guess of the candidate's name: the first non-empty line
    that looks like 'First Last' (title-cased, no digits/emails). Falls
    back to the filename if nothing plausible is found.
    """
    for line in text.splitlines()[:10]:
        line = line.strip()
        if not line or "@" in line or any(ch.isdigit() for ch in line):
            continue
        if 2 <= len(line.split()) <= 4 and NAME_LINE_RE.match(line):
            return line
    return fallback


def rank_resumes(
    job_description: str,
    resumes: List[dict],
    required_skills: List[str] = None,
    skill_weight: float = 0.4,
) -> List[ResumeResult]:
    """
    Rank resumes against a job description.

    Args:
        job_description: raw JD text.
        resumes: list of {"filename": str, "text": str}.
        required_skills: explicit list of required skills to score against.
                          If None, skills are auto-extracted from the JD.
        skill_weight: weight (0-1) given to the skills-match score; the
                      remainder is given to TF-IDF cosine similarity.

    Returns:
        List of ResumeResult, sorted by final_score descending.
    """
    if not resumes:
        return []

    if required_skills is None:
        required_skills = extract_skills(job_description)

    corpus = [job_description] + [r["text"] for r in resumes]
    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000, ngram_range=(1, 2))
    tfidf_matrix = vectorizer.fit_transform(corpus)

    jd_vector = tfidf_matrix[0:1]
    resume_vectors = tfidf_matrix[1:]
    similarities = cosine_similarity(jd_vector, resume_vectors).flatten()

    results = []
    for resume, sim in zip(resumes, similarities):
        resume_skills = extract_skills(resume["text"])
        overlap = skill_overlap(resume_skills, required_skills)

        sim_score = round(float(sim) * 100, 1)
        skill_score = overlap["match_percent"]
        final = round(skill_weight * skill_score + (1 - skill_weight) * sim_score, 1)

        results.append(
            ResumeResult(
                filename=resume["filename"],
                candidate_name=guess_candidate_name(resume["text"], resume["filename"]),
                similarity_score=sim_score,
                skill_match_percent=skill_score,
                final_score=final,
                matched_skills=overlap["matched"],
                missing_skills=overlap["missing"],
                all_resume_skills=resume_skills,
                raw_text=resume["text"],
            )
        )

    results.sort(key=lambda r: r.final_score, reverse=True)
    return results
