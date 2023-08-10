import serial
import customtkinter as ctk

app = ctk.CTk()
app.geometry("1280x720")
app.resizable(False, False)

# ser = serial.Serial("com3", 9600)

# def send_base(value):
#     ser.write(str(value).encode())

base_slider = ctk.CTkSlider(app, from_=0, to=1024)  
base_slider.place(relx=)

elbow_slider = ctk.CTkSlider(app, from_=2000, to=2180)
base_slider.place(relx=)

app.mainloop()