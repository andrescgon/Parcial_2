import sys
from antlr4 import *
from output.RationalExprLexer import RationalExprLexer
from output.RationalExprParser import RationalExprParser
from output.RationalExprListener import RationalExprListener

# Clase para implementar el Listener y realizar las operaciones con fracciones
class EvalListener(RationalExprListener):

    def __init__(self):
        self.stack = []

    # Método para sumar fracciones
    def add_fractions(self, num1, den1, num2, den2):
        if den1 == den2:  # Si los denominadores son iguales
            numerator = num1 + num2
            denominator = den1
        else:  # Si los denominadores son diferentes, se encuentra el denominador común
            numerator = (num1 * den2) + (num2 * den1)
            denominator = den1 * den2
        return numerator, denominator

    # Método para restar fracciones
    def subtract_fractions(self, num1, den1, num2, den2):
        if den1 == den2:  # Si los denominadores son iguales
            numerator = num1 - num2
            denominator = den1
        else:  # Si los denominadores son diferentes, se encuentra el denominador común
            numerator = (num1 * den2) - (num2 * den1)
            denominator = den1 * den2
        return numerator, denominator

    # Método para multiplicar fracciones
    def multiply_fractions(self, num1, den1, num2, den2):
        numerator = num1 * num2
        denominator = den1 * den2
        return numerator, denominator

    # Método para dividir fracciones
    def divide_fractions(self, num1, den1, num2, den2):
        numerator = num1 * den2
        denominator = den1 * num2
        return numerator, denominator

    # Cuando se llega a una operación de suma o resta
    def exitExpr(self, ctx):
        if ctx.getChildCount() == 3:  # expr op term
            right = self.stack.pop()
            left = self.stack.pop()
            op = ctx.getChild(1).getText()
            if op == '+':
                result = self.add_fractions(left[0], left[1], right[0], right[1])
                self.stack.append(result)
            elif op == '-':
                result = self.subtract_fractions(left[0], left[1], right[0], right[1])
                self.stack.append(result)
        else:
            # Solo hay un term (sin operadores), lo pasamos directo
            self.stack.append(self.stack.pop())

    # Cuando se llega a una operación de multiplicación o división
    def exitTerm(self, ctx):
        if ctx.getChildCount() == 3:  # term op factor
            right = self.stack.pop()
            left = self.stack.pop()
            op = ctx.getChild(1).getText()
            if op == '*':
                result = self.multiply_fractions(left[0], left[1], right[0], right[1])
                self.stack.append(result)
            elif op == '/':
                result = self.divide_fractions(left[0], left[1], right[0], right[1])
                self.stack.append(result)
        else:
            # Solo hay un factor (sin operadores), lo pasamos directo
            self.stack.append(self.stack.pop())

    # Cuando se llega a una fracción o entero
    def exitFactor(self, ctx):
        if ctx.FRACTION():
            fraction = ctx.FRACTION().getText()
            num, den = map(int, fraction.split('/'))
            self.stack.append((num, den))  # Guardar como una tupla (numerador, denominador)
        elif ctx.INT():
            self.stack.append((int(ctx.INT().getText()), 1))  # Guardar como (número, 1)

# Función para formatear la fracción
def format_fraction(fraction):
    return f"{fraction[0]}/{fraction[1]}"  # Mostrar siempre como num/den

# Función principal para ejecutar el intérprete
def main():
    input_stream = InputStream(input('Ingresa una expresión racional: '))
    
    lexer = RationalExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = RationalExprParser(token_stream)
    
    tree = parser.prog()  # Iniciar el parsing con la regla prog
    
    listener = EvalListener()
    walker = ParseTreeWalker()  # Creación del walker para recorrer el árbol
    walker.walk(listener, tree)  # Recorrer el árbol con el Listener

    result = listener.stack.pop()  # El resultado estará en la pila

    # Mostrar el resultado como fracción
    print(f'Resultado: {format_fraction(result)}')

if __name__ == '__main__':
    main()
