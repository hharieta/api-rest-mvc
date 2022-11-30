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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
