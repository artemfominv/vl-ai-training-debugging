from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-super-secret-password-do-not-use-in-prod'  # BAD PRACTICE

# In-memory bug list (dummy data)
bugs = [
    {'id': 1, 'title': 'Login page crashes', 'severity': 'High'},
    {'id': 2, 'title': 'CSS not loading', 'severity': 'Low'},
]

@app.route("/")
def index():
    return render_template("index.html", bugs=bugs)

@app.route("/calculate_severity", methods=["GET", "POST"])
def calculate_severity():
    if request.method == "POST":
        impact = request.form["impact"]              # string, e.g. "10"
        urgency = request.form["urgency"]            # string, e.g. "high"
        urgency_map = {"low": "1", "medium": "2", "high": "3"}  # strings on purpose
        urgency_multiplier = urgency_map.get(urgency, "1")      # string, e.g. "3"
        score = impact * urgency_multiplier          # TypeError: can't multiply str by str
        return render_template("severity_result.html", score=score)
    return render_template("calculate_severity.html")

def format_username(email):
    """Takes jane.doe@example.com -> Doe, Jane"""
    name_part = email.split("@")[0]  # Fixed: get the name part before @
    first, last = name_part.split(".")  # This will still raise for edge cases
    return f"{last.capitalize()}, {first.capitalize()}"

def calculate_bug_priority(severity, assigned_team_size):
    """Calculate bug priority based on severity and team size.
    Higher severity and smaller team = higher priority"""
    priority_matrix = {
        "low": 1,
        "medium": 2, 
        "high": 3,
        "critical": 4
    }
    base_priority = priority_matrix.get(severity.lower(), 1)
    # Division by zero potential here!
    adjusted_priority = base_priority * (10 / assigned_team_size)
    return round(adjusted_priority, 2)

if __name__ == "__main__":
    app.run(debug=True)
