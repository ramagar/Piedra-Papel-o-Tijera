''' PIEDRA, PAPEL O TIJERA (2 JUGADORES)'''

class PiedraPapelTijera:
    
    def __init__(self,jugador1,jugador2,puntos):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.score1 = 0  #cantidad de puntos jugador 1
        self.score2 = 0  #cantidad de puntos jugador 2
        self.puntos = puntos  #cantidad de puntos a los que se juega
        self.tablero = '                 <== vs ==>                 '
        print('\n'*7,self.tablero,'\n'*5,'Empieza el Piedra, Papel o Tijera')
        
    def jugada1(self,mano1): 
       self.mano1 = mano1.upper()
       if self.mano1== 'PIEDRA' or self.mano1== 'PAPEL' or self.mano1== 'TIJERA':
           pass
       else:
           print('\n'*20,'Escribiste algo mal pelotudo, intenta de nuevo: ','\n'*25)
           iniciar.jugada1(input('Escribi Piedra, Papel o Tijeras: '))
       
    def jugada2(self,mano2):
        self.mano2 = mano2.upper()
        if self.mano2== 'PIEDRA' or self.mano2== 'PAPEL' or self.mano2== 'TIJERA':
            print('\n'*8,f'({self.jugador1})                                             ({self.jugador2})','\n'*4,
                  f'{self.mano1}                 <== vs ==>                 {self.mano2}','\n'*5)
        else:
            print('\n'*20,'Escribiste algo mal pelotudo, intenta de nuevo: ','\n'*25)
            iniciar.jugada2(input('Escribi Piedra, Papel o Tijeras: '))                                                                              
        
        
    def ganador(self):
        if self.mano1 == 'PIEDRA' and self.mano2 == 'TIJERA':
            self.score1 += 1
            print(f'{self.jugador1} Gano 1 punto, tiene un total de {self.score1} puntos','\n'*3,
                  f'{self.jugador2} tiene un total de {self.score2} puntos','\n'*5)
        elif self.mano2 == 'PIEDRA' and self.mano1 == 'TIJERA':
            self.score2 += 1
            print(f'{self.jugador2} Gano 1 punto, tiene un total de {self.score2} puntos','\n'*3,
                  f'{self.jugador1} tiene un total de {self.score1} puntos','\n'*5)
        elif self.mano1 == 'PAPEL' and self.mano2 == 'PIEDRA':
            self.score1 += 1
            print(f'{self.jugador1} Gano 1 punto, tiene un total de {self.score1} puntos','\n'*3,
                  f'{self.jugador2} tiene un total de {self.score2} puntos','\n'*5)
        elif self.mano2 == 'PAPEL' and self.mano1 == 'PIEDRA':
            self.score2 += 1
            print(f'{self.jugador2} Gano 1 punto, tiene un total de {self.score2} puntos','\n'*3,
                  f'{self.jugador1} tiene un total de {self.score1} puntos','\n'*5)
        elif self.mano1 == 'TIJERA' and self.mano2 == 'PAPEL':
            self.score1 += 1
            print(f'{self.jugador1} Gano 1 punto, tiene un total de {self.score1} puntos','\n'*3,
                  f'{self.jugador2} tiene un total de {self.score2} puntos','\n'*5)
        elif self.mano2 == 'TIJERA' and self.mano1 == 'PAPEL':
            self.score2 += 1
            print(f'{self.jugador2} Gano 1 punto, tiene un total de {self.score2} puntos','\n'*3,
                  f'{self.jugador1} tiene un total de {self.score1} puntos','\n'*5)
        else:
            print('Empate, nadie suma puntos','\n'*3,
                  f'{self.jugador1} tiene un total de {self.score1} puntos',
                  '\n'*3,f'{self.jugador2} tiene un total de {self.score2} puntos','\n'*5)
          
       
iniciar = PiedraPapelTijera(input('Nombre del jugador 1: '),input('Nombre del jugador 2: '),5)

while True:
    print('\n'*5,f'Turno de {iniciar.jugador1}','\n'*12)
    iniciar.jugada1(input('Escribi Piedra, Papel o Tijeras: '))
    print('\n'*40,f'Turno de {iniciar.jugador2}','\n'*12)
    iniciar.jugada2(input('Escribi Piedra, Papel o Tijeras: '))
    iniciar.ganador()
    if iniciar.score1 == iniciar.puntos:
        print('\n'*10, f'Gano {iniciar.jugador1} con {iniciar.puntos} puntos','\n'*10)
        break
    elif iniciar.score2 == iniciar.puntos:
        print('\n'*10, f'{iniciar.jugador2} gano el juego con {iniciar.puntos} puntos','\n'*10)
        break
    
    
    
    
    
    