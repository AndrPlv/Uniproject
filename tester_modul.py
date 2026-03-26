import pandas as pd
def main(NameSTA):
  disp = pd.read_csv("DataSets/STAes_list.csv", delimiter=";")
  fail_work = f'{disp[disp["NameSTA"] == NameSTA]["FileName"].values[0]}.csv'
  DATASET = pd.read_csv(f"DataSets/{fail_work}", delimiter=";")
  

main("STA1")