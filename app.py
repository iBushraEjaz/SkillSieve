from flask import Flask, render_template, request
from parser import extract_resume_text
from matcher import match_skills
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    matched_skills = []
    job_text = ""

    # Read job description
    try:
        with open('job_description.txt', 'r') as f:
            job_text = f.read()
    except FileNotFoundError:
        job_text = "Job description not available."

    if request.method == 'POST':
        file = request.files['resume']
        if file:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)

            resume_text = extract_resume_text(path)
            matched_skills = match_skills(resume_text, job_text)

    return render_template('index.html', skills=matched_skills, job_desc=job_text)

if __name__ == '__main__':
    app.run(debug=True)
