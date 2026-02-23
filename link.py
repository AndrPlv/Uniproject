import serial.tools.list_ports 
import serial
import requests
from time import perf_counter


def logger(func):
    def timework(*args):
        time0 = perf_counter()
        print(func(*args))
        time1 = perf_counter()
        print(f'Working time: {round(time1-time0,3)}')
    return timework

def port():
    ser = []
    ports = serial.tools.list_ports.comports()
    for j in ports:
        ser.append(j.name)
    return ser
def link(COMPORT: str, values: int):
    ser = serial.Serial(COMPORT, 9600)
    for _ in range(values):
        inp = str(ser.readline(), 'utf-8').strip().split(',')
        data = {'tepm': inp[0], 'hum': inp}
        response = requests.post('http://192.168.0.104:5000/input', json=data)
        print(f"Статус: {response.status_code}")
        print(f"Ответ: {response.text}")
    ser.close()
