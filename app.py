from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/input', methods=['POST'])
def handle_data():
  data = request.get_json()
  print(data)
  with open('value.txt', 'a') as file:
      file.write(f't: {data['tem']}, h: {data['hum']}\n')
  
  return {'code': 200, "time": datetime.datetime.now()}
@app.route('/<CODE_DEVISE>')
def main(CODE_DEVISE): 
  return render_template('index.html', title=CODE_DEVISE)
@app.errorhandler(404)
def error(e):
  return render_template('error.html')

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=5000)