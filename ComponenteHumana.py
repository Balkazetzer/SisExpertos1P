class ExpertoHumano:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def dar_conocimiento(self):
        return f"{self.nombre} aporta conocimiento en {self.especialidad}"

class IngenieroConocimiento:
    def __init__(self, nombre):
        self.nombre = nombre

    def traducir_conocimiento(self, conocimiento):
        return f"{self.nombre} traduce el conocimiento: {conocimiento}"

if __name__ == "__main__":
    experto = ExpertoHumano("Dra. Ana", "medicina interna")
    ingeniero = IngenieroConocimiento("Carlos")
    dato = experto.dar_conocimiento()
    print(ingeniero.traducir_conocimiento(dato))
