import pygame
import random
import time


ALTO_VENTANA= 600
ANCHO_VENTANA=800 
violeta=(125,0,125)
blanco=(255,255,255)
dorado=(255, 215, 0)
plata=(192, 192, 192)
bronce=(205, 127, 50)
azul=(0, 0, 140)
negro=(0,0,0)
celeste=(30,198,255)
rojo=(255, 0, 0)
puntuaciones=[]


screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

timer_segundos=pygame.USEREVENT           #Creo un evento
pygame.time.set_timer(timer_segundos,1) 

timer_event = pygame.USEREVENT  +1 
pygame.time.set_timer(timer_event, 10)  # 10 milisegundos

timer_efecto = pygame.USEREVENT  +2
pygame.time.set_timer(timer_efecto, 1000)

timer_cine = pygame.USEREVENT  +3
pygame.time.set_timer(timer_cine, 1000)

background = pygame.image.load("juego/sprites/sky.png")
background = pygame.transform.scale(background, (ANCHO_VENTANA, ALTO_VENTANA))

nubes= pygame.image.load("juego/sprites/clouds_bg.png")
nubes = pygame.transform.scale(nubes, (ANCHO_VENTANA, ALTO_VENTANA))

montañas= pygame.image.load("juego/sprites/glacial_mountains.png")
montañas = pygame.transform.scale(montañas, (ANCHO_VENTANA, ALTO_VENTANA))

carretera = pygame.image.load("juego/sprites/carretera.jpg")
carretera = pygame.transform.scale(carretera, (ANCHO_VENTANA, 250))





cambio = pygame.image.load("juego/sprites/cambio_imagen.jpg")
cambio = pygame.transform.scale(cambio, (50, 90))


rectangulo_gano = pygame.Rect(230, 520, 450, 80)
rectangulo_nombre= pygame.Rect(175, 200, 400, 80)

fuente = pygame.font.Font(None, 70)
fuente2  = pygame.font.Font(None, 30)
fuente_select=pygame.font.Font(None, 45)
fuente_score = pygame.font.Font(None, 35)
fuente_final= pygame.font.Font(None, 90)
fuente_gano= pygame.font.Font(None, 50)

texto_mover = fuente_select.render("Mover:", True, (blanco))
texto_seleccionar = fuente_select.render("Seleccionar:", True, (blanco))
continuar = fuente_gano.render("Espacio para continuar", True, (negro))



sonido_choque = pygame.mixer.Sound("juego/sonidos/choque.mp3")
sonido_perdi = pygame.mixer.Sound("juego/sonidos/perder.mp3")
sonido_gane = pygame.mixer.Sound("juego/sonidos/gane.mp3")


