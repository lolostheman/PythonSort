from flask import Flask, redirect, url_for, render_template, request, Response, make_response
import matplotlib.pyplot as plt
import json
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import pandas as pd
from matplotlib.figure import Figure
import numpy as np
from time import time
from random import random

app = Flask(__name__)
arr = [1, 2, 3, 4]

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True


@app.route('/home')
def test():
    return render_template("index.html")


@app.route('/live-data')
def live_data():
    data = [time() * 100, random() * 100]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response


@app.route('/plot.png')
def plot_png():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = np.random.rand(100)
    ys = np.random.rand(100)
    axis.plot(xs, ys)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/bubble_sort', methods=("POST", "GET"))
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
