from gano import * 

class Derrota():
    def __init__(self):
        self.imagen = pygame.image.load("juego/sprites/perder.jpg")
        self.imagen = pygame.transform.scale(self.imagen, (ANCHO_VENTANA, ALTO_VENTANA))
    
    def cargarPantalla(self,juego):
        screen.blit(self.imagen, (0, 0))
        pygame.display.flip()
        self.eventos(juego)
        
        
    def eventos(self,juego):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego.stage= -1
                juego.detener()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sonido_perdi.stop()
                    juego.stage= 1

