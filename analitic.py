import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

def table(name: str, n=-15, delimiter=";"):
  base = pd.read_csv(name, delimiter=delimiter)
  table = base[n:]
  print(table)

def graph(name: str, y, n=-15, line_name=";", delimiter=";"):
    base = pd.read_csv(name, delimiter=delimiter)

    time = pd.to_datetime(base["Time"], format="%Y-%m-%d %H:%M:%S").dt.strftime("%H:%M:%S")

    graphs = go.Figure()
    graphs.add_trace(go.Scatter(
    x=time,
    y=base[y],
    mode='lines',
    name=line_name
    ))

    return graphs.to_html(full_html=False, include_plotlyjs=False)