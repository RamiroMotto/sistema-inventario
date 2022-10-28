import sqlite3
from tkinter import *
from tkinter import ttk,messagebox   # ttk para Treeview, muestran una colección en árbol de elementos. Cada elemento tiene una etiqueta textual, una imagen opcional y una lista opcional de valores de datos.
from bdd import Datos
class Login(Frame): # Clase login recibe Frame.
    def __init__(self,padre,controlador): #inicializa sus atributos
        super().__init__(padre) # Aca hereda padre.
        self.pack() # empaquetamos.
        self.place(x=0,y=0,width=1100,height=700) #su ubicación.
        self.controlador=controlador 
        self.widgets() # Inicializa los widgets. 
    def botones(self,x,y,text,bcolor,fcolor,cmd):
        def on_enter(e): # funciones para el puntero del mouse.
            btn["background"]=bcolor 
            btn["foreground"]=fcolor
        def on_leave(e): 
            btn["background"]=fcolor # Se invierte el resutaldo.
            btn["foreground"]=bcolor
        btn=Button(self,
        text=text,
        fg=bcolor,
        bg=fcolor,
        border=1,
        activeforeground=fcolor,
        activebackground=bcolor,
        command=cmd,)
        btn.bind("<Enter>",on_enter) # capturas el evento al hacer enter
        btn.bind("<Leave>",on_leave) 
        btn.place(x=x,y=y,width=120)
    def validacion(self,user,pas):
        return len(user)>0 and len(pas)>0
    def login(self): # Este login esta dentro del frame y nos enviará a control 1.
        with sqlite3.connect("bdd.db") as conn:
            cursor=conn.cursor() # Con esto recuperamos los datos que estamos ingresando 
            user=self.username.get()
            pas=self.password.get()
            if self.validacion(user,pas):
                consulta="SELECT * FROM usuarios WHERE nombre=? AND contraseña=?"
                parametros=(user,pas)
                try:
                    cursor.execute(consulta,parametros)
                    if cursor.fetchall():  # Si me retornas algo entonces envio self.control
                        self.control1()
                    else:
                        self.username.delete(0,END)#caso contrario, no hay nombre de user, o contraseña incorrecta limpia los campos.
                        self.password.delete(0,END) # Eliminamos o limpiamos los entry.
                        messagebox.showerror(title="Error",message="Usuario y/o Contraseña Incorrecta")
                except:
                    messagebox.showerror(title="Error",message="No se conecto a la BASE DE DATOS") 

            else:
                messagebox.showerror(title="Error",message="Llena todas los campos")

            cursor.close() # Una vez que sucede lo anterior se cierra la BDD.
    def control1(self):
        self.controlador.show_frame(Container)

    def control2(self): # control2 nos va a retornar a registro.
        self.controlador.show_frame(Registro) 
    def widgets(self):  # el widget estará dentro del frame
        fondo=Frame(self,bg="cyan") # tendrá otro frame dentro del frame.
        fondo.pack() # empaquetamos para que aparezca ese frame.
        fondo.place(x=0,y=0,width=1200,height=900)
        self.username=Entry(fondo,font="arial 16") # Creamos la variable para username con fuente arial.
        self.username.place(x=540,y=400,width=240,height=40)
        self.password=Entry(fondo,show="*",font="16") # El password se mostrará con ***
        self.password.place(x=540,y=460,width=240,height=40)
        btn=self.botones(540,520,"INICIAR","blue","white",cmd=self.login)        #hacemos el llamado del boton.
       # btn1=Button(fondo,bg="blue",fg="white",text="INICIAR",command=self.login) # Boton de inicio que estará en el fondo
        #btn1.place(x=540,y=520) # No hace falta empaquetar.
        btn1=self.botones(660,520,"REGISTRAR","blue","white",cmd=self.control2)
        #bt2=Button(fondo,bg="blue",fg="white",text="REGISTRAR",command=self.control2)
        #bt2.place(x=620,y=520)    




    
class Registro(Frame): # Esta clase tmb recibirá un Frame.
    def __init__(self,padre,controlador): # Inicializamos atributos.
        super().__init__(padre) # Heredamos al padre.
        self.pack() # Empaquetamos
        self.place(x=0,y=0,width=1200,height=900) 
        self.controlador=controlador # Heredamos o recibimos el parametro controlador.
        self.widgets() # Inicializamos widgets.
    def botones(self,x,y,text,bcolor,fcolor,cmd):
        def on_enter(e): # funciones para el puntero del mouse.
            btn["background"]=bcolor 
            btn["foreground"]=fcolor
        def on_leave(e): 
            btn["background"]=fcolor # Se invierte el resutaldo.
            btn["foreground"]=bcolor
        btn=Button(self,
        text=text,
        fg=bcolor,
        bg=fcolor,
        border=1,
        activeforeground=fcolor,
        activebackground=bcolor,
        command=cmd,)
        btn.bind("<Enter>",on_enter) # capturas el evento al hacer enter
        btn.bind("<Leave>",on_leave) 
        btn.place(x=x,y=y,width=120) # le damos ubiación.

    def validacion(self,user,pas):
        return len(user)>0 and len(pas)>0

    def eje_consulta(self,consulta,parametros=()):
        db=Datos() # Creamos un objeto para Datos.
        db.consultas(consulta,parametros) #funcion consulta o metodo consultas


    def registro(self):
        user=self.username.get()
        pas=self.password.get()
        if self.validacion(user,pas):
            if len(pas)<6:
                messagebox.showinfo(title="Error",message="La Contraseña debe ser mayor a 6 digitos")
                self.username.delete(0,END)                    #caso contrario, no hay nombre de user, o contraseña incorrecta limpia los campos.
                self.password.delete(0,END)
            else:
                consulta="INSERT INTO usuarios VALUES(?,?,?)"
                parametros=(None,user,pas)
                self.eje_consulta(consulta,parametros)    
                self.control1() # Una vez que realice la consulta la enviará al container 1
        else:
            messagebox.showerror(title="Error",message="LLene sus Datos")        

    def control1(self):
        self.controlador.show_frame(Container)
    def control2(self):
        self.controlador.show_frame(Login)  # un controlador que llama a la clase login
    def widgets(self): # Creamos iconos.
        fondo=Frame(self,bg="cyan") # tendrá otro frame dentro del frame.
        fondo.pack() # empaquetamos para que aparezca ese frame.
        fondo.place(x=0,y=0,width=1200,height=900)
        user=Label(fondo,text="Nombre de usuario",font="Arial 16",bg="cyan") # cyan no crea la linea blanca del fondo.
        user.place(x=580,y=320)
        self.username=Entry(fondo,font="Arial 16") # Creamos la variable para username con fuente arial 16
        self.username.place(x=580,y=360,width=240,height=40)
        pas=Label(fondo,text="Contraseña",font="Arial 16",bg="cyan")
        pas.place(x=580,y=410)
        self.password=Entry(fondo,show="*",font="16") # El password se mostrará con *** con tamaño 16
        self.password.place(x=580,y=450,width=240,height=40)
        btn1=self.botones(580,540,"REGRESAR","blue","white",cmd=self.control2)
        btn=self.botones(700,540,"REGISTRAR","blue","white",cmd=self.registro)
        #bt2=Button(fondo,bg="blue",fg="white",text="REGISTRAR",command=self.registro)
        #bt2.place(x=605,y=540)
    
    
class Container(Frame): # Lo mismo que todo, tendrá un frame
    def __init__(self,padre,controlador):  # Atributos.
        super().__init__(padre) # Hereda padre
        self.controlador=controlador # Inicializamos controlador
        self.pack()
        self.place(x=0,y=0,width=1200,height=900)
        self.widgets() # Llamamos, iniciamos los widgets.
        self.frames={} # Agregamos Diccionario para el frames.
        for i in (Ventas,Compras): # Iteramos Ventras y Compras.
            frame=i(self)
            self.frames[i]=frame 
            frame.pack()
            frame.config(bg="orange")
            frame.place(x=0,y=40,width=1200,height=900)
        self.show_frames(Ventas)  # LLamamos a la funcion show_frames, nos loggueamos y primero nos manda a ventas.
    def show_frames(self,container):
        frame=self.frames[container]
        frame.tkraise() # Mostramos el frame a traves de tkraise.
    def ventas(self):
        self.show_frames(Ventas)
    def compras(self):
        self.show_frames(Compras)

    def widgets(self): # Widgets estará dentro del Frame.
        venta=Button(self,text="Ventas",command=self.ventas)
        venta.pack()
        venta.place(x=0,y=0,width=300,height=40)
        compras=Button(self,text="Compras",command=self.compras)
        compras.pack()
        compras.place(x=300,y=0,width=300,height=40)

class Ventas(Frame):
    def __init__(self,padre):
        super().__init__(padre)
        self.widgets()
    def widgets(self):
        ventas=Label(self,text="Ventas")
        ventas.pack()
        ventas.place(x=558,y=450)

class Compras(Frame):
    def __init__(self,padre):
        super().__init__(padre)
        self.widgets()
    def widgets(self):
        compra=Label(self,text="Compras")
        compra.pack()
        compra.place(x=558,y=450)


        










