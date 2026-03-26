import plotly.graph_objects as go
import pandas as pd


def table(name: str, n=-15, delimiter=";"):
  base = pd.read_csv(name, delimiter=delimiter)
  return base[n:].to_html(index=False)

def graph(name: str, y: str, line_name=";", delimiter=";"):
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
def lists_STA(pack: dict):
  DataSet_operator = pd.read_csv("DataSets\STAes_list.csv", delimiter=";")
  try:
    if pack["NameSTA"] != DataSet_operator[DataSet_operator["MacAdress"] == pack["MacAdress"]]["NameSTA"].values[0]:
        mask = DataSet_operator["MacAdress"] == pack["MacAdress"]
        DataSet_operator.loc[mask, "NameSTA"] = pack["NameSTA"]
  except:
    DataSet_operator.loc[len(DataSet_operator)] = {"MacAdress": pack["MacAdress"], "NameSTA": pack["NameSTA"], "FileName": f'{pack["NameSTA"]}'}
    DataSet_STA = pd.DataFrame(columns=['Time', 'Temperature', 'Humidity'])
    DataSet_STA.to_csv(f'DataSets/{pack["NameSTA"]}.csv', index=False, sep=";")
  finally:
    DataSet_operator.to_csv("DataSets/STAes_list.csv", index=False, sep=";") 
def smart_save(pack: dict):
  DataSet_operator = pd.read_csv("DataSets\STAes_list.csv", delimiter=";")
  working_fail = DataSet_operator[DataSet_operator["MacAdress"] == pack["MacAdress"]]["FileName"].values[0]

  DataSet_STA = pd.read_csv(f"DataSets\{working_fail}.csv", delimiter=";")
  DataSet_STA.loc[len(DataSet_STA)] = {"Time": pd.to_datetime(pack["Time"]),
                                       "Temperature": pack["Temperature"],
                                       "Humidity": pack["Humidity"]}
  DataSet_STA.to_csv(f"DataSets\{working_fail}.csv", index=False, sep=";")
def name_fail_DATASET(NameSTA: str):
  disp = pd.read_csv("DataSets/STAes_list.csv", delimiter=";")
  try:
    fail_work = f'{disp[disp["NameSTA"] == NameSTA]["FileName"].values[0]}.csv'
    return f'DataSets/{fail_work}'
  except:
    return None