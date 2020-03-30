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

x = []
unique_x = set()
y = []
c = []
d = []
r = []


@app.route("/")
def wow():
	tconf=json_response['latest']['confirmed']
	#trecov=json_response['latest']['recovered']
	tdeaths=json_response['latest']['deaths']

	n = len(json_response['locations'])

	for i in range(n):
		
		x.append(json_response['locations'][i]['country'])
		unique_x.add(json_response['locations'][i]['country'])
		
		if json_response['locations'][i]['province']=="":
			y.append(" NA ")
		else:
			y.append(json_response['locations'][i]['province'])


		c.append(json_response['locations'][i]['latest']['confirmed'])
		r.append(json_response['locations'][i]['latest']['recovered'])
		d.append(json_response['locations'][i]['latest']['deaths'])
	len_set = len(unique_x)
	return render_template("wow.html",x=x,n=n,y=y,c=c,r=r,d=d,ux=unique_x,len_set=len_set,tconf=tconf,tdeaths=tdeaths)
	# return render_template("wow.html",conf=conf)


@app.route("/plot")
def create_plot():
    x = np.linspace(0, 1, 40)
    y = np.random.randn(40)

    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


    data = [
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return(graphJSON,json_response)


@app.route("/json")
def show_json():
	return(json_response)

if __name__ == '__main__':
    app.run()