class Gato:
    #_nombre="Mishi"

    #constructor
    def __init__(self, nombre, color, edad):
        self._nombre = nombre
        self._color = color
        self._edad = edad

    #met get y set
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getColor(self):
        return self._color

    def setColor(self, color):
        self._color = color

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

