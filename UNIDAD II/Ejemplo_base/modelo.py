class Persona:
    def __init__(self, nombre, edad, correo):
        self.nombre=nombre
        self.edad=edad
        self.correo=correo
    def es_mayor_de_edad(self):
        return self.edad>=18
    def __str__(self):
        return f"Nombre: {self.nombre} Edad: {self.edad} Correo: {self.correo}"

class ListaPersonas:
    def __init__(self):
        self.personas=[]
        self.cargar()
    def cargar(self):
        lista=[
            Persona("JOSE",34,"jose.tec@tecazuay.edu.ec"),
            Persona("MARIA",34,"jose.tec@tecazuay.edu.ec"),
            Persona("JUAN",34,"jose.tec@tecazuay.edu.ec")
        ]
        for p in lista:
            self.personas.append(p)

    def agregar(self,nombre, edad, correo):
        persona=Persona(nombre.strip().upper(), edad, correo)
        self.personas.append(persona)
    def buscar(self,nombre):
        for persona in self.personas:
            print(nombre.strip().upper())
            if(persona.nombre==nombre.strip().upper()):
                return persona
    def promedio_Edad(self):
        if len(self.personas)>0:
            suma_edad=0
            for persona in self.personas:
                suma_edad+=persona.edad
            return suma_edad/len(self.personas)
        else:
            return 0
    


