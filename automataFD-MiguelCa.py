import csv
#Miguel Canul Gerardo
"""
El CSV tiene que tener este formato: 

estados,separados,por,comas
alfabeto,separado,por,comas
estado_inicial,estado_aceptacion1,estado_aceptacion2
estado_actual,alfabeto,siguiente_estado
estado_actual,siguiente alfabeto,siguiente_estado
...

"""
"""Deterministics Finite State M (DFSM)"""
class AutomataFD:
     #"""Inicializar el DFSM"""
    def __init__(self):
        self.Q = []
        self.Sigma = []
        self.delta = {}
        self.q0 = None
        self.F = []
        self.EstadoActual = None

    def set_start_accept(self):
        """Pedir al usuario el estado de inicio y el estado final. Validar que estén en Q"""
        while True:
            start = input("Dame el estado inicial del Autómata: ")
            accept = input("Dame el o los estados de aceptación (separados por espacio): ").split()
            # Asegúrate de que los estados proporcionados por el usuario sean válidos
            if start in self.Q and set(accept).issubset(set(self.Q)):
                return start, accept
            else:
                print(f"Por favor, proporciona un estado de inicio y estados finales que deben estar en Q: {self.Q}.")

    def definir_states(self):
        """Pedir al usuario el conjunto de estados Q"""
        Q_in = input("Dame el conjunto de estados, separados por espacios en blanco: ").split()
        print("Estados (Q): {}".format(Q_in))
        return Q_in

    def definir_alfabeto(self):
        """Pedir al usuario el alfabeto (Σ) del autómata"""
        sigma_in = input("Dame el conjunto de símbolos del alfabeto, separados por espacios en blanco: ").split()
        print("Alfabeto (Σ): {}".format(sigma_in))
        return sigma_in

    def definir_transicion(self):
        """Crear la función de transición (δ: Q × Σ → Q) del autómata"""
        trans_dict = {q: {a: "JACHI" for a in self.Sigma} for q in self.Q}
        for key, dic_val in trans_dict.items():
            print(f"Estoy en el estado {key}. Escribe 'JACHI' si no existe el estado de transición.")
            for alfabet_in in dic_val:
                trans_dict[key][alfabet_in] = input(f"Estoy en {key} y veo {alfabet_in}, a qué estado voy: ")
        return trans_dict

    def checar_estado_aceptacion(self):
        """Verifica si el estado actual pertenece a F"""
        return self.EstadoActual in self.F

    def recorrer_automata(self, w):
        """Recorrer el autómata para ver si w lleva a un estado de aceptación"""
        self.EstadoActual = self.q0
        for x in w:
            self.EstadoActual = self.delta.get(self.EstadoActual, {}).get(x, "JACHI")
            if self.EstadoActual == "JACHI":
                return False
        return self.checar_estado_aceptacion()

    def ingresar_automata_manual(self):
        """Inicializar autómata de forma manual"""
        self.Q = self.definir_states()
        self.Sigma = self.definir_alfabeto()
        self.delta = self.definir_transicion()
        self.q0, self.F = self.set_start_accept()

    def leer_automata_csv(self, filename):
        """Leer autómata desde un archivo CSV"""
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                self.Q = next(reader)
                self.Sigma = next(reader)
                self.q0, *self.F = next(reader)
                self.delta = {state: {} for state in self.Q}
                for row in reader:
                    estado_actual, simbolo, siguiente_estado = row
                    self.delta[estado_actual][simbolo] = siguiente_estado
            print("Autómata cargado desde el archivo CSV con éxito.")
        except FileNotFoundError:
            print(f"Archivo {filename} no encontrado.")
        except Exception as e:
            print(f"Error al leer el archivo CSV: {e}")

def menu():
    m = AutomataFD()
    while True:
        print("\n--- Menú ---")
        print("1. Ingresar autómata manualmente")
        print("2. Leer autómata desde archivo CSV. Espeficicar ruta ejemplo:C:/Users/migue/Documents/JS/csv.csv")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            m.ingresar_automata_manual()
            input_w = list(input("Proporcione la cadena w: "))
            print("Cadena aceptada" if m.recorrer_automata(input_w) else "Cadena rechazada")
        elif opcion == "2":
            filename = input("Ingresa el nombre del archivo CSV: ")
            m.leer_automata_csv(filename)
            input_w = list(input("Proporcione la cadena w: "))
            print("Cadena aceptada" if m.recorrer_automata(input_w) else "Cadena rechazada")
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
