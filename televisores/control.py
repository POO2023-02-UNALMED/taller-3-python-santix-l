from televisores.tv import TV

class Control:

    def __init__(self):
        
        self._tv = None

    def canalUp(self):

        self._tv.canalUp()
    
    def canalDown(self):

       self._tv.canalDown()
    
    def volumenUp(self):

        self._tv.volumenUp()
    
    def volumenDown(self):

        self._tv.volumenDown()
    
    def turnOff(self):

        self._tv.turnOff()
    
    def turnOn(self):

        self._tv.turnOn()
    
    def setCanal(self):

        self._tv.setCanal()
    
    def setVolumen(self):

        self._tv.setVolumen()

    def enlazar(self, tv):

        self._tv = tv

        tv.setControl(self)
    
    def setTv(self, t):

        self._tv = t

    def getTv(self):
        
        return self._tv

    