from flask import render_template
from models.models import Person
import config
# import connexion

### adding a REST API URL endpoint to your Flask application ###

app = config.connex_app
app.add_api(config.base_dir / "swagger.yml")

@app.route("/")
def home():
    # query the Person model to get all the data from 
    # the person table and pass it on to render_template() 
    people = Person.query.all()
    return render_template("home.html", people=people)


# Create a URL route in our application for "/people"
@app.route("/people")
@app.route("/people/<int:person_id>")
def people(person_id=""):
    """
    This function just responds to the browser URL
    localhost:5000/people

    :return:        the rendered template "people.html"
    """
    return render_template("people.html", person_id=person_id)


# Create a URL route to the notes page
@app.route("/people/<int:person_id>")
@app.route("/people/<int:person_id>/notes")
@app.route("/people/<int:person_id>/notes/<int:note_id>")
def notes(person_id, note_id=""):
    return render_template("notes.html", person_id=person_id, note_id=note_id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
