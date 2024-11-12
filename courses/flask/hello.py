from flask import Flask, render_template
from markupsafe import escape


app = Flask("Web App")

@app.route("/")
def helloWorld():
    return "<h1> Hello World !!! </h1>"


@app.route("/blogs")
def blogs():
    user = 'freire'
    return f'<h1> Hello World {escape(user)} </h1>'


@app.route("/<user>")
def helloUser(user='freire'):
    return render_template("about.html", user_name=user)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == '__main__':
    app.run(debug=True)