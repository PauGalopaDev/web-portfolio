import os
import json
import flask as fl

app = fl.Flask(__name__, template_folder="pages", static_folder="assets")

nfiles = len(
    [
        file.name
        for file in os.scandir("pages")
        if file.name[0] == "V" and file.name[1].isdecimal()
    ]
)

@app.route("/", methods=['GET', 'POST'])
def index():
    sides = None
    with open("sides.json", "+r") as s:
        sides = json.load(s)
    
    if fl.request.method == 'POST':
        form = json.dumps(fl.request.form)
        with open("messages.json", '+a') as m:
            m.write(form + ',') #Not sending an email for security reasons

    return fl.render_template("last.html", sides=sides)

@app.route("/menu")
def menu():
    return fl.render_template("menu.html", len=nfiles)


@app.route("/<string:version>.html")
def version(version):
    return fl.render_template("{0}.html".format(version))


if __name__ == "__main__":
    app.run(debug=1)
