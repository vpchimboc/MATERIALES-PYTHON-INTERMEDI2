"""CONTROLADOR · Caso 29: une la vista con el modelo."""


class ControladorTours:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        opcion = 0
        while opcion != 4:
            opcion = self.vista.menu()
            try:
                if opcion == 1:
                    self.registrar()
                elif opcion == 2:
                    self.vista.mostrar_tours(self.modelo.tours)
                elif opcion == 3:
                    self.reservar()
                elif opcion == 4:
                    self.vista.mensaje("¡Hasta pronto!")
                else:
                    self.vista.mensaje("Opción no válida: elija del 1 al 4.")
            except ValueError as e:
                self.vista.error(e)

    def registrar(self):
        nombre, precio, cupos = self.vista.pedir_tour()          # 1. pedir a la vista
        nuevo = self.modelo.registrar(nombre, precio, cupos)     # 2. llamar al modelo
        self.vista.mensaje(f"Registrado con el código {nuevo.codigo}.")  # 3. mostrar

    def reservar(self):
        codigo = self.vista.pedir_codigo()
        tour = self.modelo.buscar(codigo)                 # si no existe, error antes de pedir la cantidad
        cantidad = self.vista.pedir_cantidad()
        self.modelo.reservar(tour.codigo, cantidad)
        self.vista.mensaje(f"Listo. Quedan {tour.cupos} cupos.")
