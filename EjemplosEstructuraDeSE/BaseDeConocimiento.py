class BaseConocimiento:
    def __init__(self):
        self.reglas = {}
        self.datos = {}

    def agregar_regla(self, nombre, regla):
        self.reglas[nombre] = regla

    def agregar_dato(self, nombre, valor):
        self.datos[nombre] = valor

    def mostrar(self):
        return {"Reglas": self.reglas, "Datos": self.datos}

if __name__ == "__main__":
    base = BaseConocimiento()
    base.agregar_regla("fiebre", "Si temperatura > 38 entonces posible infección")
    base.agregar_dato("paciente1_temp", 39)
    print(base.mostrar())
