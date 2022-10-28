from tkinter import*
from tkinter import messagebox
from turtle import title
from ventanas import Login,Registro,Container # Importamos la clase Login,Registro y Container
from bdd import Datos
class Manager(Tk):
    def __init__(self,*args,**kwargs):  ## ambos args y kwargs permiten pasar un numero de variables de argumentos a una funcion, como tuplas y como diccionario.
        super().__init__(*args,**kwargs) ## heredamos los args y kwargs.
        self.title("SISTEMA DE VENTAS Y CONTROL DE STOCK")
        self.geometry("1200x900")
        self.menu()
        container=Frame(self)   #Creamos un contenedor dentro de la ventana que creamos antes.
        container.pack(side=TOP,fill=BOTH,expand=True) # Donde aparecerá y que tiene q rellenar.
        container.configure(bg="green")
        self.frames={} #Creamos un Diccionario
        for i in (Login,Registro,Container):
            frame=i(container,self)       # estará dentro del container y dentro de la ventana   
            self.frames[i]=frame 
        self.show_frame(Login)
    def crearBDD(self):
        bdd=Datos()
        try:
            bdd.crear()
        except:
            messagebox.showinfo(title="Información",message="La Base de Datos ya esta creada")
    def menu(self):
        menubar=Menu()
        menudata=Menu(menubar,tearoff=0)
        menudata.add_command(label="Crear/Conectar Base de Datos",command=self.crearBDD)
        menubar.add_cascade(label="Inicio",menu=menudata) # Se mostrará en cascada tipo submenu.
        self.config(menu=menubar)

    def show_frame(self,container): # Recibe la ventana y container
        frame=self.frames[container] # el valor que tiene el diccionario container
        frame.tkraise()               # con el metodo tkraise lo mostramos.             





