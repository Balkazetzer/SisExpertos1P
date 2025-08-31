class BaseConocimiento:
    def __init__(self):
        self.reglas = {}

    def agregar_regla(self, nombre, regla):
        self.reglas[nombre] = regla

class AdquisicionConocimiento:
    def __init__(self, base):
        self.base = base

    def incorporar(self, nombre, regla):
        if nombre not in self.base.reglas:
            self.base.agregar_regla(nombre, regla)
            return f"Conocimiento nuevo agregado: {nombre}"
        else:
            return f"El conocimiento {nombre} ya existe"

if __name__ == "__main__":
    base = BaseConocimiento()
    subsistema = AdquisicionConocimiento(base)
    print(subsistema.incorporar("tos", "Si hay tos y fiebre → posible gripe"))
    print(subsistema.incorporar("tos", "Si hay tos persistente → posible bronquitis"))
