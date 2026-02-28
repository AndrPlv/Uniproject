from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/input', methods=['POST'])
def handle_data():
  data = request.get_json()
  print(type(data))
  print(data)
  dase = pd.read_csv("DataSet.csv", delimiter=";")
  dase.loc[len(dase)] = data
  dase.to_csv("DataSet.csv", index=False, sep=";")
  
  return {'code': 200}
@app.route('/<CODE_DEVISE>')
def main(CODE_DEVISE): 
  return render_template('index.html', title=CODE_DEVISE)
@app.errorhandler(404)
def error(e):
  return render_template('error.html')

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=5000)