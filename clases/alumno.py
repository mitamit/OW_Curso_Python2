class Alumno():
    contador = 0

    def __init__(self, nombre = ""):
        self.nombre = nombre  #propiedad de objeto
        Alumno.contador += 1  #propiedad de clase
        self.__secreto = 'dsksl'

  

    