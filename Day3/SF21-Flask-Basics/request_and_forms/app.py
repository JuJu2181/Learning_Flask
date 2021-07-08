
from flask import Flask, render_template,request

app = Flask(__name__)




# @app.route('/')
# def index():
#     return render_template("form.html")




####------------------STEP 1: request introduction and ------------------------------------------###

# @app.route('/message')
# def message():
#     message = request.args.get('msg')
#     return render_template('message.html', msg=message)


####----------------------STEP 2: form and http methods -----------------------------------------###

# @app.route('/message',methods=["GET","POST"])
# def message():
#     message = request.form.get('msg')
#     return render_template("message.html", msg=message)








####-----------------------STEP 3: GET and POST using same endpoint---------------------------------###
### Pass methods in app.route
@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("form.html")

    if request.method == "POST":
        message = request.form.get('msg')
        return render_template("message.html", msg=message)





if __name__=="__main__":
    app.run(debug=True)