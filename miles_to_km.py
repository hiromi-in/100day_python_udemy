from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=350, height=150)
window.config(padx=70, pady=70)

mile_input = Entry(width=10)
mile_input.grid(column=1, row=0)

mile_text = Label(text="Miles", font=("Arial", 15, "normal"))
mile_text.grid(column=2, row=0)
is_equal_to = Label(text="is equal to", font=("Arial", 14, "normal"))
is_equal_to.grid(column=0, row=1)
km_result = Label(text="0", font=("Arial", 17, "normal"))
km_result.grid(column=1, row=1)
km_text = Label(text="Km", font=("Arial", 14, "normal"))
km_text.grid(column=2, row=1)

def button_clicked():
    value = mile_input.get()
    calc_km = round(int(value) * 1.609, 2)
    km_result.config(text=calc_km)

calc_button = Button(text="Calculate", command=button_clicked)
calc_button.grid(column=1, row=2)



window.mainloop()