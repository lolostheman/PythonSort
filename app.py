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
from main import bubble_sort
from main import randomArray
from main import selection_sort
from main import merge_sort

app = Flask(__name__)
arr = randomArray(20)
i = 0
num = -1


@app.route('/home')
def test():
    return render_template("index.html")


@app.route('/live-data-bubble')
def live_data_bubble():
    global arr
    global i
    data = [i, arr[i]]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    i += 1
    if i == len(arr):
        arr = bubble_sort(arr)
        i = 0
    return response


@app.route('/live-data-selection')
def live_data_selection():
    global arr
    global i
    data = [i, arr[i]]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    i += 1
    if i == len(arr):
        arr = selection_sort(arr)
        i = 0
    return response


@app.route('/live-data-merge')
def live_data_merge():
    global arr
    global i
    data = [i, arr[i]]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    i += 1
    if i == len(arr):
        arr = merge_sort(arr)
        i = 0
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
    global arr
    global i
    global num
    arr = randomArray(20)
    i = 0
    num = -1
    return render_template("bubble.html")


@app.route('/merge_sort')
def merge():
    global arr
    global i
    global num
    arr = randomArray(20)
    i = 0
    num = -1
    return render_template("merge.html")


@app.route("/selection_sort")
def selection():
    global arr
    global i
    global num
    arr = randomArray(20)
    i = 0
    num = -1
    return render_template("selection.html")




if __name__ == "__main__":
    app.run(debug=True)
