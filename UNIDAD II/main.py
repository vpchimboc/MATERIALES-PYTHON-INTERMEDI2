from modelo import ListaPersonas
from vista import VistaPersonas
from controlador import ControladorPersonas

modelo=ListaPersonas()
vista=VistaPersonas()
controlador=ControladorPersonas(modelo,vista)
controlador.ejecutar()

