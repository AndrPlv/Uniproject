from flask import Flask, render_template, request, jsonify
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

app = Flask(__name__)


@app.route('/input', methods=['POST'])
def handle_data():
  data = request.get_json()

  if None in [data[j] for j in data.keys()]:
    print("None!")
    return {'code': 0}
  else:
    data["Time"] = pd.to_datetime(data["Time"], format="%d.%m.%Y %H:%M:%S")
    dase = pd.read_csv("DataSet.csv", delimiter=";")
    dase.loc[len(dase)] = data
    dase.to_csv("DataSet.csv", index=False, sep=";")
  
  return {'code': 200}
@app.route('/update')
def update():
  base = pd.read_csv('DataSet.csv', delimiter=";")
  
  return jsonify({
        'Table': base[-15:][::-1].to_html(index=False),
        'Temperature': [int(t) for t in base['Temperature'][-len(base):]],  
        'Humidity': [int(h) for h in base['Humidity'][-len(base):]],       
        'Time': pd.to_datetime(base['Time']).to_list()
    })
  
@app.route('/')
def main():
  base = pd.read_csv('DataSet.csv', delimiter=";")

  table = base[-15:].to_html()

  Temgrapch = go.Figure()
  Temgrapch.add_trace(go.Scatter(
    x=base["Time"],
    y=base["Temperature"],
    mode='lines',
    name="Temperature"
  ))

  Humgrapch = go.Figure()
  Humgrapch.add_trace(go.Scatter(
    x=base["Time"],
    y=base["Humidity"],
    mode='lines',
    name="Humidity"
  ))

  Temgrapch = Temgrapch.to_html(full_html=False, include_plotlyjs=False)
  Humgrapch = Humgrapch.to_html(full_html=False, include_plotlyjs=False)

  return render_template("index.html", table=table, Temgrapch=Temgrapch, Humgrapch=Humgrapch)
    
 
@app.errorhandler(404)
def error(e):
  return render_template('error.html')

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=5000)