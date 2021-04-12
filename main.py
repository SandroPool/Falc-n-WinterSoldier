from arma import Arma
from super_heroe import SuperHeroe

if __name__ == '__main__':

    '''Primer el jugador seleciona el personje con el 
    quiere atacar y luego que inicie la batalla.
    El juego termina cuando la vida de uno de los 
    dos sea menor a 0 si la resistencia es menor 
    a 1 el jugador tendra la opción de                
    recargar mas escribiendo el número 1 '''

    jugando = input('Iniciar Juego (s/n) ').lower()
    
    while jugando == 's':
        pistola = Arma('Pistola',2,8)
        metralleta = Arma('Metralleta',2,10)

        falcon = SuperHeroe('Samuel Wilson',2,50,pistola)
        bucky = SuperHeroe('Bucky Barnes',3,50,metralleta)
         
    
        print('✓==\U0001F3AE GAME FALCON & WINTER SOLIER \U0001F3AE==✓')

        print('ELIGE TU SUPER HEROE: ')
        print('[1] \U0001F47E FALCON \n[2] \U0001F916 WINTER SOLDIER')

        personaje = int(input(': '))

        if personaje == 1:
            print('BIENVENIDO : {0}'.format(falcon.nombre))
            print('TIENES EL ARMA {0} TIENE {1} BALAS '.format(pistola.nombre,pistola.resistencia))
                
            while bucky.salud > 0 and falcon.salud > 0:
                if pistola.resistencia > 0:
                    ataques = int(input('CUANTAS VECES QUIERES ATACAR: '))
                    for ataque in range(ataques):
                        falcon.atacar(bucky)
                
                    print('{0} tu vida es {1} \U00002764 y tienes {2} balas'.format(falcon.nombre,falcon.salud,pistola.resistencia))
                    print('{0} tu vida es {1} \U00002764'.format(bucky.nombre,bucky.salud))
                    print('====================== \U0001F525 \U0001F525 \n')
                    
                else:
                    uno = int(input('No tienes balas escribe "1" para recargar: '))
                    if uno == 1:
                        falcon.mejorar_arma(pistola.nombre)
                        print('Ahora tienes {0} de balas y {1} de poder \n'.format(pistola.resistencia,pistola.poder))        
            else:
                print('\U0001F64C GANASTE  FELICIDADES \U0001F64C')
                     
        else:
            print('BIENVENIDO : {0}'.format(bucky.nombre))
            print('TIENES EL ARMA {0} TIENE {1} BALAS '.format(metralleta.nombre,metralleta.resistencia))
            
            while falcon.salud > 0 and bucky.salud > 0:
                if metralleta.resistencia > 0:
                    ataques = int(input('CUANTAS VECES QUIERES ATACAR: '))
                    for ataque in range(ataques):
                        bucky.atacar(falcon)
                        
                    print('{0} tu vida es {1} \U00002764 y tienes {2} balas'.format(bucky.nombre,bucky.salud,metralleta.resistencia))
                    print('{0} tu vida es {1} \U00002764'.format(falcon.nombre,falcon.salud))
                    print('====================== \U0001F525 \U0001F525  \n')
                else:
                    uno = int(input('No tienes balas escribe "1" para recargar: '))
                    if uno == 1:
                        bucky.mejorar_arma(metralleta.nombre)
                        print('Ahora tienes {0} de balas y {1} de poder '.format(metralleta.resistencia,metralleta.poder))
                        
            else:
                print('\U0001F64C GANASTE FELICIDADES \U0001F64C')

        jugando = input('Continuar Juego (s/n) ').lower()
    



