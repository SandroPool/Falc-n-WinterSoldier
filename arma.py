class Arma:
    nombre: str
    poder: int
    resistencia: int

    def __init__(self,nombre,poder,resistencia,categoria=1):
        self.nombre = nombre
        self.poder = poder
        self.resistencia = resistencia
        self.categoria = categoria
        
