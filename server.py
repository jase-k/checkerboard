# Your program should have the following output

# http://localhost:5000/(x)/(y) - should display x by y checkerboard.  For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard.  Before you pass x or y to Jinja, please remember to convert it to integer first (so that you can use x or y in a for loop)

from flask import Flask, render_template

app = Flask(__name__)

# http://localhost:5000 - should display 8 by 8 checkerboard
@app.route('/')
def hello():
    return render_template("index.html", rows = 8, columns = 8, color1 = "white", color0= 'black')

# http://localhost:5000/4 - should display 8 by 4 checkerboard
@app.route('/<int:cols>')
def columns(cols):
    return render_template("index.html",  columns = cols, rows = 8, color1 = "white", color0= 'black')

# http://localhost:5000/4 - should display 8 by 4 checkerboard
@app.route('/<int:cols>/<int:rws>')
def fullboard(cols, rws):
    return render_template("index.html",  columns = cols, rows = rws, color1 = "white", color0= 'black')

@app.route('/<int:cols>/<int:rws>/<string:color1>/<string:color0>')
def colorboard(cols, rws, color1, color0):
    return render_template("index.html",  columns = cols, rows = rws, color1 = color1, color0=color0)


@app.errorhandler(404)
def handle_error(e):
    return "Sorry no page here", 404

if(__name__ == "__main__"):
    app.run(debug=True)