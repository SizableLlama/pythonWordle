from tkinter import *

#Alphabet buttons for wordle game!
def create_alphabet_buttons(root):
    letters= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    buttons = {}
    for letter in letters:
        buttons[letter] = Button(root, text=letter)
    return buttons
