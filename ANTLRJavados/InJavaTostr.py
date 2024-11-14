from javaTraductorParser import *
from javaTraductorListener import javaTraductorListener

class InJavaTostr(javaTraductorListener):
    def __init__(self):
        self.java_code = "public class Operaciones {\n"  # Código Java inicial con la clase
        self.indent_level = 1  # Nivel de indentación inicial para la clase
        self.current_function = ""  # Para almacenar el código de la función actual
        self.function_name = ""  # Para almacenar el nombre de la función actual
        self.arguments = "" #Para almacenar los arguments
    def get_indent(self):
        return "    " * self.indent_level  # Retorna la indentación actual

    # Enter a parse tree produced by javaTraductorParser#funcDef.
    def enterFuncDef(self, ctx: javaTraductorParser.FuncDefContext):
        self.function_name = ctx.funcName().getText()  # Guarda el nombre de la función
        params = ctx.parameters().getText() if ctx.parameters() else ""

        # Aquí se modifican los parámetros agregando el tipo int
        if params:
            params = ', '.join([f"int {param}" for param in params.split(',')])  # Agrega "int" a cada parámetro

        self.current_function += f"{self.get_indent()}public static int {self.function_name}({params}) {{\n"
        self.indent_level += 1  # Aumenta la indentación para el cuerpo de la función
    
    # Exit a parse tree produced by javaTraductorParser#funcDef.
    def exitFuncDef(self, ctx: javaTraductorParser.FuncDefContext):
        self.indent_level -= 1
        self.current_function += f"{self.get_indent()}}}\n\n"  # Cierra la función
        self.java_code += self.current_function
        self.current_function = ""  # Resetea el código de la función actual

    # Enter a parse tree produced by javaTraductorParser#assignStmt.
    def enterAssignStmt(self, ctx: javaTraductorParser.AssignStmtContext):
        var_name = ctx.varName().getText()
        expr = ctx.expr().getText()
        self.current_function += f"{self.get_indent()}int {var_name} = {expr};\n"

    # Exit a parse tree produced by javaTraductorParser#returnStmt.
    def exitReturnStmt(self, ctx: javaTraductorParser.ReturnStmtContext):
        expr = ctx.expr().getText()
        self.current_function += f"{self.get_indent()}return {expr};\n"
# Enter a parse tree produced by javaTraductorParser#arguments.
    def enterArguments(self, ctx: javaTraductorParser.ArgumentsContext):
    # Captura todos los argumentos
        arguments = [arg.getText() for arg in ctx.expr()]
        self.arguments = ", ".join(arguments)  # Guarda los argumentos como texto

    


    # Exit a parse tree produced by javaTraductorParser#file.
    def exitFile(self, ctx: javaTraductorParser.FileContext):
        # Agrega el método main de Java
        self.java_code += (
            f"{self.get_indent()}public static void main(String[] args) {{\n"
            f"{self.get_indent()}    int resultado = {self.function_name}({self.arguments});\n"
            f"{self.get_indent()}    System.out.println(resultado);\n"
            f"{self.get_indent()}}}\n"
        )
        self.java_code += "}\n"  # Cierra la clase Operaciones

# Función para obtener el código Java generado
def get_java_code():
    listener = InJavaTostr()
    return listener.java_code
