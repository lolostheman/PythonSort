from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
arr = [1, 2, 3, 4]


@app.route('/home')
def test():
    return render_template("index.html", content="pussy juice")


@app.route("/<name>")
def user(name):
    return "Hello, " + "<h1>"+name+"</h1>"


@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Logan!"))


if __name__ == "__main__":
    app.run(debug=True)
