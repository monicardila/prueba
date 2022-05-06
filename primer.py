class Persona:

    def __init__(self, nombre: str):
        print("hola Mundo")
        self.nombre = nombre

    def __str__(self) -> str:
        pass


def main():
    test = Persona("Monia")


if __name__ == "__main__":
    main()