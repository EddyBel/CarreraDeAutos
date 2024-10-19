from random import randint
from time import sleep
import os
from math import floor

class Carrera:

    def __init__(self, competidores: int = 5, meta: int = 150, time: float = .05, useName: bool = False):
        self.carrito = [
            ".-'--`-._",
            "'-O---O--'"
        ]
        self.competidores = competidores
        self.meta = meta
        self.time = time
        self.useName = useName
        self.competidores = max(2, self.competidores)
        self.avance_count = [0] * self.competidores
        self.nombres = []
        self.longitud_carrito = max(len(line) for line in self.carrito) - 1

    def nombresCarritos(self):
        if self.useName:
            for i in range(self.competidores):
                nombre = input(f"Ingrese el nombre para el carrito {i + 1}: ")
                self.nombres.append(nombre)
        else:
            self.nombres = [f"Carrito {i + 1}" for i in range(self.competidores)]

    def moverCursorAlInicio(self):
        print("\033[H", end='')

    def mostrarGanador(self, winner: str, padding: int = 8):
        sizeString = len(winner)
        paddingLeftAndRight = floor(padding / 2)
        totalWidth = sizeString + padding + 2
        print(totalWidth * "◼")
        print(f"◼{' ' * paddingLeftAndRight}{winner}{' ' * (padding - paddingLeftAndRight)}◼")
        print(totalWidth * "◼")

    def main(self):
        self.nombresCarritos()
        os.system("cls" if os.name == "nt" else "clear")
        print("-" * self.meta + "|")

        while True:
            for i in range(self.competidores):
                avance = randint(0, 2)
                self.avance_count[i] += avance

            self.moverCursorAlInicio()
            print("-" * self.meta + "|")

            for i in range(self.competidores):
                print(f"{self.nombres[i]} ({self.avance_count[i]}km)" + " " * (self.longitud_carrito - len(self.nombres[i])))
                for line in self.carrito:
                    print((" " * self.avance_count[i]) + line)
                print("-" * self.meta + "|")

            sleep(self.time)

            ganador = -1
            for i in range(self.competidores):
                if self.avance_count[i] >= self.meta - self.longitud_carrito:
                    if ganador == -1:
                        ganador = i
                    self.mostrarGanador(self.nombres[ganador])
                    break
            else:
                continue
            break

        positions = [(self.avance_count[j], j) for j in range(self.competidores)]
        positions.sort(reverse=True, key=lambda x: x[0])

        print("\nRanking final:")
        for index, (avance, competidor) in enumerate(positions, start=1):
            print(f"{index} :: {self.nombres[competidor]} con avance de {avance}km")

class Juego:

    def __init__(self):
        self.opciones = ["Iniciar carrera rápida", "Iniciar carrera con nombres", "Salir"]
        self.opcion_actual = 0

    def mostrarMenu(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("\n--- Menú Principal ---")
        for i, opcion in enumerate(self.opciones):
            print(f"{i + 1}. {opcion}")

    def seleccionarOpcion(self):
        opcion = input("Selecciona una opción: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= len(self.opciones):
                self.opcion_actual = opcion - 1
                return True
            else:
                print("Opción no válida.")
                return False
        else:
            print("Opción no válida.")
            return False

    def ejecutarOpcion(self):
        if self.opcion_actual == 0:  # Carrera rápida (sin nombres personalizados)
            carrera = Carrera(useName=False)
            carrera.main()
            input("Presione Enter para continuar...")
        elif self.opcion_actual == 1:  # Carrera con nombres personalizados
            carrera = Carrera(useName=True)
            carrera.main()
            input("Presione Enter para continuar...")
        elif self.opcion_actual == 2:  # Salir
            print("¡Gracias por jugar!")
            exit()

    def main(self):
        while True:
            self.mostrarMenu()
            if self.seleccionarOpcion():
                self.ejecutarOpcion()

if __name__ == "__main__":
    juego = Juego()
    juego.main()

