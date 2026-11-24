"""MODELO · Caso 29: Tours Cuenca Colonial
Datos (Tour) y reglas (OperadoraTours). No usa print() ni input()."""


class Tour:
    def __init__(self, codigo, nombre, precio, cupos):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cupos = cupos

    def reservar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("la cantidad debe ser mayor que cero.")
        if cantidad > self.cupos:
            raise ValueError(f"solo hay {self.cupos} cupos.")
        self.cupos -= cantidad


class OperadoraTours:
    def __init__(self):
        self.tours = [Tour(1, "Centro histórico", 15.00, 20),
                      Tour(2, "El Cajas", 35.00, 12)]

    def registrar(self, nombre, precio, cupos):
        nuevo = Tour(len(self.tours) + 1, nombre, precio, cupos)
        self.tours.append(nuevo)
        return nuevo

    def buscar(self, codigo):
        for tour in self.tours:
            if tour.codigo == codigo:
                return tour
        raise ValueError("no existe ese código.")

    def reservar(self, codigo, cantidad):
        tour = self.buscar(codigo)
        tour.reservar(cantidad)
        return tour
