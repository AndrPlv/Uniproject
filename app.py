from flask import Flask, render_template, request, jsonify
from time import perf_counter
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

@app.route('/<NameSTA>')
def main(NameSTA):
  time = perf_counter()

  working_file = analitic.name_fail_DATASET(NameSTA)
  if working_file is None:
    return render_template('error.html')
  else:
    table = analitic.table(working_file)
    graph_tem = analitic.graph(name=working_file, y="Temperature", line_name="Temperature")
    graph_hum = analitic.graph(name=working_file, y="Humidity", line_name="Humidity")
    
    print(f"Время ответа main: {perf_counter() - time}")
    return render_template('index.html', NameSTA=NameSTA, table=table, Temgrapch=graph_tem, Humgrapch=graph_hum) 
@app.route('/update/<NameSTA>')
def update(NameSTA):
  working_file = analitic.name_fail_DATASET(NameSTA)
  base = pd.read_csv(working_file, delimiter=";")
  return jsonify({
        'Table': base[-15:][::-1].to_html(index=False),
        'Temperature': [int(t) for t in base['Temperature'][-len(base):]],  
        'Humidity': [int(h) for h in base['Humidity'][-len(base):]],       
        'Time': pd.to_datetime(base['Time']).to_list()
  })

@app.errorhandler(404)
def error(e):
  return render_template('error.html')

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=5000)