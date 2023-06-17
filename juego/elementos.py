import pygame
import random
import time
from variables import *

def resetear(selector,tabla):
    validar=False     
    contador=25
    x_meta=900
    meta_bandera=0
    segundos=75.0
    score=1000000.0
    enemigo=Enemigo(selector.numero)
    enemigo.usado.append(selector.valor)
    player = Jugador(selector.valor) 
    tabla.sprite=player.player
    # tabla.sprite=pygame.transform.scale(tabla.sprite, (40, 40))
    stop_tiempo=False
    return validar,contador,x_meta,meta_bandera,segundos,score,enemigo,player,stop_tiempo
    
def cambiarMusica(cancion):
    pygame.mixer.music.stop() 
    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play(loops=-1)

def dibujarHitbox(screen,rect):
     pygame.draw.rect(screen, (rojo), rect, 2)  


def reducirHitboxAncho(rectangulo_colision,ancho):
    nuevo_ancho = rectangulo_colision.height // ancho
    rectangulo_colision = rectangulo_colision.inflate(-nuevo_ancho, 0)
    return rectangulo_colision

def reducirHitboxAlto(rectangulo_colision,alto):
    nuevo_alto = rectangulo_colision.height // alto
    rectangulo_colision = rectangulo_colision.inflate(0, -nuevo_alto)
    return rectangulo_colision


def NumeroRandomEntre(num1,num2):
    numero_aleatorio = random.randint(num1, num2)
    return numero_aleatorio
    

def obtenerPersonaje(y, x):
    fila = (y - 30) // 99
    columna = (x - 33) // 137
    return fila * 5 + columna

def dibujarFondoMovil(imagen,velocidad,altura_ventana,x):
    x_relativa = x % imagen.get_rect().width
    screen.blit(imagen,(x_relativa - imagen.get_rect().width , altura_ventana))
    if x < ANCHO_VENTANA:
        screen.blit(imagen,(x_relativa,altura_ventana))
    x -= velocidad
    return x

def getSuperficies(path,filas,columnas):
    lista=[]
    superficie_imagen=pygame.image.load(path)
    #Redefino el tamaño de la imagen
    superficie_imagen = pygame.transform.scale(superficie_imagen, (superficie_imagen.get_width() / 2, superficie_imagen.get_height() / 2))
    #print(superficie_imagen) Imprime <Surface(anchoxaltox32 SW)>
    fotograma_ancho=int(superficie_imagen.get_width()/columnas)
    fotograma_alto=int(superficie_imagen.get_height()/filas)
    
    for fila in range(filas):
        for columna in range(columnas):
            x=columna*fotograma_ancho
            y=fila*fotograma_alto
            superficie_fotograma=superficie_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
            lista.append(superficie_fotograma)
    return lista


class Juego():
    def __init__(self):
        self.running = True
        self.stage = 0
    def detener(self):
        self.running = False


class Jugador():
    def __init__(self,personaje):
        self.sprites=getSuperficies("juego/sprites/personajes.jpg", 5, 5)
        self.player=personaje
        self.imagen=self.sprites[self.player]
        self.rect=pygame.Rect(80, 523, 70, 25)
        self.pos_imagen=[self.rect.x,self.rect.y-33]


    def dibujar(self,pantalla):
        self.imagen = self.sprites[self.player]
        pantalla.blit(self.imagen, self.pos_imagen)
        #dibujarHitbox(screen,self.rect)  
  

    def manejo(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                key_up_pressed = True
                if self.rect.y >393: #393
                    self.rect.y=self.rect.y - 10
                    self.pos_imagen[1]-= 10
            elif event.key == pygame.K_DOWN:
                key_down_pressed = True
                if self.rect.y <523:
                    self.rect.y=self.rect.y + 10
                    self.pos_imagen[1]+= 10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                key_up_pressed = False
            elif event.key == pygame.K_DOWN:
                key_down_pressed = False

    def invertido(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                key_up_pressed = True
                if self.rect.y >393: #353
                    self.rect.y=self.rect.y - 10
                    self.pos_imagen[1]-= 10
            elif event.key == pygame.K_UP:
                key_down_pressed = True
                if self.rect.y <523:
                    self.rect.y=self.rect.y + 10
                    self.pos_imagen[1]+= 10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                key_up_pressed = False
            elif event.key == pygame.K_UP:
                key_down_pressed = False

class Enemigo():
    def __init__(self,personaje):
        self.sprites=getSuperficies("juego/sprites/personajes.jpg", 5, 5)
        self.player=personaje
        self.usado=[]
        self.imagen=self.sprites[self.player]
        self.rect=pygame.Rect(900, NumeroRandomEntre(393,523), 70, 25)
        self.pos_imagen=[self.rect.x,self.rect.y-33]
        self.contador=0


    def dibujar(self,pantalla):
        self.imagen = self.sprites[self.player]
        pantalla.blit(self.imagen,self.pos_imagen)
        #dibujarHitbox(screen,self.rect) 
    

    def cambio(self):
        self.rect.y=NumeroRandomEntre(393,523)
        self.pos_imagen[1]=self.rect.y-33
        self.usado.append(self.player)

        activo=True
        while activo:
            valor = NumeroRandomEntre(0, 24)
            if valor not in self.usado:
                self.player = valor
                activo = False
            elif int(len(self.usado))==25: 
                self.player = valor
                activo = False
            

    def movimiento(self,event,timer_segundos):
        if int(len(self.usado))==25  :
            pass
        elif event.type==timer_segundos:

            self.rect.x -= 2 #Velocidad del enemigo 2
            self.pos_imagen[0]-=2
            if len(self.usado)>12:
                self.rect.x -= 1 #Velocidad del enemigo despues de pasar a la mitad 3
                self.pos_imagen[0]-=1

            if self.rect.x<=-50:
                self.rect.x=850
                self.pos_imagen[0]=850
                self.cambio()
                self.contador=0
    #393,523
    def arribAbajoAleatorio(self):
        if self.rect.x in range(0,800):
            if self.contador<3:
                valor=NumeroRandomEntre(1, 2)
                if valor==1:
                    if self.rect.y+10<523:
                        self.rect.y+=10
                        self.pos_imagen[1]+=10
                        self.contador+=1
                    else:
                        self.rect.y-=10
                        self.pos_imagen[1]-=10
                        self.contador+=1
                if valor==2:
                    if self.rect.y-10>393:
                        self.rect.y-=10
                        self.pos_imagen[1]-=10
                        self.contador+=1
                    else:
                        self.rect.y+=10
                        self.pos_imagen[1]+=10
                        self.contador+=1
        
                
        
            
class Meta():
    def __init__(self,meta):
        self.sprite=[pygame.image.load("juego/sprites/metaroja.png"),pygame.image.load("juego/sprites/meta.amarilla.png"),pygame.image.load("juego/sprites/meta.png")]
        self.sprite=self.sprite[meta]
        self.sprite=pygame.transform.scale(self.sprite, (100, 155))

                
class Banana():
    def __init__(self):
        self.sprite=pygame.image.load("juego/sprites/banana.png")
        self.rect=self.sprite.get_rect()
        self.rect=reducirHitboxAncho(self.rect,1.3)
        self.rect=reducirHitboxAlto(self.rect,1.3)
        self.sprite=pygame.transform.scale(self.sprite, (40, 40))
        self.rect.x=900
        self.rect.y=NumeroRandomEntre(383,514)
        self.advertencia=pygame.image.load("juego/sprites/cambio_imagen.jpg")
        self.advertencia = pygame.transform.scale(self.advertencia, (50, 90))
        self.lanza_banana=True
        self.velocidad=4
        self.efecto_tiempo=4
        self.efecto_aplicado=False

    
    def movimiento(self,event,timer_segundos,enemigo):
        if int(len(enemigo.usado))==25  :
            pass
        elif event.type==timer_segundos:
            if self.lanza_banana:
                self.rect.x -= self.velocidad #Velocidad de la banana
                if self.rect.x<=-50:
                    self.rect.y=NumeroRandomEntre(383,514)
                    self.rect.x=850
                    self.lanza_banana=False
            
    
    def dibujarAdvertencia(self):
        self.advertencia.set_alpha(250) 
        screen.blit(self.advertencia,(10,250))

    def dibujarAdvertenciaTitilando(self):
        self.advertencia.set_alpha(20) 
        screen.blit(self.advertencia,(10,250))
        
class Tabla():
    def __init__(self):
        self.nombre="None"
        self.puntos=0
        self.sprite=0
        
    def ordenar_lista_mayormenor(self,lista):
        n = len(lista)
        for i in range(n-1):
            indice_maximo=i
            for j in range(i+1, n):
                if lista[j]["puntos"] > lista[indice_maximo]["puntos"]:
                    indice_maximo = j

            auxiliar = lista[i]
            lista[i] = lista[indice_maximo]
            lista[indice_maximo] = auxiliar
        return lista

