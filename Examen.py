"""Canul Gerardo Miguel Antonio"""
import csv

class AutomataFD:
    def __init__(self):
        self.Q = []
        self.Sigma = []
        self.delta = {}
        self.q0 = None
        self.F = []
        self.EstadoActual = None

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

    def leer_automata_csv(self, filename):
        """Leer autómata desde un archivo CSV"""
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                
                # Leer las primeras líneas del CSV
                self.Q = next(reader)
                self.Sigma = next(reader)
                
                # Leer estado inicial y hasta 4 estados de aceptación
                estados_inicio_aceptacion = next(reader)
                self.q0 = estados_inicio_aceptacion[0]
                self.F = estados_inicio_aceptacion[1:]
                
                # Validar que los estados de aceptación no excedan 4 y estén en Q
                if len(self.F) > 4:
                    raise ValueError("El archivo CSV contiene más de 4 estados de aceptación.")
                if not set(self.F).issubset(set(self.Q)):
                    raise ValueError("Uno o más estados de aceptación no están definidos en Q.")
                
                # Crear la función de transición
                self.delta = {state: {} for state in self.Q}
                for row in reader:
                    estado_actual, simbolo, siguiente_estado = row
                    self.delta[estado_actual][simbolo] = siguiente_estado
                
                print("Autómata cargado desde el archivo CSV con éxito.")
        except FileNotFoundError:
            print(f"Archivo {filename} no encontrado.")
            raise
        except ValueError as e:
            print(f"Error en el archivo CSV: {e}")
            raise
        except Exception as e:
            print(f"Error al leer el archivo CSV: {e}")
            raise

def main():
    m = AutomataFD()
    # Archivo CSV por defecto
    default_csv = "examen.csv"  # Cambia esto por la ruta de tu archivo CSV
    try:
        m.leer_automata_csv(default_csv)
        
        while True:
            # Solicitar la cadena de entrada `w`
            input_w = list(input("\nProporcione la cadena w: "))
            # Verificar si la cadena es aceptada o no
            if m.recorrer_automata(input_w):
                print("Cadena aceptada")
            else:
                print("Cadena rechazada")
            
            # Preguntar si se desea ingresar otra cadena
            otra = input("\n¿Desea ingresar otra cadena? (s/n): ").strip().lower()
            if otra != 's':
                print("Finalizando el programa.")
                break
    except Exception:
        print("No se pudo procesar el autómata. Verifica el archivo CSV.")

if __name__ == "__main__":
    main()
