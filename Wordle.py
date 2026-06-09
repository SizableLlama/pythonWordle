from tkinter import *
from alphabetButtons import create_alphabet_buttons
import random
def WordGenerator():
    WordArray=["apple", "beach", "cloud", "dance", "eagle", "flame", "grape", "house", "image", "juice", "koala", "lemon", "music", "night", "ocean", "piano", "queen", "river", "smile", "table", "uncle", "voice", "water", "xenon",
               "yacht", "zebra", "alarm", "bread", "candy", "dream", "earth", "field", "ghost", "heart", "ivory", "jelly", "knife", "light", "mouse", "nurse", "onion", "paper", "quiet", "radio", "stone", "tiger", "under", "vivid",
               "whale", "young"]
    return random.choice(WordArray)


def GuessCheckLen(Guess):
    if len(Guess) != 5:
        print("Invalid guess.")
        return False
    return True


def AppendingArrays(Word,Guess,CorrectArray,WrongPlaceArray,WrongLetterArray):

    for x in range(len(Guess)):
        if Guess[x]==Word[x]:
            CorrectArray[x]=Guess[x]
        elif Guess[x] in Word:
            if Guess[x] not in WrongPlaceArray:
                WrongPlaceArray.append(Guess[x])
        else:
            if Guess[x] not in WrongLetterArray:
                WrongLetterArray.append(Guess[x])
    return CorrectArray,WrongPlaceArray,WrongLetterArray


alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def game(Word):
    Counter=0
    CorrectArray = ["_" for x in range(5)]
    WrongPlaceArray= []
    WrongLetterArray= []

    while Counter < 6:
        Guess=input("Please guess a five letter word.\n:").lower()

        if not GuessCheckLen(Guess):
            continue

        AppendingArrays(Word,Guess,CorrectArray,WrongPlaceArray,WrongLetterArray)
        Counter+=1

        print(f"""Correct letter correct place:\n{CorrectArray}
              \n Correct letter wrong place:\n{WrongPlaceArray} \n
              Wrong letter:\n{WrongLetterArray}""")


        if Guess==Word:
            print(f"You win in {Counter} attempts!")
            return
    if Counter==6:
        print(f"You lose! the word was {Word}.")

def gui():
    #Create root window
    root=Tk()

    #Title and geometry
    root.title("Wordle!")
    root.geometry('500x500')

    #Adding a label to the window
    lbl = Label(root, text = "Type a word! : ")
    lbl.grid()

    #adding Entry Feild
    txt = Entry(root, width=10)
    txt.grid(column =1, row =0)

    #function to display text when button is clicked
    #.def clicked():
    #    lbl.configure(text = "You pushed the button.")

    #function is display user text when button is clicked
    def clicked():
        res = f"You wrote '{txt.get()}'"
        lbl.configure(text = res)

    #button wiget with red colour text inside
    btn = Button(root, text = "Don't click me!", fg = "red", command=clicked)

    #set button grid
    btn.grid(column=2, row=0)



    #Execute
    root.mainloop()

def Wordle():
    root=Tk();

    root.title("Wordle!")
    root.geometry('500x500')

    buttons = create_alphabet_buttons(root)

    rows=['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM']
    for r, row in enumerate(rows):
        for c, letter in enumerate(row):
            buttons[letter].grid(row=r, column=c)





    root.mainloop();


Wordle()
Word=WordGenerator()
game(Word)

