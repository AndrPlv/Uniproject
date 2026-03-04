import serial
import serial.tools.list_ports as stl
import customtkinter

root = customtkinter.CTk()

root.title("Переконфигурация станции")
customtkinter.set_appearance_mode('dark') # цвет фона
customtkinter.set_default_color_theme('green') # цвет интерфейса
root.geometry('500x500')
root.resizable(0,0)

def update_comports():
    device_list = ["Нет устройств"] if len(stl.comports()) == 0 else [j.name for j in stl.comports()]
    devices.configure(text=f"Доступные устройства: {" ".join(device_list)}")

title = customtkinter.CTkLabel(root, text="Переконфигурация станции", font=('Arial', 19))
title.place(x=120,y=10)

device_list = ["Нет устройств"] if len(stl.comports()) == 0 else [j.name for j in stl.comports()]
devices = customtkinter.CTkLabel(root, text=f"Доступные устройства: {" ".join(device_list)}", font=('Arial', 18))
devices.place(x=20,y=60)

update_device_list = customtkinter.CTkButton(root, text="Обновить список", command=update_comports)
update_device_list.place(x=350,y=100)

root.mainloop()

