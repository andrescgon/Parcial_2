import sys
from antlr4 import *
from LaplaceLexer import LaplaceLexer
from LaplaceParser import LaplaceParser
from antlr4.tree.Tree import ParseTreeWalker, ParseTreeListener

class LaplaceTransformListener(ParseTreeListener):
    def enterExpression(self, ctx):
        # Comprobamos si la entrada es una integral
        if ctx.integral():
            self.enterIntegral(ctx.integral())
        else:
            # Si no es una integral, puede ser una función simple
            function_name = ctx.function().getText()
            result = self.calculate_laplace_transform(function_name)
            print(f"Transformada de Laplace de {function_name}: {result}")

    def enterIntegral(self, ctx):
        function_name = ctx.function().getText()  # Nombre de la función
        result = self.calculate_laplace_transform(function_name)
        print(f"Transformada de Laplace de la integral de {function_name}: {result}")

    def calculate_laplace_transform(self, function_name):
        # Lógica para calcular transformadas de Laplace
        if function_name == 'f':
            return "1/s"  # Transformada de f(t) = 1
        elif function_name == 't':
            return "1/s^2"  # Transformada de f(t) = t
        elif function_name == 't^2':
            return "2/s^3"  # Transformada de f(t) = t^2
        elif function_name.startswith('e'):
            k = function_name[2:]  # Extraer k de e^(kt)
            return f"1/(s - {k})"  # Transformada de f(t) = e^(kt)
        elif function_name == 'sin':
            return "1/(s^2 + 1)"  # Transformada de f(t) = sin(t)
        elif function_name == 'cos':
            return "s/(s^2 + 1)"  # Transformada de f(t) = cos(t)
        elif function_name == 'heaviside':
            return "1/s"  # Transformada de f(t) = u(t)
        elif function_name == 'delta':
            return "1"  # Transformada de f(t) = δ(t)
        
        return "Función no soportada"

def main():
    input_stream = InputStream(input("Ingrese la función para la que desea calcular la transformada de Laplace: "))
    lexer = LaplaceLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LaplaceParser(stream)
    
    tree = parser.expression()  # Parsear la expresión
    listener = LaplaceTransformListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == "__main__":
    main()

