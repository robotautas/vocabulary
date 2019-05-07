from tkinter import *
import json
from difflib import get_close_matches

window = Tk()
window.title("Dicktionary")
window.resizable(FALSE, FALSE)

def translate(w):

    data = json.load(open("data.json"))
    matches = get_close_matches(word_value.get(), data.keys())
    word = word_value.get()
    if word in data.keys():
        return data[w]
    elif len(matches) > 0:
        word = matches[0]
        return data[word]
    else:
        noword = ["There's no such word in a dictionary, try something else."]
        return noword


def define(i):
    data = json.load(open("data.json"))
    matches = get_close_matches(word_value.get(), data.keys())
    word = word_value.get()
    if word in data.keys():
        return word+":\n\n"
    elif len(matches) > 0:
        return "Closest match -> "+matches[0]+":\n\n"
    else:
        return word+": \n\n"


def run_program():
    user_input = (define(word_value.get()))
    output = (translate(word_value.get()))
    t1.configure(state=NORMAL)
    t1.delete(1.0, END)
    t1.insert(END, user_input)
    for item in output:
        meaning = "*"+item+"\n"
        t1.insert(END, meaning)
    t1.configure(state=DISABLED)


word_value = StringVar()

l1 = Label(window, text="Enter a word:")
l1.grid(row=0, column=0, sticky=S+W)

e1 = Entry(window, textvariable=word_value)
e1.grid(row=1, column=0, sticky=N)

b1 = Button(window, text="Go", command=run_program)
b1.grid(row=2, column=0, sticky=N+E)

t1 = Text(window, wrap=WORD)
t1.grid(row=0, column=1, rowspan=30)

window.mainloop()
