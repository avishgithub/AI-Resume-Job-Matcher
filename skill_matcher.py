def compare_skills(resume_skills, job_skills):
    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched_skills = resume_set.intersection(job_set)
    missing_skills = job_set.difference(resume_set)
    extra_skills = resume_set.difference(job_set)

    total_job_skills = len(job_set)
    total_matched_skills = len(matched_skills)

    if total_job_skills > 0:
        coverage = (total_matched_skills / total_job_skills) * 100

    else: 
        coverage = 0
    
    return {
        "matched": sorted(matched_skills),
        "missing": sorted(missing_skills),
        "extra": sorted(extra_skills),
        "coverage": round(coverage, 2)
    }