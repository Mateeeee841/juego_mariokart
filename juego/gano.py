from carrera import *

class Victoria():
    def __init__(self):
        self.imagen =   pygame.image.load("juego/sprites/ganador.jpg")
        self.imagen =   pygame.transform.scale(self.imagen, (ANCHO_VENTANA, ALTO_VENTANA))
        
        
    def cargarPantalla(self,score_final,juego,puntuaciones):
        screen.blit(self.imagen, (0, 0))
        screen.blit(score_final, (430, 70))
        pygame.draw.rect(screen, (negro), rectangulo_gano, 10)
        screen.blit(continuar, (rectangulo_gano.x + 30, rectangulo_gano.y + 30))
        pygame.display.flip()
        self.eventos(juego,puntuaciones)

    def eventos(self,juego,puntuaciones):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego.stage= -1
                juego.detener()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sonido_gane.stop()
                    juego.stage= 7
                    puntuaciones.cargue_tabla=False

    
    

        