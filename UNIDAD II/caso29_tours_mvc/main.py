"""Caso 29: Tours Cuenca Colonial · versión MVC
POO II · 2.1 Modelo – Vista – Controlador"""
from modelo import OperadoraTours
from vista import VistaTours
from controlador import ControladorTours

if __name__ == "__main__":
    ControladorTours(OperadoraTours(), VistaTours()).ejecutar()
