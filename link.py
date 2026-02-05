import serial.tools.list_ports 
import serial
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
@logger
def link(COMPORT: str, values: int):
    ser = serial.Serial(COMPORT, 9600)
    DATE = []
    for _ in range(values):
        inp = str(ser.readline(), 'utf-8').strip().split(',')
        DATE.append([inp[0],inp[1],'xx:xx:xx'])
    ser.close()
    return DATE
print(link('COM4', 5))