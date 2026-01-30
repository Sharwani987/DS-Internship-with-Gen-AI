from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    matches = []
    if request.method == "POST":
        test_string = request.form["testString"]
        regex_pattern = request.form["regexPattern"]
        try:
            matches = re.findall(regex_pattern, test_string)
        except re.error:
            matches = ["Invalid regex pattern"]
    return render_template("index.html", matches=matches)

if __name__ == "__main__":
    app.run(debug=True)