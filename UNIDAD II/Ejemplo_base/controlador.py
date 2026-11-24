class ControladorPersonas:
    def __init__(self, modelo, vista):
        self.modelo=modelo
        self.vista=vista
    def ejecutar(self):
        opcion=""
        while opcion!="4":
            opcion=self.vista.menu()
            if opcion=="1":
                nombre, edad, correo= self.vista.pedir_datos()
                persona=self.modelo.agregar(nombre,edad,correo)
                self.vista.mensaje("Persona registrada")
            elif opcion=="2":
                self.vista.mostrar_personas(self.modelo.personas)
            elif opcion=="3":
                persona=self.modelo.buscar(self.vista.pedir_nombre())
                print(persona)
            elif opcion=="4":
                self.vista.mensaje("Hasta pronto")


        