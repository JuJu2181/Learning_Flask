from flask import Flask, request, render_template, redirect
from utils import save_contact
app = Flask(__name__)


@app.route('/',methods = ["GET", "POST"])
def contact():

    if request.method=="GET":
        return render_template("portfolio.html")

    if request.method =="POST":
        name =  request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        
        save_contact(name, email, phone)

        return redirect('/')



if __name__== "__main__":
    app.run(debug=True)