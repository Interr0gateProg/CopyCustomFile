from tkinter.filedialog import *
from quitter import Quitter
from ClassVisitor import CopyCustomFile
from tkinter.simpledialog import *

class Main(Frame):
    def __init__(self, parent=None, **opt):
        Frame.__init__(self, parent, **opt)
        self.pack()
        self.ButtonTo = Button(self, text='Write toDir', command=self.toDirf)
        self.ButtonFrom = Button(self, text='Write fromDir', command=self.fromDirf)
        self.ButtonEnds = Button(self, text='White endswith', command=self.ends)
        self.ButtonStart = Button(self, text='Start', command=self.start)
        self.ButtonTo.pack(side=TOP)
        self.ButtonFrom.pack(side=TOP)
        self.ButtonEnds.pack(side=TOP)
        self.ButtonStart.pack(side=TOP)
        Quitter(self).pack(side=TOP)
    def fromDirf(self):
        self.fromDir = askdirectory()
        if self.fromDir: self.ButtonFrom.config(text='Ok')
    def toDirf(self):
        self.toDir = askdirectory()
        if self.toDir: self.ButtonTo.config(text='Ok')
    def ends(self):
        self.endswith = askstring('Endswith','What endswith do you want? (It must be like .py')
        self.ButtonEnds.config(text='Ok')
    def start(self):
        Copy = CopyCustomFile(self.fromDir, self.toDir, self.endswith)
        Copy.run()

M = Main()
M.mainloop()