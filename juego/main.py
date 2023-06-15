import pygame




# Inicializar Pygame


pygame.init()

from cine import *




juego=Juego()
tutorial=Tutorial()
selector=Selector(texto_mover,texto_seleccionar)
nombre=Nombre()
carrera=Carrera()
victoria=Victoria()
derrota=Derrota()
puntuaciones=Puntuaciones()
cinematica=Cinematica()
while juego.running:
    
    #ESTABLESCO QUE HAY UN NUEVO JUGADOR
    tabla=Tabla()
    
    #CAMBIO MUSICA
    cambiarMusica("juego/sonidos/menu.mp3")
    
    #TUTORIAL
    while juego.stage==0:
        tutorial.cargarImagen(juego)

                    
    #INGREAR NOMBRE
    while juego.stage==1:
        nombre.obtenerNombre(juego,tabla)
        nombre_texto=fuente.render(nombre.input_text, True, (negro))
        nombre_titulo=fuente.render("Ingrese su nombre:", True, (blanco))
        indicacion=fuente2.render("Espacio para continuar", True, (blanco))
        nombre.cargarNombre(nombre_texto,nombre_titulo,indicacion)

    
    #ELEGIR PERSONAJE
    while juego.stage==2:
        selector.menu(juego)
     
    #RESETEO JUEGO
    carrera.validar,carrera.contador,carrera.x_meta,carrera.meta_bandera,carrera.segundos,carrera.score,enemigo,player,carrera.stop_tiempo=resetear(selector,tabla)
    
    #CAMBIO MUSICA
    cambiarMusica("juego/sonidos/carrera.mp3")
    tiempo=0
    
   
    
    #CINEMATICA
      
    while juego.stage==3:
        cinematica.cargarCine(juego,enemigo,player)
        if cinematica.tiempo>8: #Duracion de la cinematica
                juego.stage=4
                
    banana=Banana()
    
    #CARRERA    
    
    while juego.stage==4:
        pocision = fuente.render("#"+str(carrera.contador), True, (carrera.color_pos))
        tiempo = fuente_score.render("Time: {0:.2f}".format(carrera.segundos)  , True, (violeta))
        score_vivo= fuente_score.render("Score: {0:.0f}".format(carrera.score)  , True, (violeta))
        meta=Meta(carrera.meta_bandera)
        carrera.cargarCarrera(tiempo,score_vivo,enemigo,player,juego,pocision,banana,meta)
        carrera.terminarCarrera(enemigo,meta,juego)
        
        
    #Musica Gane
    if juego.stage==5:
        sonido_gane.play(maxtime=4200)
        pygame.mixer.music.stop()

    #Musica Perdi
    else:
        pygame.mixer.music.stop()
        sonido_perdi.play(maxtime=7000)


    #Gano
    while juego.stage==5:
        score_final=fuente_final.render("{0:.0f}".format(carrera.score),True, (violeta))
        victoria.cargarPantalla(score_final,juego,puntuaciones)
        tabla.puntos=carrera.score
                    
                    
    #Perdi
    while juego.stage==6:
        derrota.cargarPantalla(juego)
      
    #Creo la lista de ganadores
    if juego.stage==7:
        puntuaciones.crearLista(tabla)
        
    #Puntuaciones
    while juego.stage== 7:
        puntuaciones.eventos(juego)
        titulo_final=fuente.render("TABLA DE PUNTUACIONES", True, (blanco))
        puntuaciones.crearTabla(titulo_final)
        if not puntuaciones.cargue_tabla:
            for jugador in puntuaciones.lista:
                nombre_final=fuente.render(str(jugador[1]) , True, (blanco))
                puntos_final=fuente.render("{0:.0f}".format(jugador[2]), True, (blanco))
                pocision_final=fuente.render(str(puntuaciones.pocision)+" .", True, (blanco))
                lista_sprites=getSuperficies("juego/sprites/personajes.jpg", 5, 5)
                sprite_final=lista_sprites[int(jugador[3])]
                sprite_final=pygame.transform.scale(sprite_final, (40, 40))
                puntuaciones.cargarPuntuaciones(titulo_final,tabla,pocision_final,puntos_final,nombre_final,sprite_final)
            puntuaciones.cargue_tabla=True
        pygame.display.flip()
        
        
# Finalizar Pygame
pygame.quit()