class Marca:

    def __init__(self, nombre):
        
        self._nombre = nombre
    
    def setNombre(self, nom):

        self._nombre= nom

    def getNombre(self):
        
        return self._nombre