"""
skills.py
---------
Lightweight, dependency-free skill extraction.

Rather than relying on a heavyweight NER model (which would require large
downloads), this module matches resume/JD text against a curated, editable
skills taxonomy (`SKILLS_DB`) using word-boundary regex matching. This is
fast, transparent, and easy for users to extend for their own domain.
"""

import re
from typing import List, Set

# Editable skills taxonomy. Extend this list to fit your own domain/industry.
SKILLS_DB = [
    # Programming languages
    "Python", "Java", "JavaScript", "TypeScript", "C++", "C#", "Go", "Rust",
    "R", "SQL", "PHP", "Ruby", "Swift", "Kotlin", "Scala", "MATLAB",
    # Data Science / ML
    "Machine Learning", "Deep Learning", "NLP", "Natural Language Processing",
    "Computer Vision", "Data Science", "Data Analysis", "Data Visualization",
    "Statistics", "TF-IDF", "Cosine Similarity", "Feature Engineering",
    "Model Deployment", "MLOps", "A/B Testing", "Reinforcement Learning",
    # Libraries / frameworks
    "Scikit-Learn", "TensorFlow", "PyTorch", "Keras", "Pandas", "NumPy",
    "Matplotlib", "Seaborn", "OpenCV", "SpaCy", "NLTK", "Hugging Face",
    "XGBoost", "LightGBM", "Streamlit", "Flask", "Django", "FastAPI",
    "React", "Angular", "Vue.js", "Node.js", "Express.js",
    # Data / cloud / infra
    "AWS", "Azure", "GCP", "Docker", "Kubernetes", "Git", "GitHub",
    "CI/CD", "Linux", "REST API", "GraphQL", "Airflow", "Spark", "Hadoop",
    "Kafka", "PostgreSQL", "MySQL", "MongoDB", "Redis", "Snowflake",
    "Power BI", "Tableau", "Excel",
    # Soft / general
    "Communication", "Leadership", "Project Management", "Agile", "Scrum",
    "Problem Solving", "Teamwork", "Time Management",
]

# Pre-build case-insensitive, word-boundary regex patterns once for speed.
_SKILL_PATTERNS = [
    (skill, re.compile(r"(?<![A-Za-z0-9])" + re.escape(skill) + r"(?![A-Za-z0-9])", re.IGNORECASE))
    for skill in SKILLS_DB
]


def extract_skills(text: str, custom_skills: List[str] = None) -> List[str]:
    """
    Return the list of known skills (from SKILLS_DB plus any custom_skills)
    found in `text`, preserving the canonical casing from the taxonomy.
    """
    found: Set[str] = set()
    patterns = list(_SKILL_PATTERNS)
    if custom_skills:
        patterns += [
            (s, re.compile(r"(?<![A-Za-z0-9])" + re.escape(s) + r"(?![A-Za-z0-9])", re.IGNORECASE))
            for s in custom_skills
        ]

    for canonical, pattern in patterns:
        if pattern.search(text):
            found.add(canonical)

    return sorted(found)


def skill_overlap(resume_skills: List[str], jd_skills: List[str]) -> dict:
    """
    Compare a resume's skills against a job description's required skills.
    Returns matched skills, missing skills, and a simple match percentage.
    """
    resume_set = {s.lower() for s in resume_skills}
    jd_set = {s.lower() for s in jd_skills}

    matched = sorted(s for s in jd_skills if s.lower() in resume_set)
    missing = sorted(s for s in jd_skills if s.lower() not in resume_set)

    match_pct = round(100 * len(matched) / len(jd_skills), 1) if jd_skills else 0.0

    return {
        "matched": matched,
        "missing": missing,
        "match_percent": match_pct,
    }
