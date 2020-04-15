from tkinter import *
from tkinter.messagebox import *

class Quitter(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        time = Button(self, text='Quit', command=self.quit)
        time.pack(side=TOP)
    def quit(self):
        ans = askokcancel('Verify quit', 'Do you really want to quit?')
        if ans: Frame.quit()