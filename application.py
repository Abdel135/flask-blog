from flask import Flask , render_template ,url_for ,flash,redirect
from form import registration, Login

app=Flask(__name__)

app.config["SECRET_KEY"]="08e9eaa0aa7461a98fabe2f724a59243"

posts=[
    {
        "title":"Blog 1",
        "author" : "Abdel",
        "Date" : "12/12/2020" 
    },
    {
        "title":"Blog 2",
        "author" :"Mike",
        "Date" :"9/8/2012"
    },
    {
        "title" : "Blog 3",
        "author" : "Jeff",
        "Date"  : "01/02/2003"
    }
]


@app.route("/")
@app.route("/home",methods=["GET","POST"])
def home():
    return render_template("home.html",posts=posts,title="Flask app!")

@app.route("/about")
def about():
    return render_template("about.html",posts=posts)

@app.route("/register",methods=["GET","POST"])
def register():
    form=registration()
    if form.validate_on_submit():
        flash(f"Your account of '{form.username.data}' has been created!","success")
        return redirect(url_for("home"))
    return render_template("register.html",title="Register",form=form)

@app.route("/login")
def login():
    form=Login()
    return render_template("login.html",form=form)




if __name__=="__main__":
    app.run(debug=True) 