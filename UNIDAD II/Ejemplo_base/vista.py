class VistaPersonas:
    def menu(self):
        print("####REGISTRO DE PERSONAS###")
        print("1. Agregar persona")
        print("2. Mostrar personas")
        print("3. Buscar personas")
        print("4. Salir")
        opcion=input("Ingrese una opción")
        return opcion
    def pedir_datos(self):
        nombre=input("Ingrese nombre")
        try:
            edad=int(input("Ingrese edad"))
        except ValueError:
            raise ValueError("La edad debe de ser numero enter")
        correo=input("Ingrese correo")
        return nombre, edad, correo
    def pedir_nombre(self):
        nombre=input("Ingrese nombre a buscar: ")
        return nombre
    def mensaje(self,mensaje):
        print(mensaje)
    def mostrar_personas(self,personas):
            for persona in personas:
                 print(persona)
    