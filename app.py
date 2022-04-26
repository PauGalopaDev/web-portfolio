import os
import json
import flask as fl

app = fl.Flask(__name__, template_folder="pages", static_folder="assets")


@app.route("/", methods=['GET', 'POST'])
def index():
    sides = None
    with open("sides.json", "+r") as s:
        sides = json.load(s)

    return fl.render_template("index.html", sides=sides)


"""
I had to cut it out :(

@app.route("/menu")
def menu():
    return fl.render_template("menu.html", len=nfiles)

@app.route("/<string:version>.html")
def version(version):
    return fl.render_template("{0}.html".format(version))
"""

if __name__ == "__main__":
    app.run(debug=1)
