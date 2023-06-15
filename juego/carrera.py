from seleccion import *

class Carrera():
    def __init__(self):
        self.x_carretera=0
        self.x_nube=0
        self.x_montaña=0
        self.x_meta=900
        self.meta_bandera=0
        self.velocidad=20
        self.score=1000000.0
        self.segundos=75.0
        self.stop_tiempo=False
        self.validar=True
        self.estoy_chocando=True
        self.contador=25
        self.color_pos=(blanco)
        
    def cargarCarrera(self,tiempo,score_vivo,enemigo,player,juego,pocision,banana,meta):
        screen.blit(background,(0,0))
        self.moverFondo()
        screen.blit(meta.sprite, (self.x_meta, 399))
        self.dibujarBanana(banana,enemigo)
        self.dibujarPersonajes(enemigo,player)
        screen.blit(tiempo, (500, 10))
        screen.blit(score_vivo, (500, 35))
        self.actualizarPocision(enemigo,pocision)
        self.establecerEventos(juego,enemigo,banana,player)
        pygame.display.flip()
        self.chocaron(player,enemigo,banana)
        
    
    def dibujarPersonajes(self,enemigo,player):
        if enemigo.rect.y>player.rect.y:
            player.dibujar(screen)
            enemigo.dibujar(screen)
        else:
            enemigo.dibujar(screen)
            player.dibujar(screen)
        
        
    def moverFondo(self):
        self.x_nube=dibujarFondoMovil(nubes,self.velocidad/400,0,self.x_nube)
        self.x_montaña=dibujarFondoMovil(montañas,self.velocidad/20,0,self.x_montaña)
        self.x_carretera=dibujarFondoMovil(carretera,self.velocidad/1.01,350,self.x_carretera) 
        
        
        
    def establecerEventos(self,juego,enemigo,banana,player):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego.stage=-1
                juego.detener()
            if not self.stop_tiempo:
                if event.type == timer_event:
                    self.segundos-=0.01282
                    self.score-=self.segundos
            elif self.stop_tiempo:
                pass
            enemigo.movimiento(event,timer_segundos)
            if event.type == timer_efecto:
                enemigo.arribAbajoAleatorio()
            banana.movimiento(event,timer_segundos,enemigo)
            self.toqueBanana(banana,player,event)  

            
            
    def dibujarBanana(self,banana,enemigo):
            if int(len(enemigo.usado)) < 22:
                if not banana.lanza_banana:        
                    if round(self.segundos) == NumeroRandomEntre(0, 55) :
                        banana.lanza_banana=True
                if banana.lanza_banana:
                    screen.blit(banana.sprite, (banana.rect.x, banana.rect.y)) 
    
    def toqueBanana(self,banana,player,event):
        self.colisionesBanana(banana,player)
        self.cartelBanana(banana,event)
        self.manejoJugador(event,banana,player)
        
    def colisionesBanana(self,banana,player):
        if pygame.sprite.collide_rect(banana, player):
                banana.efecto_aplicado=True
                banana.efecto_tiempo=4
                
    def cartelBanana(self,banana,event):
        if banana.efecto_aplicado:
                if not banana.efecto_tiempo<2 :
                    banana.dibujarAdvertencia()
                else:
                    banana.dibujarAdvertenciaTitilando()
                if event.type == timer_efecto:
                    banana.efecto_tiempo-=1
           
    def manejoJugador(self,event,banana,player):
            if banana.efecto_tiempo>0 and banana.efecto_aplicado:
                player.invertido(event)
            elif banana.efecto_aplicado and not banana.efecto_tiempo>0:
                banana.efecto_tiempo=4
                banana.efecto_aplicado=False
            else:
                player.manejo(event)
                

        
    def chocaron(self,player,enemigo,banana):
            if pygame.sprite.collide_rect(enemigo, player):
                if enemigo.rect.x>player.rect.x:
                    self.velocidad=3.2
                    banana.velocidad=0.6
                    enemigo.rect.x=+130
                    enemigo.pos_imagen[0]=enemigo.rect.x
                    if self.estoy_chocando:
                        print("suena")
                        sonido_choque.play(maxtime=2000)
                        self.estoy_chocando=False
            else:        
                self.velocidad=20
                banana.velocidad=4
                self.estoy_chocando=True
        
       

    def actualizarPocision(self,enemigo,pocision):
            if enemigo.rect.x>48 :
                self.validar=False
            if enemigo.rect.x<48 and not self.validar:
                self.contador-=1
                self.validar=True
            if self.contador==1:
                self.color_pos=(dorado)
            elif self.contador==2:
                self.color_pos=(plata)
            elif self.contador==3:
                self.color_pos=(bronce)
            else:
                self.color_pos=(blanco)
            screen.blit(pocision, (10, 10))
        


    def terminarCarrera(self,enemigo,meta,juego):
        if int(len(enemigo.usado))==25 :
            self.x_meta=self.x_meta-20
            if self.x_meta<-50 and self.meta_bandera<2:
                self.x_meta=850
                self.meta_bandera+=1
            if self.meta_bandera==2:
                if self.x_meta<180:
                    self.velocidad=1
                    self.stop_tiempo=True
                    
        if self.x_meta<-2000:
            juego.stage= 5
            enemigo.usado=[]
        if self.segundos< 0:
            juego.stage = 6
            perdio=True
            enemigo.usado=[]
      
    
    