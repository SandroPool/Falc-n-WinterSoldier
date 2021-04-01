class SuperHeroe:
    nombre: str
    ataque: int
    salud: int

    def __init__(self,nombre,ataque,salud,arma):
        self.nombre = nombre
        self.ataque = ataque
        self.salud = salud
        self.arma = arma

    def atacar(self, otro):
        otro.salud -= (self.ataque + self.arma.poder) 
        self.arma.resistencia -= 1

    def mejorar_arma(self, nombre=str):
        if self.arma.nombre == nombre:
            self.arma.resistencia += 2
            self.arma.poder += 2

            
