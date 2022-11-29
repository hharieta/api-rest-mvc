from flask import Flask, render_template
import connexion

### adding a REST API URL endpoint to your Flask application ###

"""
Application instance using Connexion rather than Flask:

app = Flask(__name__.split(".")[0])

Internally, the Flask app is still created, 
but it now has additional functionality added to it
"""
app = connexion.App(__name__.split(".")[0], specification_dir="./")
app.add_api("swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
