import sys
import math
from antlr4 import *
from LaplaceTransformLexer import LaplaceTransformLexer
from LaplaceTransformParser import LaplaceTransformParser

class CustomListener(ParseTreeListener):
    def __init__(self):
        self.variables = {}  # Diccionario para almacenar variables

    def enterStatement(self, ctx):
        # Aquí puedes definir lo que se debe hacer al entrar a una declaración.
        pass

    def exitStatement(self, ctx):
        expression = ctx.expression().getText()
        result = self.evaluate_expression(expression)
        print(f"Transformada de Laplace de '{expression}' es {result}")

    def evaluate_expression(self, expression):
        try:
            # Reemplazar las funciones por sus equivalentes en Python
            expression = expression.replace("sin", "math.sin")
            expression = expression.replace("cos", "math.cos")
            expression = expression.replace("tan", "math.tan")
            expression = expression.replace("exp", "math.exp")
            expression = expression.replace("log", "math.log")
            expression = expression.replace("sqrt", "math.sqrt")
            
            # Evaluar las variables en el contexto
            for var in self.variables:
                exec(f"{var} = {self.variables[var]}")
            
            # Evalúa la expresión usando eval()
            return eval(expression)
        except NameError as e:
            print(f"Error: variable no definida: {e}")
            return None
        except Exception as e:
            print(f"Error al evaluar la expresión '{expression}': {e}")
            return None

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = LaplaceTransformLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LaplaceTransformParser(stream)
    
    # Llamada al punto de entrada
    tree = parser.prog()
    
    listener = CustomListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Por favor, proporciona el archivo de entrada.")
        sys.exit(1)
    
    main(sys.argv)

