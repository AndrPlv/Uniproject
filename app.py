from flask import Flask, render_template, request, jsonify
import pandas as pd
import analitic

app = Flask(__name__)


@app.route('/input', methods=['POST'])
def handle_data():
  data = request.get_json()

  if None in [data[j] for j in data.keys()]:
    return {'code': 0}
  else:
    analitic.lists_STA(data)
    analitic.smart_save(data)
  
  return {'code': 200}
@app.route('/update')
def update():
  table = analitic.table("DataSet.csv", n=-20)
  Temgrapch = analitic.graph("DataSet.csv", y="Temperature", n=-200, line_name="Temperature")
  Humgrapch = analitic.graph("DataSet.csv", y="Humidity", n=-200, line_name="Humidity") 

  return render_template("index.html", table=table, Temgrapch=Temgrapch, Humgrapch=Humgrapch)
    
 
@app.errorhandler(404)
def error(e):
  return render_template('error.html')

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=5000)