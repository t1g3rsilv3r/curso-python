class Numero:
    def _init_(self, numero: int):
        self.numero = numero

    def evaluar_numero(self):
        if self.numero % 2 == 0:
            print("El número es par")
        else:
            print("El número es impar")

        if self.numero == 7:
            print("El número ingresado es un comodin")

        if self.numero == 10:
            print("Tu número es diez")

    def sumar(self, numero_a: int) -> None:
        resultado = self.numero + numero_a
        print(f"La suma es: {resultado}")

