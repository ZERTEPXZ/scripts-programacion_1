import abc

class Menu(abc.ABC):
    def __init__(self, titulo):
        self.titulo = titulo
        self.opciones = {}

    def agregar_opcion(self, opcion, funcion):
        self.opciones[opcion] = funcion

    def mostrar_menu(self):
        print(self.titulo)
        for opcion, funcion in self.opciones.items():
            print(f"{opcion}. {funcion.__name__.replace('_', ' ').capitalize()}")

    def obtener_seleccion(self):
        while True:
            try:
                seleccion = int(input("Seleccione una opcion: "))
                if seleccion in self.opciones:
                    return seleccion
                else:
                    print("Opción inválida. Intente de nuevo.")
            except ValueError:
                print("Entrada inválida. Intente de nuevo.")

    def ejecutar_seleccion(self, seleccion):
        funcion = self.opciones[seleccion]
        funcion()

    @abc.abstractmethod
    def ejecutar_opcion_abstracta(self):
        pass

class MenuPrincipal(Menu):
    def __init__(self, titulo):
        super().__init__(titulo)

    def ejecutar_opcion_abstracta(self):
        print("Ejecutando la opción abstracta en MenuPrincipal...")

def opcion_uno():
    print("Ejecutando la opción 1...")

def opcion_dos():
    print("Ejecutando la opción 2...")

def opcion_tres():
    print("Ejecutando la opción 3...")

def salir():
    print("Saliendo del programa...")
    exit()

if __name__ == "__main__":
    menu = MenuPrincipal("Menu Principal")
    menu.agregar_opcion(1, opcion_uno)
    menu.agregar_opcion(2, opcion_dos)
    menu.agregar_opcion(3, opcion_tres)
    menu.agregar_opcion(4, salir)

    while True:
        menu.mostrar_menu()
        seleccion = menu.obtener_seleccion()
        menu.ejecutar_seleccion(seleccion)
        menu.ejecutar_opcion_abstracta()