import json

# Load predefined skills
with open('skills.json') as f:
    SKILL_LIST = json.load(f)

def match_skills(resume_text, job_text):
    matches = []
    for skill in SKILL_LIST:
        if skill.lower() in resume_text.lower() and skill.lower() in job_text.lower():
            matches.append(skill)
    return matches
