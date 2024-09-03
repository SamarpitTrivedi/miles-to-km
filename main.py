from tkinter import *



window = Tk()
window.minsize(width= 250, height= 200)
window.config(padx=20,pady=20)
window.title("Mile to Km Converter")

def convert_to_km():
    miles = float(miles_input.get())
    km = int(miles)*1.609
    kilometer_result_label.config(text=f"{km}")



miles_input = Entry(width=10)
miles_input.grid(column=4,row=3)

miles_label = Label(text="Miles")
miles_label.grid(column=5,row=3)

is_equal_to = Label(text="Is equal to")
is_equal_to.grid(column=2,row=6)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=4,row=6)

kilometer_label = Label(text="km")
kilometer_label.grid(column=6,row=6)

button = Button(text="Convert",command=convert_to_km)
button.grid(column=4,row=8)























window.mainloop()