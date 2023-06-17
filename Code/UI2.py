from tkinter import *
import UI1
import Generator
import pygame


def sound():
    pygame.mixer.music.load("Code/Bad_Snacks.mp3")
    pygame.mixer.music.play(loops=0)


def History():
    wind = Tk()
    wind.config(background="white")
    wind.title('History output')
    showcase = Canvas(wind, bg="gray16", height=200, width=200)
    try:
        f1 = open('Assets/History.txt', 'r')
        text1 = f1.readlines()
        f1.close()
    except:
        Label(wind, text="File missing")
    Placeholder = Text(wind, width=50, height=7,
                       wrap=WORD, background='white')
    Placeholder.grid(row=2, column=2)
    Placeholder.delete(0.0, END)
    Placeholder.insert(END, text1)
    showcase.mainloop()


class Interface2:

    def __init__(self):
        pygame.mixer.init()
        sound()
        open('Assets/History.txt', 'w').close()
        self.attempts = 0
        self.AT_Input = []
        Generator.generate_number()
        self.T = Generator.Number
        self.window = Tk()
        self.window.geometry("590x590")
        self.c = Canvas(self.window, bg="gray16", height=200, width=200)
        self.window.title("Vache-Taureau")
        self.filename = PhotoImage(file="Assets/aa.gif")
        self.bg_label = Label(self.window, image=self.filename)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.c.pack()
        self.HISTORY_button = Button(self.window, text="History", width=6, height=1,
                                     command=History, fg="black", font=('Raleway', 14), bg='grey', borderwidth=4)
        self.HISTORY_button.pack(pady=5)

        self.l2 = Label(self.window, text="Enter your guess:", bg='snow3', fg="black",
                        font=('Raleway', 15), borderwidth=1, relief="sunken")
        self.l2.pack(pady=5)
        self.nb1 = Entry(self.window, width=10,
                         font=('Raleway', 15), borderwidth=5, bg='snow3', border=3)
        self.nb1.pack(pady=5)
# 8888888888888888888888
        self.submit_button = Button(self.window, text="submit", width=6, height=1,
                                    command=self.click, fg="black", font=('Raleway', 14), bg='grey',  borderwidth=4)
        self.submit_button.pack(pady=5)
        self.text = StringVar()
        self.text.set("you have 10 attempts ")
        self.l3 = Label(self.window, textvariable=self.text, bg='snow3', fg="black",
                        font=('Raleway', 15), borderwidth=1, relief="sunken")
        self.l3.pack(pady=5)
        # cows

        self.text1 = StringVar()
        self.text1.set("0 cows ")
        self.l3 = Label(self.window, textvariable=self.text1, bg='snow3', fg="black",
                        font=('Raleway', 15), borderwidth=1, relief="sunken")
        self.l3.pack(pady=5)

        # bulls

        self.text2 = StringVar()
        self.text2.set("0 bulls ")
        self.l3 = Label(self.window, textvariable=self.text2, bg='snow3', fg="black",
                        font=('Raleway', 15), borderwidth=1, relief="sunken")
        self.l3.pack(pady=5)

        self.back_button = Button(self.window, text="back", width=6, height=1,
                                  command=self.back, fg="black", font=('Raleway', 14), bg='grey',  borderwidth=4)
        self.back_button.pack(pady=5)

        self.quit_botton = Button(self.window, text="Quit", width=6, height=1,
                                  command=self.close_window, fg="black", font=('Raleway', 14), bg='grey',  borderwidth=4)
        self.quit_botton.pack(pady=5)
        self.window.mainloop()

    def back(self):
        open('Assets/History.txt', 'w').close()
        self.window.destroy()
        UI1.Interface1()
        Generator.Number.clear()
        exit()

    def close_window(self):
        open('Assets/History.txt', 'w').close()
        self.window.destroy()
        exit()

    def click(self):

        self.attempts += 1
        entered_text1 = self.nb1.get()

        bulls = 0
        cows = 0

        for j in range(4):
            for k in range(4):
                if(int(entered_text1[j]) == self.T[k]):
                    cows += 1
        for x in range(4):
            if int(entered_text1[x]) == self.T[x]:
                bulls += 1
        cows = cows-bulls

        vc = str(cows)+"cows"
        vb = str(bulls)+"bulls"
        self.AT_Input.append((entered_text1, vb, vc))
        self.nb1.delete(0, 'end')
        fichier = open('Assets/History.txt', 'a')
        fichier.write(str(self.AT_Input[self.attempts-1]))

        fichier.close()

        if bulls == 4:
            self.text.set(
                "you have won after {} attempts ".format(self.attempts))
            self.submit_button.pack_forget()
            self.T.clear()
            Generator.Number.clear()

        elif self.attempts >= 10:
            self.text.set("you have lost")
            self.submit_button.pack_forget()
            self.T.clear()
            Generator.Number.clear()

        else:

            self.text1.set(vc)
            self.text2.set(vb)
            va = "you have "+str(10-self.attempts)+" attempts"
            self.text.set(va)
