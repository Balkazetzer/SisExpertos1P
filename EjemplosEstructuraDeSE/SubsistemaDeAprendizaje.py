class Aprendizaje:
    def __init__(self):
        self.reglas = {}

    def aprender_estructura(self, nombre, regla):
        self.reglas[nombre] = regla
        return f"Se aprendió nueva regla: {nombre}"

    def aprender_parametro(self, nombre, frecuencia):
        self.reglas[nombre] = f"Probabilidad estimada: {frecuencia}"
        return f"Se actualizó probabilidad de {nombre}"

if __name__ == "__main__":
    aprendiz = Aprendizaje()
    print(aprendiz.aprender_estructura("tos", "Si tos y fiebre → gripe"))
    print(aprendiz.aprender_parametro("gripe", "70%"))
