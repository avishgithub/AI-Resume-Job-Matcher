def generate_recommendations(missing_skills):
    recommendations = []

    skills_suggestions = {
        "python": "Practice Python fundamentals, functions and OOP.",
        "sql": "Practice SQL queries, joins and database operations.",
        "django": "Learn Django models, views, templates and CRUD operations.",
        "flask": "Build a small web application using Flask.",
        "rest api": "Learn REST principles and practice API development and testing.",
        "pandas": "Practice data cleaning and manipulation using Pandas.",
        "numpy": "Learn NumPy arrays and numerical operations.",
        "machine learning": "Study supervised learning and build a basic ML project.",
        "git": "Practice Git commands, branching and version control.",
        "mysql": "Practice database design, normalization and MySQL queries.",
        "postgresql": "Learn PostgreSQL queries and relational database concepts."
    }

    for skill in missing_skills:
        suggestion = skills_suggestions.get(
            skill.lower(),
            f"study {skill} and build a small practical project using it."
        )

        recommendations.append({
            "skill": skill,
            "suggestion": suggestion
        })

    return recommendations