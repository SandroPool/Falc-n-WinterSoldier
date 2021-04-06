import random

class SuperHeroe:
    nombre: str
    ataque: int
    salud: int

    def __init__(self,nombre,ataque,salud,arma):
        self.nombre = nombre
        self.ataque = ataque
        self.salud = salud
        self.arma = arma

        '''funcion acatacar usamos la relacion entre clases,
         Super Heroe y el arma, tipo relacion agregacion
         pasamos como parametro un objeto del mismo tipo
         si el que recibe el daño no tiene el escudo activo
         disminuye el poder del ataque más el del arma
         si este tiene el escudo activo se devuelve su propio
         ataque'''
    def atacar(self, otro):
        escudo_uno = random.choice([True,False])
        escudo_dos = random.choice([True,False])
        
        if escudo_uno:
            otro.salud -= (self.ataque + self.arma.poder) 
            self.arma.resistencia -= 1
        elif escudo_dos:
            self.salud -= (self.ataque + self.arma.poder)
            self.arma.resistencia -= 1
            

    def mejorar_arma(self, nombre=str):
        if self.arma.nombre == nombre:
            self.arma.resistencia += 8
            self.arma.poder += 1

