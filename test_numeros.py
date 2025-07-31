from numeros import Numero

num = Numero(10)

print(f"Original number: {num.numero}")
print(f"Sum: {num.sumar(5)}")
print(f"Subtraction: {num.restar(3)}")
print(f"Division: {num.dividir(5)}")
print(f"Multiplication: {num.multiplicar(2)}")

try:
    num.dividir(0)
except ValueError as e:
    print(f"Error caught: {e}")

num2 = Numero(7)
resultado_suma = num2.sumar(3)
print(f"\nSuma de 7 + 3 = {resultado_suma}")

num3 = Numero(9)
resultado_division = num3.dividir(3)
print(f"División de 9 / 3 = {resultado_division}")