from flask import Flask, render_template
import numpy as np
import pandas as pd
import plotly
import plotly.graph_objs as go
import json
import requests


app = Flask(__name__)


response = requests.get("https://coronavirus-tracker-api.herokuapp.com/v2/locations")
json_response = response.json()

def create_plot():
    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


    data = [
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


@app.route("/")
def hello():
	bar = create_plot()
	return render_template("index.html",plot=bar)
