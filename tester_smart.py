from datetime import datetime
from random import randint
from time import sleep
import requests


name = 'MYSTA'
mac = 'B9:E6:2T:4E:C3:H1'

for _ in range(25):
    temperature, humidity = randint(0, 30), randint(10, 100)
    DATA = {'MacAdress': mac,
            'NameSTA': name,
            'Temperature': temperature,
            'Humidity': humidity,
            'Time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    respone = requests.post(f"http://192.168.0.104:5000/input", json=DATA)
    print(r"*___________/\__________*")
    print(f'Отправленый пакет:')
    for j in DATA:
        print(f'{j} ---> {DATA[j]}')
    print(f'Ответ: {respone}')
    print(r"*___________\/__________*")    
    sleep(1)
