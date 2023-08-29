import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()
root.geometry('800x800')

rocket_label = tk.Label(root, bg="blue", width=3, height=4)
rocket_label.place(x=400, y=730)
speed_label = tk.Label(root, text="Rocket Speed:\n", bg="white", width=16, height=5, bd=1,
                                            relief="solid")
speed_label.place(x=680, y=400)
new_x = 400
new_y = 730
g = 1
prev_y = new_y
speed = 0
constant_speed = False
a = 1
explosion_true = False
def rocket_up():
   global explosion_true
   global new_x
   global new_y
   global g
   global prev_y, speed
   global constant_speed
   global a
   x = rocket_label.winfo_x()
   y = rocket_label.winfo_y()
   if not explosion_true:
       prev_y = new_y
       new_y = y - g
       if not constant_speed:
           g += a
           a -= 0.005
       speed = abs(new_y - prev_y)
       rocket_label.place(x=400, y=new_y)
       if new_y <= 0:
           rocket_label.place(x=400, y=800)
           new_y = 800
       if new_y > 800:
           rocket_label.place(x=400, y=0)
           new_y = 0
       if speed >= 100:
           constant_speed = True
       root.after(100, rocket_up)
   if new_y <= 0 and rocket_screen <= 0:
       explosion_true = True
   if explosion_true:
       rocket_explode()

def rocket_speed():
   global new_x
   global new_y
   global speed
   speed_label.config(text=f"Rocket Speed:\n{int(speed)}")
   root.after(100, rocket_speed)
fuel_label = tk.Label(root, text="Fuel:", bg="white", bd=1, relief="solid")
fuel_label.place(x=20, y=20)
fuel_back = tk.Label(root, bg="white", bd=4, relief="solid", height=1, width=30, fg="black")
fuel_back.place(x=20, y=40)
fuel_top = tk.Label(root, bg="red", height=1, width=30)
fuel_top.place(x=20, y=40)
fuel = 10000
rocket_screen = 0
rocket_flying = True
def rocket_distance():
   global rocket_screen
   global speed
   global rocket_flying
   global new_y
   distance_label = tk.Label(root, width=10, height=7, bg="white", bd=1, relief="solid",
                             text=f"Rocket_screen:\n{rocket_screen}")
   distance_label.place(x=20, y=200)
   if rocket_flying:
       if new_y == 800:
           rocket_screen += 1
           distance_label.config(text=f"Rocket_screen:\n{rocket_screen}")
   if rocket_screen == 32:
       rocket_flying = False
   if not rocket_flying:
       if new_y == 0:
           rocket_screen -= 1
           distance_label.config(text=f"Rocket_screen:\n{rocket_screen}")
   print(new_y)
   root.after(100, rocket_distance)
def rocket_fuel():
   global speed
   global fuel
   fuel_int = int((fuel / 10000) * 30)
   fuel_top.config(width=fuel_int)
   fuel -= speed
   if fuel_int <= 0:
       no_fuel()
   root.after(100, rocket_fuel)
def no_fuel():
   fuel_top.place_forget()
   fuel_back.config(text="NO FUEL!!")
   global new_y
   global constant_speed
   x = rocket_label.winfo_x()
   y = rocket_label.winfo_y()
   constant_speed = False
   root.after(100, no_fuel)
image = Image.open(r"C:\Users\josep\Downloads\explosion_picture.png")
resize_image = image.resize((300, 300))
img = ImageTk.PhotoImage(resize_image)

explosion = tk.Label(image=img)
explosion.image = img

def rocket_explode():
   global new_y
   global rocket_screen
   global explosion
   explosion.place(x=300, y=550)
   root.after(100, rocket_explode)
   rocket_label.place_forget()
rocket_distance()
rocket_fuel()
root.after(1000, rocket_up)
rocket_speed()
root.mainloop()
