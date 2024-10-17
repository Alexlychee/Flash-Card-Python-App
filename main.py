from tkinter import *
from pandas import read_csv
import random
BACKGROUND_COLOR = "#B1DDC6"

############################# CARD FUNCTIONALITY #############################
data = read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

# Displays the French card
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, flip)

# Flip card to show translation
def flip():
    card_back = PhotoImage(file="images/card_back.png")
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)


############################# USER INTERFACE #############################
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Flash Card
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

next_card()
flip_timer = window.after(3000, func=flip)

window.mainloop()


