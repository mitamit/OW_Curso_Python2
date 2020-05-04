def tablas(function):
    def envoltura(tabla=1):
        print('Tabla del %i:' %tabla)
        print('-'*15)
        for numero in range(0,11):
            function(numero, tabla)
        print('-' * 15)
    return envoltura

@tablas
def suma(numero, tabla=1):
    print('%2i + %2i = %3i' %(tabla, numero, tabla+numero))

@tablas
def multiplicar(numero, tabla=1):
    print('%2i + %2i = %3i' %(tabla, numero, tabla*numero))