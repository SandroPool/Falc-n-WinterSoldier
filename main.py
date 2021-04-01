from arma import Arma
from super_heroe import SuperHeroe

if __name__ == '__main__':

    pistola = Arma('Pistola',3,10)
    metralleta = Arma('Metralleta',4,10)

    falcon = SuperHeroe('Sam',5,50,pistola)
    bucky = SuperHeroe('Bucky',6,50,metralleta)

    while 1: 
        print('✓==\U0001F3AE GAME FALCON & WINTER SOLIER \U0001F3AE==✓')

        print('ELIGE TU SUPER HEROE: ')
        print('[1] \U0001F47E FALCON \n[2] \U0001F916 WINTER SOLDIER')

        personaje = int(input(': '))

        if personaje == 1:
            print('BIENVENIDO : {0}'.format(falcon.nombre))
            print('TIENES EL ARMA {0} TIENE {1} BALAS '.format(pistola.nombre,pistola.resistencia))

            while bucky.salud > 0:
                ataques = int(input('CUANTAS VECES QUIERES ATACAR: '))
                for ataque in range(ataques):
                    falcon.atacar(bucky)
                
                print('Tienes vida {0} Te Quedan {1} Balas'.format(falcon.salud,pistola.resistencia))
                print('Vida de {0} es {1} '.format(bucky.nombre,bucky.salud))
                print('✓✓✓======================✓✓✓\n')
            else:
                print('GANASTE {0} FELICIDADES \U0001F64C'.format(falcon.nombre))
                     
        else:
            print('BIENVENIDO : {0}'.format(bucky.nombre))
            print('TIENES EL ARMA {0} TIENE {1} BALAS '.format(metralleta.nombre,metralleta.resistencia))
            
            while falcon.salud > 0:
                ataques = int(input('CUANTAS VECES QUIERES ATACAR: '))
                for ataque in range(ataques):
                    bucky.atacar(falcon)
            
                print('Tienes vida  {0} Te Quedan {1} Balas'.format(bucky.salud,metralleta.resistencia))
                print('Vida de {0} es {1} '.format(falcon.nombre,falcon.salud))
                print('✓✓✓======================✓✓✓\n')
            else:
                print('GANASTE {0} FELICIDADES \U0001F64C'.format(bucky.nombre))
        break
    
