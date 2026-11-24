"""
Caso 29: Tours Cuenca Colonial
POO II · Unidad 1 · Ejercicio sencillo: una clase y un menú de 4 opciones · SOLUCIÓN (docente)
"""


class Tour:
    """Representa cada tour del sistema."""

    def __init__(self, codigo, nombre, precio, cupos):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cupos = cupos

    def reservar(self, cantidad):
        if cantidad <= 0:
            print("  Error: la cantidad debe ser mayor que cero.")
            return False
        if cantidad > self.cupos:
            print(f"  Error: solo hay {self.cupos} cupos.")
            return False
        self.cupos -= cantidad
        return True

    def __str__(self):
        return f"{self.codigo:<6}{self.nombre:<24}{self.precio:<12.2f}{self.cupos:<10}"


def buscar(lista, codigo):
    for objeto in lista:
        if objeto.codigo == codigo:
            return objeto
    return None


def main():
    tours = [Tour(1, "Centro histórico", 15.00, 20), Tour(2, "El Cajas", 35.00, 12)]
    opcion = 0
    while opcion != 4:
        print("""
==============================
  TOURS CUENCA COLONIAL
==============================
1. Registrar tour
2. Mostrar tours
3. Reservar cupos
4. Salir""")
        opcion = int(input("Elija una opción: "))
        if opcion == 1:
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cupos = int(input("Cupos: "))
            nuevo = Tour(len(tours) + 1, nombre, precio, cupos)
            tours.append(nuevo)
            print(f"Registrado con el código {nuevo.codigo}.")
        elif opcion == 2:
            print(f"{'Cód':<6}{'Nombre':<24}{'Precio':<12}{'Cupos':<10}")
            for objeto in tours:
                print(objeto)
        elif opcion == 3:
            codigo = int(input("Código: "))
            objeto = buscar(tours, codigo)
            if objeto is None:
                print("  Error: no existe ese código.")
            else:
                cantidad = int(input("Cantidad: "))
                if objeto.reservar(cantidad):
                    print(f"Listo. Quedan {objeto.cupos} cupos.")
        elif opcion == 4:
            print("¡Hasta pronto!")
        else:
            print("Opción no válida: elija del 1 al 4.")


if __name__ == "__main__":
    main()
