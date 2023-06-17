from tkinter import *
from threading import *
import UI2
import pygame

new_ui = any
# functions----------------------------------------------


def sound():
    pygame.mixer.music.load("Code/Bad_Snacks.mp3")
    pygame.mixer.music.play(loops=-1)


def rules():
    wind = Tk()
    wind.title("Rules of the game")
    wind.geometry("350x350")

    try:
        f1 = open('Assets/rules.txt', 'r')
        text1 = f1.read()
        f1.close()
    except:
        Label(wind, text="File missing")
    Placeholder = Text(wind, width=350, height=590,
                       wrap=WORD, background='white')
    Placeholder.grid(row=2, column=2)
    Placeholder.delete(0.0, END)
    Placeholder.insert(END, text1)

    wind.mainloop()


class Interface1:
    # init---------------------------------------------------

    def __init__(self):
        pygame.mixer.init()
        sound()
        self.window = Tk()
        self.window.title('Vache-Taureau')
# background--------------------------------------------
        self.window.geometry("590x590")
        self.c = Canvas(self.window, bg="gray16", height=200, width=200)
        self.filename = PhotoImage(file="Assets/aa.gif")
        self.bg_label = Label(self.window, image=self.filename)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.c.pack()
        self.START_BUTTON = Button(self.window, text="Play Game", width=10, height=2,
                                   command=self.play, font=('Raleway', 18), bg='grey', fg='black', borderwidth=10)
        self.START_BUTTON.pack(pady=20)
        self.RULES_BUTTON = Button(self.window, text="How to Play", width=10, height=2, font=('Raleway', 18),
                                   command=rules, bg='grey', fg='black', borderwidth=10)
        self.RULES_BUTTON.pack(pady=10)

        self.window.mainloop()

    def play(self):
        global new_ui
        self.window.destroy()
        new_ui = UI2.Interface2()
        exit()
# Buttons----------------------------------------------
