import pygame
# Inicializar Pygame
pygame.init()

from puntuaciones import *

banana=Banana()
juego=Juego()
tutorial=Tutorial()
selector=Selector(texto)
nombre=Nombre()
carrera=Carrera()
victoria=Victoria()
derrota=Derrota()
puntuaciones=Puntuaciones()

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
        nombre_texto=fuente.render(nombre.input_text, True, (blanco))
        nombre_titulo=fuente.render("Ingrese su nombre:", True, (blanco))
        nombre.cargarNombre(nombre_texto,nombre_titulo)

    
    #ELEGIR PERSONAJE
    while juego.stage==2:
        selector.menu(juego)
     
    #RESETEO JUEGO
    carrera.validar,carrera.contador,carrera.x_meta,carrera.meta_bandera,carrera.segundos,carrera.score,enemigo,player,carrera.stop_tiempo=resetear(selector,tabla)
    
    #CAMBIO MUSICA
    cambiarMusica("juego/sonidos/carrera.mp3")

      
    #CARRERA    
    while juego.stage==3:
        pocision = fuente.render("#"+str(carrera.contador), True, (carrera.color_pos))
        tiempo = fuente_score.render("Time: {0:.2f}".format(carrera.segundos)  , True, (violeta))
        score_vivo= fuente_score.render("Score: {0:.0f}".format(carrera.score)  , True, (violeta))
        meta=Meta(carrera.meta_bandera)
        carrera.cargarCarrera(tiempo,score_vivo,enemigo,player,juego,pocision,banana,meta)
        carrera.terminarCarrera(enemigo,meta,juego)

    #Musica Gane
    if juego.stage==4:
        sonido_gane.play(maxtime=4200)
        pygame.mixer.music.stop()

    #Musica Perdi
    else:
        pygame.mixer.music.stop()
        sonido_perdi.play(maxtime=7000)


    #Gano
    while juego.stage==4:
        score_final=fuente_final.render("{0:.0f}".format(carrera.score),True, (violeta))
        victoria.cargarPantalla(score_final,juego,puntuaciones)
        tabla.puntos=carrera.score
                    
                    
    #Perdi
    while juego.stage==5:
        derrota.cargarPantalla(juego)
      
    #Creo la lista de ganadores
    if juego.stage==6:
        puntuaciones.crearLista(tabla)
        
    #Puntuaciones
    while juego.stage== 6:
        puntuaciones.eventos(juego)
        titulo_final=fuente.render("TABLA DE PUNTUACIONES", True, (blanco))
        puntuaciones.crearTabla(titulo_final)
        if not puntuaciones.cargue_tabla:
            for jugador in puntuaciones.lista:
                print(len(puntuaciones.lista))
                print(jugador[1])
                nombre_final=fuente.render(str(jugador[1]) , True, (blanco))
                puntos_final=fuente.render("{0:.0f}".format(jugador[2]), True, (blanco))
                pocision_final=fuente.render(str(puntuaciones.pocision)+" .", True, (blanco))
                lista_sprites=getSuperficies("juego/sprites/personajes.jpg", 5, 5)
                sprite_final=lista_sprites[int(jugador[3])]
                sprite_final=pygame.transform.scale(sprite_final, (40, 40))
                puntuaciones.cargarPuntuaciones(titulo_final,tabla,pocision_final,puntos_final,nombre_final,sprite_final)
            puntuaciones.cargue_tabla=True
        #     for jugador in puntuaciones.lista:
        #         nombre_final=fuente.render(str(jugador.nombre) , True, (blanco))
        #         puntos_final=fuente.render("{0:.0f}".format(jugador.puntos), True, (blanco))
        #         pocision_final=fuente.render(str(puntuaciones.pocision)+" .", True, (blanco))
        #         puntuaciones.cargarPuntuaciones(titulo_final,tabla,pocision_final,puntos_final,nombre_final)
        
        pygame.display.flip()
        
        
# Finalizar Pygame
pygame.quit()