from intro import *

class Nombre():
    def __init__(self):
        self.input_text=""
        self.max=11
        
    def cargarNombre(self,nombre_texto,nombre_titulo,indicacion):
        screen.fill((azul))
        screen.blit(nombre_titulo,(150,20))
        pygame.draw.rect(screen, (blanco), rectangulo_nombre)
        screen.blit(nombre_texto,(rectangulo_nombre.x+20,rectangulo_nombre.y+10))
        pygame.draw.rect(screen, (blanco), (rectangulo_nombre.x+75,340,250,40),4)
        screen.blit(indicacion,(rectangulo_nombre.x+85,350))
        pygame.display.flip() 
    
    def obtenerNombre(self,juego,tabla):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego.stage=-1
                juego.detener()
            if event.type == pygame.KEYDOWN:
                if self.input_text!="":
                    if event.key == pygame.K_SPACE:
                 
                        tabla.nombre=self.input_text
                        self.input_text = ''
                        juego.stage=2
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                if int(len(self.input_text))<self.max:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_BACKSPACE:
                            pass
                    else:
                        self.input_text += event.unicode
                 
        