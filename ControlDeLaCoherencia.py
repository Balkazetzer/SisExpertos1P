class BaseConocimiento:
    def __init__(self):
        self.reglas = {}

    def agregar_regla(self, nombre, regla):
        self.reglas[nombre] = regla

class ControlCoherencia:
    def __init__(self, base):
        self.base = base

    def verificar(self, nombre, nueva_regla):
        if nombre in self.base.reglas and self.base.reglas[nombre] != nueva_regla:
            return f"Inconsistencia detectada con la regla {nombre}"
        else:
            self.base.agregar_regla(nombre, nueva_regla)
            return "Regla coherente, agregada con éxito"

if __name__ == "__main__":
    base = BaseConocimiento()
    control = ControlCoherencia(base)
    print(control.verificar("dolor", "Si dolor cabeza → migraña"))
    print(control.verificar("dolor", "Si dolor cabeza → resfriado"))
