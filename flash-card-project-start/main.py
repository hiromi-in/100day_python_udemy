from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
timer = None
new_word = ""
#--------------------Create a word list------------------------------#

try:
    word_data = pandas.read_csv("data/words_to_learn.csv")
    to_learn = word_data.to_dict(orient="records")
except FileNotFoundError:
    word_data = pandas.read_csv("data/french_words.csv")
    to_learn = word_data.to_dict(orient="records")
#word_dict = {row.French:row.English for (index,row) in word_data.iterrows()}
#key_list = [item for item in word_dict]

#--------------------Button command----------------------------------#


def next_word():
    global new_word, timer
    window.after_cancel(timer)
    new_word = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(word, text=new_word["French"], fill="black")
    canvas.itemconfig(language, text="French", fill="black")

    timer = window.after(3000, flip)

def flip_and_remove_from_list():
    global new_word
    to_learn.remove(new_word)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()

#---------------------Flip the card----------------------------------#
is_front = True

def flip():
    global is_front, new_word, timer

    if is_front == True:
        window.after_cancel(timer)
        canvas.itemconfig(canvas_image, image=card_back)
        canvas.itemconfig(word, text=new_word["English"], fill="white")
        canvas.itemconfig(language, text="English", fill="white")
        timer = window.after(3000, flip)
        is_front = False
    elif is_front == False:
        window.after_cancel(timer)
        canvas.itemconfig(canvas_image, image=card_front)
        next_word()
        is_front = True

#---------------------UI set up--------------------------------------#
window = Tk()
window.title("Flashy")
window.config(width=800, height=750, padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
correct_button_image = PhotoImage(file="images/right.png")
wrong_button_image = PhotoImage(file="images/wrong.png")

canvas=Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(800 // 2, 526 // 2, image=card_front)
language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 253, text= "", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


correct_button = Button(image=correct_button_image, highlightthickness=0, command=flip_and_remove_from_list)
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=flip)
correct_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)


#-----------------------Execution-----------------------------------------#
next_word()

window.mainloop()