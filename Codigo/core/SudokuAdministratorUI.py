"""
    @author: gehernandezc@unah.hn
    @version: 1.0
    @date 2021/04/03
"""
from tkinter import *
from tkinter import messagebox
from core.SudokuAdministratorBinnacle import *
from core.SudokuUserAdministration import *
from core.ScreenCenter import ScreenCenter
from core.SudokuGame import SudokuGame
from core.SudokuBoardUI import SudokuBoardUI
from core.Close import DialogClose


class SudokuAdministratorUI(Frame):

    def __init__(self):
        self.parent = Tk()
        self.parent.protocol("WM_DELETE_WINDOW", self.__onClosing)
        super().__init__(self.parent)
        self.pack()
        self.__initUI()
        self.master.mainloop()

    def __initUI(self):
        self.icon = PhotoImage(file="core/images/SudokuLogo.png", master=self.parent)
        self.brand = PhotoImage(file="core/images/Brand.png", master=self.parent)
        self.width = 400
        self.height = 600
        self.parent.title('Opciones Administrador')
        self.parent.iconphoto(True, self.icon)

        self.parent.geometry("%dx%d" % (self.width, self.height))
        self.parent.configure(background = "#171717")
        self.parent.resizable(False, False)

        TitleStyles = tkFont.Font(family="Lato", size=25, weight='bold')
        ButtonStyles = tkFont.Font(family="Lato", size=17)

        self.center = ScreenCenter()
        self.center.center(self.parent, self.width, self.height)

        label1= Label(self.parent, text='¿Qué deseas hacer?', font=TitleStyles)
        label1.configure(background = "#171717", fg="white")
        label1.pack()
        label1.place(x=60,y=120)

        Button(self.parent, text = 'Administración usuarios', bg="#6ea8d9", font=ButtonStyles, command= self.__goUserAdministration).place(x=50, y=220, height = 50, width = 310)
        Button(self.parent, text = 'Ir al juego', bg="#6ea8d9", font=ButtonStyles, command= self.__goGame).place(x=50, y=280, height = 50, width =310)
        Button(self.parent, text = 'Bitácora', bg="#6ea8d9", font=ButtonStyles, command= self.__goBinnacle).place(x=50, y=340, height = 50, width =310)
        Button(self.parent, text = 'Salir', bg="#6ea8d9", font=ButtonStyles, command= self.__onClosing).place(x=50, y=400, height = 50, width =310)
        
        label2 = Label(self.parent, image=self.brand, borderwidth=0)
        label2.pack()
        label2.place(x=8,y=555)

    def __goUserAdministration(self):
        self.parent.withdraw()
        SudokuUserAdministration(parent=self.parent)

    def __goBinnacle(self):
        self.parent.withdraw()
        SudokuAdministratorBinnacle(parent=self.parent)

    def __goGame(self):
        with open('core/sudoku/n00b.sudoku', 'r') as boardFile:
            self.parent.destroy()
            root = Tk()
            game = SudokuGame(boardFile)
            game.start()
            SudokuBoardUI(root, game)

    def __onClosing(self):
        d = DialogClose(self.parent)
        self.parent.wait_window(d.top)