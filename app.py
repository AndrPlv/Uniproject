from flask import Flask,render_template
import link
app = Flask(__name__)

@app.route('/')
def hello_world():
  if len(link.port()):
    out_data_ports = f'Доступные порты: {' '.join(link.port())}.'
    return render_template('index.html', inf_ports=out_data_ports) 
  else:
    return render_template('error_port.html')     
@app.errorhandler(404)
def error(e):
  return render_template('error.html')

if __name__ == '__main__':
  app.run(debug=True)