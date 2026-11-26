import re

SKILL_DATABASE = {
    "Programming Languages": [
        "python",
        "java",
        "c++",
        "c",
        "javascript",
        "sql"
    ],

    "Frameworks": [
        "django",
        "flask",
        "fastapi"
    ],

    "Databases": [
        "mysql",
        "postgresql",
        "sqlite",
        "mongodb"
    ],

    "Libraries": [
        "pandas",
        "numpy",
        "matplotlib",
        "scikit-learn"
    ],

    "Tools": [
        "git",
        "github",
        "docker"
    ],

    "AI and Machine Learning": [
        "machine learning",
        "deep leraning",
        "natural learning processing",
        "tensorflow",
        "pytorch"
    ]
}


SKILL_ALIASES = {
    "sklearn": "scikit-learn",
    "restful api": "rest api",
    "js": "javascript",
    "postgres": "postgresql",
    "numpy library": "numpy",
    "pandas library": "pandas"
}


def extract_skills(text):

    found_skills = set()

    for category, skills in SKILL_DATABASE.items():
        for skill in skills:
            pattern = (
                r"(?<![a-z0-9])"
                + re.escape(skill)
                + r"(?![a-z0-9])"
            )

            if re.search(pattern, text, re.IGNORECASE):
                canonical_skill = SKILL_ALIASES.get(skill, skill)
                found_skills.add(canonical_skill)

    return sorted(found_skills)