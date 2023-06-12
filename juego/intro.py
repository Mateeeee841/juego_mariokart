from elementos import *


class Tutorial():
    def __init__(self):
        self.leido=False
        self.imagen=self.imagen = pygame.image.load("juego/sprites/introduccion.jpg")
        self.imagen = pygame.transform.scale(self.imagen, (ANCHO_VENTANA, ALTO_VENTANA))

        
    def cargarImagen(self,juego):
        screen.blit(self.imagen, (0, 0))
        self.interactuar(juego)
        pygame.display.flip()


    
    
    def interactuar(self,juego):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego.stage=-1
                juego.detener()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    juego.stage=1
