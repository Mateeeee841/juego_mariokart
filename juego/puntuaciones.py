from perdio import * 
import sqlite3
class Puntuaciones():
    def __init__(self):
        self.lista=[]
        self.cargue_tabla=False
        self.y_tabla=100
        self.pocision=1
        
    def cargarPuntuaciones(self,titulo_final,tabla,pocision_final,puntos_final,nombre_final,sprite_final):
        self.mostrarTabla(titulo_final,tabla,pocision_final,puntos_final,nombre_final,sprite_final)
        self.lista=[]
        
        
    def crearLista(self,tabla):
        self.baseDatos(tabla)
        

    def baseDatos(self,tabla):
	    with sqlite3.connect("juego/jugadores.db") as conexion:
		    try:
			    sentencia = ''' create  table personajes
			    (
			    id integer primary key autoincrement,
			    nombre text,
			    puntos real,
			    sprite real
			    )
			    '''
			    conexion.execute(sentencia)
			    print("Se creo la tabla personajes")                       
		    except sqlite3.OperationalError:
			    print("La tabla personajes ya existe")


		    #INSERT (Agrego los datos a mi base de datos):
		    try:
			    conexion.execute("insert into personajes(nombre,puntos,sprite) values (?,?,?)", (tabla.nombre, tabla.puntos,tabla.sprite))
			    conexion.commit()# Actualiza los datos realmente en la tabla
		    except:
			    print("Error")
            
		    # SELECT y ORDER BY (Ordeno la lista por una parametro y la imprimo):
		    cursor = conexion.execute("SELECT * FROM personajes ORDER BY puntos DESC")
		    for fila in cursor:
			    self.lista.append(fila) 
            
                
                
            
               
            
    
    
    
    def mostrarTabla(self,titulo_final,tabla,pocision_final,puntos_final,nombre_final,sprite_final):
            screen.blit(pocision_final,(30,self.y_tabla))
            screen.blit(nombre_final,(140,self.y_tabla))
            screen.blit(puntos_final,(440,self.y_tabla))
            screen.blit(sprite_final,(660,self.y_tabla+2))
            # print(tabla.sprite)
            self.y_tabla+=50
            self.pocision+=1
            self.cargue_tabla=True
         

    def crearTabla(self,titulo_final):
        if not self.cargue_tabla:       
            screen.fill((azul))
            self.y_tabla=100
            self.pocision=1
            screen.blit(titulo_final,(70,20))


    def eventos(self,juego):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego.stage= -1
                juego.detener()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    juego.stage=1

                
        

