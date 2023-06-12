from nombre import *


class Selector():
    def __init__(self,texto_mover,texto_seleccionar):
        self.sprite=pygame.image.load("juego\sprites/selector_personaje.png")
        self.sprite = pygame.transform.scale(self.sprite, ( 170 ,  140 ))
        self.y_selector=30
        self.x_selector=33
        self.eligiendo=False
        self.seleccion = pygame.image.load("juego/sprites/seleccion.jpg")
        self.seleccion = pygame.transform.scale(self.seleccion, (ANCHO_VENTANA - 100 , ALTO_VENTANA -100 ))
        self.keys = pygame.image.load("juego/sprites/keys.png")
        self.keys = pygame.transform.scale(self.keys, (130, 130 ))
        self.space = pygame.image.load("juego/sprites/space.png")
        self.space = pygame.transform.scale(self.space, (50, 50 ))
        self.texto_mover=texto_mover
        self.texto_seleccionar=texto_seleccionar
        self.numero = NumeroRandomEntre(0,24)
        self.valor=0
        
        
    def menu(self,juego):
        screen.fill((celeste)) 
        screen.blit(self.texto_mover, (50, 10))
        screen.blit(self.texto_seleccionar, (400, 10))
        screen.blit(self.keys, (150, -40))
        screen.blit(self.space, (600, 0))
        screen.blit(self.seleccion, (50, 50))    
        screen.blit(self.sprite, (self.x_selector,self.y_selector))
        self.movimiento(juego)
        pygame.display.flip()
        
    def movimiento(self,juego):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego.stage=-1
                juego.detener()
                print("aa")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if self.x_selector != 581:
                        self.x_selector+=137
                elif event.key == pygame.K_LEFT:
                    if self.x_selector != 33:
                        self.x_selector-=137
                elif event.key == pygame.K_UP:
                    key_up_pressed = True
                    if self.y_selector != 30:
                       self.y_selector-=99
                elif event.key == pygame.K_DOWN:
                    key_down_pressed = True
                    if self.y_selector < 400:
                        self.y_selector+=99 
                if event.key == pygame.K_SPACE:
                    self.asignarPersonaje(juego)
    
    
    def asignarPersonaje(self,juego):
        self.valor=obtenerPersonaje(self.y_selector,self.x_selector)
        if self.numero == self.valor:
            if self.numero == 24:
                self.numero -= 1
            else:
                self.numero += 1
        juego.stage=3    
       
                


