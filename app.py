import os
import flask as fl

app = fl.Flask(__name__, template_folder="pages", static_folder="assets")

nfiles = len(
    [
        file.name
        for file in os.scandir("pages")
        if file.name[0] == "V" and file.name[1].isdecimal()
    ]
)

@app.route("/")
def index():
    return fl.render_template("last.html")


@app.route("/menu")
def menu():
    return fl.render_template("menu.html", len=nfiles)


@app.route("/<string:version>.html")
def version(version):
    return fl.render_template("{0}.html".format(version))


if __name__ == "__main__":
    app.run(debug=1)
