class BaseConocimiento:
    def __init__(self):
        self.datos = {}

    def agregar_dato(self, nombre, valor):
        self.datos[nombre] = valor

class MotorInferencia:
    def __init__(self, base):
        self.base = base

    def inferir(self):
        if "paciente1_temp" in self.base.datos and self.base.datos["paciente1_temp"] > 38:
            return "El motor de inferencia concluye: posible infección"
        return "No se pudo inferir nada"

class SubsistemaColaborador:
    def __init__(self, base):
        self.base = base

    def solicitar_info(self, dato, valor):
        self.base.agregar_dato(dato, valor)
        return f"Dato agregado: {dato} = {valor}"

if __name__ == "__main__":
    base = BaseConocimiento()
    motor = MotorInferencia(base)
    subsistema = SubsistemaColaborador(base)
    print(motor.inferir())
    print(subsistema.solicitar_info("paciente1_temp", 39))
    print(motor.inferir())
