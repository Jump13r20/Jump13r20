class Vehiculo():
    
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        
    def __str__(self):
        return 'color {}, {} ruedas, {} puertas'.format( self.color, self.ruedas, self.puertas )
        
        
class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return Vehiculo.__str__(self) + ', {} km/h, {} cc'.format(self.velocidad, self.cilindrada)
        
        
c = Coche("azul", 4, 5, 120, 1200)
print(c)