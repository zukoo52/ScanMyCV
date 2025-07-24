from flask import Flask, render_template, request
from resume_utils import extract_text, analyze_resume

import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["resume"]
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Extract text and analyze
        text = extract_text(filepath)
        score, breakdown, tips = analyze_resume(text)

        return render_template("result.html", score=score, breakdown=breakdown, tips=tips, text=text)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
