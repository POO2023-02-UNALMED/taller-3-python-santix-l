class TV:

    _numTV = 0

    def __init__(self, marca, estado):
        
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control = None

        TV._numTV += 1

    
    def setMarca(self, mar):

        self._marca = mar

    def getMarca(self):
        
        return self._marca
    

    
    def setPrecio(self, pre):

        self._precio = pre

    def getPrecio(self):
        
        return self._precio
    
    
    def setControl(self, con):

        self._control = con

    def getControl(self):
        
        return self._control
    

    def setCanal(self, can):

        if self._estado and can >= 1 and can <= 120:

            self._canal = can
    
    def getCanal(self):

        return self._canal
    

    
    def setVolumen(self, vol):

        if self._estado and vol >= 0 and vol <= 7:

            self._volumen = vol

    def getVolumen(self):

        return self._volumen
    
    
    @classmethod
    def setNumTV(cls, num):

        TV._numTV = num
    
    @classmethod
    def getNumTV(cls):

        return TV._numTV
    
    
    def getEstado(self):

        return self._estado
    

    def turnOff(self):

        self._estado = False
    
    def turnOn(self):

        self._estado = True
    


    def canalUp(self):

        if self._estado and self._canal >= 1 and self._canal < 120:

            self._canal += 1
    
    def canalDown(self):

       if self._estado and self._canal > 1 and self._canal <= 120:

            self._canal -= 1
    
    def volumenUp(self):

        if self._estado and self._volumen >= 0 and self._volumen < 7:

            self._volumen += 1
    
    def volumenDown(self):

        if self._estado and self._volumen > 0 and self._volumen <= 7:

            self._volumen -= 1
    
    
    
