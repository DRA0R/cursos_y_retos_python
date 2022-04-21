import math

class Esfera:
    def __init__(self,radio):
        self.radio = radio

    def area(self):
        return (self.radio**2)*math.pi
    
    # def volumen(self):
    #     return (self.radio**3)*math.pi*(3/4) 

class Cilindro(Esfera):
    def __init__(self, radio, altura):
        super().__init__(radio)
        self.altura = altura
    
    def volumen_cilindro(self):
        return cilindro.area()*self.altura

if __name__ == '__main__':
    esfera = Esfera(radio=8)
    print(esfera.area())
    # print(esfera.volumen())

    cilindro = Cilindro(radio =8, altura=4)
    print(cilindro.volumen_cilindro())