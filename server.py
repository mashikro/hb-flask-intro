"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/") #this is the root localhost:5000
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
        <head> </head>
        <body>
            <a href="http://localhost:5000/choice">Hi! <b>This is the home page.</b></a>
        </body>
    </html>"""

@app.route("/choice")
def choice():
    return"""
     <!doctype html>
    <html>
      <head>
        <title>Make a choice!</title>
      </head>
      <body>
        <h1>Hi!</h1>
            Do you want a <a href='/hello'>compliment</a> or an <a href ='/helloM'>insult</a>
        </body>
    </html>
    """

@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"> 
          <select name="compliment">
                <option value = 'awesome'>awesome</option>
                <option value = 'terrific'>terrific</option>
                <option value = 'fantastic'>fantastic</option>
                <option value = 'neato'>neato</option>
                <option value = 'fantabulous'>fantabulous</option>
                <option value = 'wowza'>wowza</option>
                <option value = 'brilliant'>brilliant</option>
                <option value = 'coolio'>coolio</option>
          <input type="submit" value="Submit">
        </form>

      </body>
    </html>
    """

@app.route("/helloM")
def say_hello_mean():

    return"""
      <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <form action="/diss">
           What's your name? <input type="text" name="person">
          <select name="diss">
                <option value = 'ugly'>ugly</option>
                <option value = 'fat'>fat</option>
                <option value = 'stupid'>stupid</option>
                <option value = 'dumb'>dumb</option>
                <option value = 'not loved'>not loved</option>
        <input type="submit" value="Submit">
        </form>
    </body>
    </html>
        """



@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")


    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)

@app.route("/diss") #go to /diss
def diss_person():

    player = request.args.get("person")

    diss = request.args.get("diss")


    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, diss)



if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0") #TRUE means we are debugging things. developer mode
