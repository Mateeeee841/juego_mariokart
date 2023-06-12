from puntuaciones import *
import pdb
import sys
class EnemigoCine():
    def __init__(self,num_sprite,lista,x,y):
        self.sprite=lista[num_sprite]
        self.rect=pygame.Rect(x, y, 70, 25)
        self.x=self.rect.x
        self.y=self.rect.y
        self.velocidad=20
        
    def dibujar(self):
        screen.blit(self.sprite,(self.x,self.y))
        
    def mover(self):
        self.x += self.velocidad
        print(self.x)
        
        
class Cinematica():
    def __init__(self):
        self.lista=[]
        self.tiempo=0
        self.contador3=pygame.image.load("juego/sprites/3.png")
        self.contador2=pygame.image.load("juego/sprites/2.png")
        self.contador1=pygame.image.load("juego/sprites/1.png")
        self.contadorgo=pygame.image.load("juego/sprites/Go.png")
        self.sonido_cuenta=pygame.mixer.Sound("juego/sonidos/cuenta.mp3")
        self.sonido_empezo=pygame.mixer.Sound("juego/sonidos/GO.mp3")
        self.sonido_arranque = pygame.mixer.Sound("juego/sonidos/arranca.mp3")
        self.sonido_falla = pygame.mixer.Sound("juego/sonidos/falla.mp3")
        self.sonido_arranque.set_volume(2.5)
        self.humo=pygame.image.load("juego/sprites/smoke.png")
        self.humo=pygame.transform.scale(self.humo, (100, 100))
        self.sono1=False
        self.sono2=False
        self.sono3=False
        self.sonogo=False
        self.sonomo=False
        self.sonofalla=False
        self.var=-1
        self.enemigo1="x"
        self.enemigo2="x"
        self.enemigo3="x"
        self.enemigo4="x"
        self.enemigo5="x"
        
    def obtenerPosicion(self,imagen):
        image_width = imagen.get_width()
        image_height = imagen.get_height()
        x = (ANCHO_VENTANA - image_width) // 2
        y = (ALTO_VENTANA - image_height) // 2
        pocision=(x,y)
        return pocision
        
                
    def cargarFondo(self):
        screen.blit(background,(0,0))
        screen.blit(nubes,(0,0))
        screen.blit(montañas,(0,0))
        screen.blit(carretera,(0,350))
    
    
    
    def cargarCine(self,juego,enemigo,jugador):
            self.cargarFondo()
            jugador.dibujar(screen) 
            pocision1=self.obtenerPosicion(self.contador1)
            pocision2=self.obtenerPosicion(self.contador2)
            pocision3=self.obtenerPosicion(self.contador3)
            pocisiongo=self.obtenerPosicion(self.contadorgo)
            
            if self.tiempo<=5:
                self.obtenerSprites(enemigo,jugador)
                for objeto in self.lista:
                    objeto.dibujar()
                    
            if self.tiempo==2:
                screen.blit(self.contador3,(pocision3))#3
                if not self.sono3:
                    self.sonido_cuenta.play(maxtime=1000)
                    self.sono3=True
            if self.tiempo==3:
                screen.blit(self.contador2,(pocision2))#2
                if not self.sono2:
                    self.sonido_cuenta.play(maxtime=1000)
                    self.sono2=True
            if self.tiempo==4:
                screen.blit(self.contador1,(pocision1))#1
                if not self.sono1:
                    self.sonido_cuenta.play(maxtime=1000)
                    self.sono1=True
            if self.tiempo==5:
                screen.blit(self.contadorgo,(pocisiongo))#GO
                if not self.sonogo:
                    self.sonido_empezo.play(maxtime=1000)
                    self.sonogo=True
                    
            if self.tiempo>7:
                self.cargarFondo()
                jugador.dibujar(screen)
                if not self.sonomo:
                    self.sonido_arranque.play(maxtime=1000)
                    self.sonomo=True
                pygame.display.flip()
                    
            self.eventos(enemigo,jugador)
            if self.tiempo<=5:
                pygame.display.flip()
            
            
           
            
            
    
                
    
    def obtenerSprites(self,enemigo,jugador):
        
        self.var=jugador.player
        if self.var<24 and self.var>17:
            self.var=-1
        if int(len(self.lista))<5 : 
            self.enemigo1=EnemigoCine(self.var+1,enemigo.sprites,200,400)  
            self.lista.append(self.enemigo1)  
            self.enemigo2=EnemigoCine(self.var+2,enemigo.sprites,300,490)  
            self.lista.append(self.enemigo2)  
            self.enemigo3=EnemigoCine(self.var+3,enemigo.sprites,400,400)    
            self.lista.append(self.enemigo3)
            self.enemigo4=EnemigoCine(self.var+4,enemigo.sprites,500,490)    
            self.lista.append(self.enemigo4)
            self.enemigo5=EnemigoCine(self.var+5,enemigo.sprites,600,400)    
            self.lista.append(self.enemigo5)

        

            
    def eventos(self,enemigo,jugador):
        for event in pygame.event.get():
            if event.type==timer_cine:
                self.tiempo+=1
                print(self.tiempo)
            if self.tiempo>5 and self.tiempo<7:
                self.arrancanEnemigos(enemigo,event,jugador)
                
            if self.tiempo>7 and self.tiempo<9:
                screen.blit(self.humo,(80,450))
                jugador.dibujar(screen)
            
            if event.type == pygame.QUIT:
                print("sali")
                juego.stage= -1
                juego.detener()
            
                
            
    def arrancanEnemigos(self,enemigo,event,jugador):
        if self.tiempo <7:
            if event.type == timer_segundos:
                self.cargarFondo()
                screen.blit(self.humo,(80,450))
                if not self.sonofalla:
                    self.sonido_falla.play(maxtime=1000)
                    self.sonofalla=True
                jugador.dibujar(screen)
                if self.lista[0].x<1510:
                    for objeto in self.lista:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                juego.stage= -1
                                juego.detener() 
                                self.lista[0].x=2000    
                        objeto.dibujar()
                        objeto.mover()
                else:
                    self.tiempo =8
                pygame.display.flip()
           

            