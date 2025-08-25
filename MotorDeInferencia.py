class BaseConocimiento:
    def __init__(self):
        self.reglas = {}
        self.datos = {}

    def agregar_regla(self, nombre, regla):
        self.reglas[nombre] = regla

    def agregar_dato(self, nombre, valor):
        self.datos[nombre] = valor

class MotorInferencia:
    def __init__(self, base):
        self.base = base

    def inferir(self):
        if "paciente1_temp" in self.base.datos and self.base.datos["paciente1_temp"] > 38:
            return "El motor de inferencia concluye: posible infección"
        return "No se pudo inferir nada"

if __name__ == "__main__":
    base = BaseConocimiento()
    base.agregar_dato("paciente1_temp", 39)
    base.agregar_regla("fiebre", "Si temperatura > 38 entonces posible infección")
    motor = MotorInferencia(base)
    print(motor.inferir())
