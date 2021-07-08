from flask import Flask, render_template

app = Flask(__name__)



# TO COMMENT OR UNCOMMENT [Ctrl + /]

#-----------------------------------------------Without Layout-----------------------------------------------------------------#

##--------------------------------------STEP 1: simple templating rendering---------------------------------------------------#
# @app.route('/')
# def index():
#     return render_template("index.html")



###--------------------------------------STEP 2: template render with arguments passing and Jinja variables--------------------#
# @app.route('/')
# def index():
#     ''' Pass message as msg to render template function''' 

#     message = "Hello, how are you?"
#     return render_template("message.html",msg=message)





###---------------------------------------STEP 3: template rendering [conditionals]------------------------------------------------#
# @app.route('/')
# def index():
#     ''' Pass message as msg and show as show from render_template'''
#     show  = True
#     message = "Hello, how are you?"
#     return render_template("conditional_msg.html",msg=message,show=False)





###-----------------------------------------STEP 4: template rendering multiples [loop]---------------------------------------------#
# @app.route('/')
# def index():
#     ''' Pass multi_message as messages from render_template'''

#     multi_message = ["Hello", "How are you?", "I am learning flask."]
#     return render_template("multiple_msg.html",messages=multi_message)






#########----------------------------------------Using Layout-------------------------------------------------------------##########

###--------------------------------------STEP 1: simple templating rendering---------------------------------------------------#
@app.route('/')
def index():
    return render_template("new_templates/index.html")





###--------------------------------------STEP 2: template render with arguments passing and Jinja variables--------------------#
# @app.route('/')
# def index():
#     message = "Hello how are you?"
#     return render_template("new_templates/message.html", msg=message)





###---------------------------------------STEP 3: template rendering [conditionals]------------------------------------------------#
# @app.route('/')
# def index():
#     show  = True
#     message = "Hello how are you?"
#     return render_template("new_templates/conditional_msg.html", show=show, msg=message)





###-----------------------------------------STEP 4: template rendering multiples [loop]---------------------------------------------#
# @app.route('/')
# def index(): 
#     ''' Pass multi_message as messages from render_template'''

#     multi_message = ["Hello", "How are you?", "I am learning flask."]

#     return render_template("new_templates/multiple_msg.html")





#if debug = True on when we make some changes in code we don't manually need to restart server
if __name__=="__main__":
    app.run(debug=True)