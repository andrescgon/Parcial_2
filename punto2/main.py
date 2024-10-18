import antlr4
from antlr4 import InputStream, CommonTokenStream
from MapFunctionLexer import MapFunctionLexer
from MapFunctionParser import MapFunctionParser

def main():
    input_str = input("Ingrese una expresión en el formato MAP(funcion, iterable): ")
    
    input_stream = InputStream(input_str)
    lexer = MapFunctionLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MapFunctionParser(token_stream)
    
    tree = parser.expr()

    # Extraer el nombre de la función o expresión lambda
    function_node = tree.mapFunction().functionCall()
    
    if function_node.lambdaExpr():
        # Extraer la expresión lambda
        param = function_node.lambdaExpr().IDENTIFIER().getText()
        operation = function_node.lambdaExpr().exprBody().getText()
        func = eval(f"lambda {param}: {operation}")
    else:
        # Extraer una función estándar
        function_name = function_node.IDENTIFIER().getText()
        func = eval(function_name)
    
    # Obtener y evaluar el iterable
    iterable_expr = tree.mapFunction().iterable().getText()
    try:
        iterable = eval(iterable_expr)
    except Exception as e:
        print(f"Error al evaluar el iterable: {e}")
        return

    # Aplicar la función utilizando map()
    try:
        result = list(map(func, iterable))
    except Exception as e:
        print(f"Error al aplicar la función: {e}")
        return
    
    print('Iterable',iterable,'Resultado',result)

if __name__ == '__main__':
    main()

