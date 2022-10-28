import sqlite3
class Datos:
    def __init__(self,*args,**kwargs): # Inicializamos parametros
        super().__init__(*args,**kwargs) # Los heredamos.
        self.nombre="bdd.db"
    def crear(self):
        conn=sqlite3.connect(self.nombre)
        cursor=conn.cursor()
        cursor.execute("""CREATE TABLE usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(50),
            contraseña VARCHAR(50)
        )""")
    def consultas(self,consulta,parametros=()): # función consultas que recibirá consultas mediante tuplas
        conn=sqlite3.connect(self.nombre)
        cursor=conn.cursor()
        result=cursor.execute(consulta,parametros) # se guardan aca los resultados de la consulta
        conn.commit()
        return result #que retorne lo que encuentre.




    