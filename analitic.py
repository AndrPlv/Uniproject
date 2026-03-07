import plotly.graph_objects as go
import pandas as pd

fig = go.Figure()

base = pd.read_csv('DataSet.csv', delimiter=";")
fig.add_trace(go.Scatter(
    x=[j for j in range(len(base))],
    y=base["Temperature"],
    mode='lines+markers+text',           # только линии
    name='Название линии'
))
fig.add_trace(go.Scatter(
    x=[j for j in range(len(base))],
    y=base["Humidity"],
    mode='lines+markers+text',           # только линии
    name='Название линии'
))

fig.show()  # Показать