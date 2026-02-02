import serial.tools.list_ports 
import serial


def port():
    ser = []
    ports = serial.tools.list_ports.comports()
    for j in ports:
        ser.append(j.name)
    return ser