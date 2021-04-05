from tkinter import *
from tkinter import messagebox
from core.SudokuAdministratorBinnacle import *
from core.SudokuUserAdministration import *
from core.ScreenCenter import ScreenCenter
from core.SudokuGame import SudokuGame
from core.SudokuBoardUI import SudokuBoardUI
from core.DialogClose import DialogClose

"""
Frame que permite visualizar las opciones de un usuario que tiene como
rol administrador.
@author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
@version 1.0
"""
class SudokuAdministratorUI(Frame):

    """
    Constructor de la clase.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __init__(self):
        self.parent = Tk()
        self.parent.protocol("WM_DELETE_WINDOW", self.__onClosing)
        super().__init__(self.parent)
        self.pack()
        self.__initUI()
        self.master.mainloop()

    """
    Creación de los widgets.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
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

    """
    Función que abre una nueva ventada en donde se pueden administrar los
    usuarios registrados en el juego y la BD.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __goUserAdministration(self):
        self.parent.withdraw()
        SudokuUserAdministration(parent=self.parent)

    """
    Función que abre una nueva ventada para visualizar la bitacora.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __goBinnacle(self):
        self.parent.withdraw()
        SudokuAdministratorBinnacle(parent=self.parent)

    """
    Función que le permite al administrador jugar.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __goGame(self):
        with open('core/sudoku/n00b.sudoku', 'r') as boardFile:
            self.parent.destroy()
            root = Tk()
            game = SudokuGame(boardFile)
            game.start()
            SudokuBoardUI(root, game)

    """
    Función que permite minimizar o salir del juego.
    @author Daniel Arteaga, Kenneth Cruz, Gabriela Hernández, Luis Morales
    @version 1.0
    """
    def __onClosing(self):
        self.dialogClose = DialogClose(self.parent)
        self.parent.wait_window(self.dialogClose)