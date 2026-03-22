from datetime import datetime
from random import randint
from time import sleep
import requests


name = 'STA0_EcVi'
mac = '908:77:106:33:71'

for _ in range(100):
    temperature, humidity = randint(0, 30), randint(10, 100)
    DATA = {'MacAdress': mac,
            'NameSTA': name,
            'Temperature': temperature,
            'Humidity': humidity,
            'Time': '2026-03-22 22:30:14'}
    respone = requests.post("http://10.179.199.1:5000/input", json=DATA)
    print(r"*___________/\__________*")
    print(f'Отправленый пакет:')
    for j in DATA:
        print(f'{j} ---> {DATA[j]}')
    print(f'Ответ: {respone}')
    print(r"*___________\/__________*")    

