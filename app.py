from flask import Flask, render_template, request

# Create the Flask application
app = Flask(__name__)


# Show the home page
@app.route("/")
def home():
    return render_template("index.html")


# Show the team members page
@app.route("/team")
def team():
    # Team member details
    members = [
        {
            "name": "Chong Choong Zing Shaun",
            "email": "czschong001@mymail.sim.edu.sg",
        },
        {
            "name": "Pang Tian Ci",
            "email": "tcpang001@mymail.sim.edu.sg",
        },
        {
            "name": "Thangaraju Ajath Shatru",
            "email": "thangara005@mymail.sim.edu.sg",
        },
        {
            "name": "Teo Zhijie",
            "email": "zteo009@mymail.sim.edu.sg",
        },
    ]
    return render_template("team.html", members=members)


# Show the documentation page
@app.route("/documentation")
def documentation():
    return render_template("docs.html")


# Show and process the request form
@app.route("/form", methods=["GET", "POST"])
def form():
    action_type = request.args.get("type", "Contact Us")
    submitted = False
    name = ""

    # Get the form details after submission
    if request.method == "POST":
        action_type = request.form.get("action_type", action_type)
        name = request.form.get("name", "")
        submitted = True

    return render_template(
        "form.html",
        action_type=action_type,
        submitted=submitted,
        name=name,
    )


# Run the website locally
if __name__ == "__main__":
    app.run(debug=True, port=5001)
