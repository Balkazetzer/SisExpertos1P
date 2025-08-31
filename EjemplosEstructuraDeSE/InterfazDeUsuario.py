class InterfazUsuario:
    def mostrar_resultado(self, resultado):
        print("Resultado del sistema experto:", resultado)

    def solicitar_dato(self):
        return input("Ingrese la temperatura del paciente: ")

if __name__ == "__main__":
    interfaz = InterfazUsuario()
    dato = interfaz.solicitar_dato()
    interfaz.mostrar_resultado(f"Temperatura registrada: {dato}")
