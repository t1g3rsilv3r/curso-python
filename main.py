
def saludar(nombre):
    print(f"Hola, {nombre}!")
    print("¿Cómo estás?")
    return nombre

def main():
    nombre = input("ingrese un nombre: ")  
    nombresaludado = saludar(nombre)
    print(f"Tu nombre es: {nombresaludado}")

if __name__ == "__main__":
    main()  
