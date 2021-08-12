from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)
arr = [1, 2, 3, 4]


@app.route('/home')
def test():
    return render_template("index.html")


@app.route('/bubble_sort')
def bubble():
    return render_template("bubble.html")


@app.route('/merge_sort')
def merge():
    return render_template("merge.html")


@app.route("/selection_sort")
def selection():
    return render_template("selection.html")


@app.route("/<usr>")
def user(usr):
    return "<h1>" + usr + "</h1>"


@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Logan!"))


if __name__ == "__main__":
    app.run(debug=True)
