from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont

class SudokuAdministratorDeleteUser(Frame):

    def __init__(self, parent):
        self.parent = parent
        self.delete = Tk()
        super().__init__(self.delete)
        self.pack()
        self.__initUI()
        img = PhotoImage(file="images/pause.png", master=self.delete)
        Button(self.delete, image=img, command=self.goBack, bg="#413c3d").place(x=250, y=480)
        self.master.mainloop()

    def __initUI(self):

        self.delete.title('Crear Usuarios')

        #Tamaño de la ventana
        self.delete.geometry("400x600")
        self.delete.configure(background = "#413c3d")

        #Mantiene la ventana fija para evitar que el diseño se vea afectado
        self.delete.resizable(False, False)

        #estilos para crear labels
        FontStyles = tkFont.Font(family="Lucida Grande", size=208)
        LabelStyles = tkFont.Font(family="Lucida Grande", size=13)

        
        # Muestra el titulo de la seccion
        label1= Label(self.delete, text='Eliminar usuario', font=FontStyles)
        label1.configure(background = "#413c3d", fg="white")
        label1.pack()
        label1.place(x=130,y=100)

        label2= Label(self.delete, text='Introduzca el nombre de usuario a eliminar:', font =LabelStyles)
        label2.configure(background = "#413c3d", fg="#6ea8d9")
        label2.pack()
        label2.place(x=35,y=180)

        
        input_text = StringVar()
        self.userText = ttk.Entry(self.delete, textvariable = input_text)
        self.userText.pack()
        self.userText.place(x=110,y=240, height = 30, width = 200)
        
        Button(self.delete, text = 'Eliminar', command= self.__save, bg="#6ea8d9").place(x=155, y=310, height = 50, width = 110)

    def __save(self):
        print(self.userText.get())

    def goBack(self):
        self.delete.destroy()
        self.parent.deiconify()