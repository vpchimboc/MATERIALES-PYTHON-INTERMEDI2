#Crear una clase
class Libro:
    pass

libro1=Libro()
print(type(libro1))
#Crear el contructor de la clase
class Libro:
    
    def __init__(self, nombre, autor,estado,listaLibros):
        self.nombre=nombre
        self.autor=autor
        self.estado=estado
        self.listalibros=listaLibros
    def mostrar(self):
        print("Nombre del libro: ",self.nombre, " Autor: ", self.autor)
    def cambiar_estado(self,estado1):
        self.estado=estado1
    def mostrarlista(self):
        for e in self.listalibros:
            print(e)
    def __str__(self):
        return f"nombre:{self.nombre}, autor: {self.autor}, estado: {self.estado} "
libro2=Libro("Python intermedio", "Sandoval","Disponible", ["Python basico", "Python Intermedio"])
libro2.mostrar()
print(libro2)
libro2.cambiar_estado("Prestado")
print(libro2)
print(libro2.nombre)
libro2.mostrarlista()


