class EjecutorAcciones:
    def ejecutar(self, conclusion):
        if "infección" in conclusion:
            return "Acción: recetar antibióticos"
        else:
            return "Acción: observación y reposo"

if __name__ == "__main__":
    ejecutor = EjecutorAcciones()
    print(ejecutor.ejecutar("posible infección detectada"))
