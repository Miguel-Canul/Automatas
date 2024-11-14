from antlr4 import *
from javaTraductorLexer import javaTraductorLexer
from javaTraductorParser import javaTraductorParser
from javaTraductorListener import javaTraductorListener
from InJavaTostr import InJavaTostr

def main(): 
    # Solicitar el nombre del archivo de entrada
    in_java_line_ = input('Dame el archivo de entrada: ')

    # Leer el contenido del archivo
    try:
        with open(in_java_line_, 'r') as file:
            file_content = file.read()
    except FileNotFoundError:
        print(f"Error: El archivo {in_java_line_} no se encontró.")
        return

    # Crear el InputStream con el contenido del archivo
    input_stream = InputStream(file_content)
    
    # Crear el lexer
    lexer = javaTraductorLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Crear el parser
    parser = javaTraductorParser(token_stream)
    
    # Generar el árbol de análisis (parse tree)
    tree = parser.file_()

    # Crear un walker y usar el listener para convertir a Java
    walker = ParseTreeWalker()
    listener = InJavaTostr()  # Crea una instancia de tu listener
    walker.walk(listener, tree)

    # Imprimir el código Java generado
    print(listener.java_code)
    
    # Guardar el código generado en el archivo "Operaciones.java"
    java_file_name = 'Operaciones.java'
    try:
        with open(java_file_name, 'w') as java_file:
            java_file.write(listener.java_code)
        print(f"El código Java ha sido guardado en {java_file_name}")
    except IOError:
        print("Error al guardar el archivo .java")

if __name__ == '__main__':
    main()
