''' PIEDRA, PAPEL O TIJERA (1 JUGADOR CONTRA LA MAQUINA, COMANDO DE VOZ)'''

import random
import speech_recognition as sr

r = sr.Recognizer()
jugando = True

class PiedraPapelTijera:
    
    def __init__(self,jugador1,jugador2,puntos):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.score1 = 0  #cantidad de puntos jugador 1
        self.score2 = 0  #cantidad de puntos jugador 2
        self.puntos = puntos  #cantidad de puntos a los que se juega
        self.tablero = '                 <== vs ==>                 '
        print('\n'*7,self.tablero,'\n'*5,'Empieza el Piedra, Papel o Tijera')
        
    def jugada1(self): 
        # comando de voz hecho con chat gpt
       with sr.Microphone() as source:
           print("Grita PIEDRA, PAPEL O TIJERA")  
           r.adjust_for_ambient_noise(source, duration=1) 
           audio = r.listen(source,timeout=7,phrase_time_limit=3)

       try:
           self.mano1 = r.recognize_google(audio, language='es-ES')
           self.mano1 = self.mano1.upper()
       except sr.UnknownValueError:
           print("No se entendio que dijiste",'\n'*5)
           iniciar.jugada1()
       except sr.RequestError as e:
           print("No se ha podido conectar con el servicio de reconocimiento de voz de Google; {0}".format(e))
           jugando = False
           return jugando 
       if self.mano1== 'piedra' or self.mano1 == 'papel' or self.mano1 == 'tijera':
           return self.mano1
    
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
          
       
iniciar = PiedraPapelTijera(input('Nombre del jugador 1: '),'Maquina',3)

while jugando == True:
    print('\n'*5,f'Turno de {iniciar.jugador1}','\n'*12)
    iniciar.jugada1()
    print('\n'*12)
    iniciar.jugada2(random.choice(['piedra','papel','tijera']))
    iniciar.ganador()
    if iniciar.score1 == iniciar.puntos:
        print('\n'*10, f'Gano {iniciar.jugador1} con {iniciar.puntos} puntos','\n'*10)
        jugando = False
    elif iniciar.score2 == iniciar.puntos:
        print('\n'*10, f'{iniciar.jugador2} gano el juego con {iniciar.puntos} puntos','\n'*10)
        jugando = False
    