class Explicacion:
    def __init__(self):
        self.historial = []

    def registrar(self, conclusion, razon):
        self.historial.append((conclusion, razon))

    def explicar(self):
        for c, r in self.historial:
            print(f"Conclusión: {c} | Razón: {r}")

if __name__ == "__main__":
    exp = Explicacion()
    exp.registrar("posible infección", "Temperatura > 38°C")
    exp.registrar("reposo recomendado", "Síntomas leves")
    exp.explicar()
