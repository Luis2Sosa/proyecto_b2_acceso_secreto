# Proyecto bonus #2 - Sistema de acceso directo
# Autor: Luis Sosa

def verificar_codigo(codigo_correcto):
    def acceso_sistema(funcion):
        def decorador():
            codigo = input("Introduzca el código secreto:\n")
            if codigo != "luis123":
                print("Codigo incorrecto. Acceso denegado.")
                exit()
            funcion()
        return decorador
    return acceso_sistema

@verificar_codigo("verificando")
def acceder():
    print("Acceso consedido al sistema ultra secreto...")

# Ejecutamos la funcion protegida
acceder()