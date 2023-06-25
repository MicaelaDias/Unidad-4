class NumeroComplejo:
    def __init__(self, real=0, imaginario=0):
        self.real=real
        self.imaginario = imaginario

    
    def __str__(self):
        s=''
        if self.real != 0 and self.imaginario != 0:
            if self.imaginario >= 0:
                s = f"{self.real} + {self.imaginario}i"
            else:
                s = f"{self.real} - {abs(self.imaginario)}i"
        elif self.real != 0:
            s = str(self.real)
        elif self.imaginario != 0:
            s = f"{self.imaginario}i"
        else:
            s = "0"
        return s
    def getReal(self):
        return self.real
    def getImaginario(self):
        return self.imaginario
    
    def __add__(self, otro):
        real = self.real + otro.real
        imaginario = self.imaginario + otro.imaginario
        return NumeroComplejo(real, imaginario)
    
    
    def __sub__(self, otro):
        real = self.real - otro.real
        imaginario = self.imaginario - otro.imaginario
        return NumeroComplejo(real, imaginario)
    
    def __mul__(self, otro):
        real = (self.real * otro.real) - (self.imaginario * otro.imaginario)
        imaginario = (self.real * otro.imaginario) + (self.imaginario * otro.real)
        return NumeroComplejo(real, imaginario)
    
    def __truediv__(self, otro):
        denominador = otro.real ** 2 + otro.imaginario ** 2
        real = (self.real * otro.real + self.imaginario * otro.imaginario) / denominador
        imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / denominador
        return NumeroComplejo(real, imaginario)
