"""VISTA · Caso 29: muestra y pide datos. No decide nada."""


class VistaTours:
    def menu(self):
        print("""
==============================
  TOURS CUENCA COLONIAL
==============================
1. Registrar tour
2. Mostrar tours
3. Reservar cupos
4. Salir""")
        return int(input("Elija una opción: "))

    def pedir_tour(self):
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        cupos = int(input("Cupos: "))
        return nombre, precio, cupos

    def pedir_codigo(self):
        return int(input("Código: "))

    def pedir_cantidad(self):
        return int(input("Cantidad: "))

    def mostrar_tours(self, tours):
        print(f"{'Cód':<6}{'Nombre':<24}{'Precio':<12}{'Cupos':<10}")
        for t in tours:
            print(f"{t.codigo:<6}{t.nombre:<24}{t.precio:<12.2f}{t.cupos:<10}")

    def mensaje(self, texto):
        print(texto)

    def error(self, texto):
        print(f"  Error: {texto}")
