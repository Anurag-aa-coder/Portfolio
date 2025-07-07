from flask import Flask, render_template
from form import ContactForm

app = Flask(__name__)
app.secret_key = 'thisis_contactform_secretekey'  

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title= "About")


@app.route("/base")
def base():
    return render_template("base.html", title="Base")
    
@app.route("/projects")
def projects():
    return render_template("projects.html", title="Projects")

@app.route("/contact",methods=["GET", "POST"])
def contact():
    form=ContactForm()
    return render_template("contact.html", form=form,title="Contact")
    
if __name__ == "__main__":
    app.run(debug=True)
