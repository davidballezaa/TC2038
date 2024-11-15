
import numpy as np
import queue
import random


from pygame.locals import *
from pygame.locals import Color
import pygame
import glob


#	Lee el archivo del mapa
def loadMap(fileName):
	f = open(fileName , "r")
	text = list()
	for line in f:
		aux = line.split('\n')
		text.append( list(map(int, aux[0].split('  '))) )
	#print(text)
	map_cells = np.array(text)
	print(map_cells)
	return(map_cells)



def showCoors(pygame, screen, rows, cols, font, map_cells):
	white = Color('white')
	black = Color('black')

	surface = pygame.Surface((cols * tile_size, rows * tile_size ), pygame.SRCALPHA, 32)
	pygame.draw.rect(  surface, (255, 255, 255, 80),  (0, 0, cols*tile_size, rows*tile_size ) )
	screen.blit(surface, (0, 0))

	for i in range(0, rows ):
		for j in range(0, cols ):
			if map_cells[i][j] == 0:
				textColor = white
			else:
				textColor = black
				
			text = font.render( str( i )+','+ str(j) , True, textColor )
			screen.blit(text, (j*tile_size + (tile_size/6), i*tile_size + (tile_size/3)) )

# Crea el mapa de tiles, calculado las coordenadas usando tile_size
def tiles(screen, map_cells, tile1, tile2):
	for i in range(0, len(map_cells)):
		for j in range(0, len(map_cells[0])):
			if map_cells[i][j] == 0: 
				screen.blit(tile1, (j * tile_size, i * tile_size))
			else:
				screen.blit(tile2, (j * tile_size, i * tile_size))

def yellow_path(pygame, screen, path_tile, path, step):
	for s in range(0, step+1):
		i = path[s][1]
		j = path[s][0]
		
		screen.blit(path_tile, (i*tile_size, j*tile_size) )


# Aqui va tu codigo para encontrar el camino con a*
#def aStar( ): 




def main1():
	global tile_size
	tile_size = 40						# Tamaño de celdas

	pos_init = (9,1)
	pos_target = (7,3)
	
	
	map_cells = loadMap( 'map2.txt' ) 	#	Get map from file, as a numpy array
	
	map_cells[pos_init] = '1'			# Initial position 
	map_cells[pos_target] = '10'		# Target position	

	rows = map_cells.shape[0]			#	Number of rows and cols
	cols = map_cells.shape[1]			#	Number of cols

	#	Cambia por la llamada a tu funcion que encuentra el path usando a*
	# path = aStar(map_cells, pos_init, pos_target, rows, cols)            	
	path  = [(9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (6, 3), (7, 3)]

	print(map_cells, '\n' )
	print('Steps : ', len(path)-1, '\n', path, '\n')



	#	Display game map: init, set the screen size, the refresh time, title, font
	pygame.init()
	screen = pygame.display.set_mode(( cols*tile_size, rows*tile_size ))
	clock = pygame.time.Clock()
	pygame.display.set_caption( 'Skull' )
	font = pygame.font.SysFont('arial.ttf', 20)

	#	Carga las imagenes de tiles y las escala
	img1 = pygame.image.load("tile1.png")
	img2 = pygame.image.load("tile2.png")
	img3 = pygame.image.load("skull.png")
	img4 = pygame.image.load("treasure.png")
	tile_green = pygame.transform.scale(img1, (tile_size, tile_size))
	tile_grey = pygame.transform.scale(img2, (tile_size, tile_size))
	skull = pygame.transform.scale(img3, (tile_size, tile_size))		# imagen skull 
	treasure = pygame.transform.scale(img4, (tile_size, tile_size))		# imagen treasure 

	path_tile = pygame.Surface((tile_size, tile_size))  				# tile amarillo para el path
	path_tile.fill( Color('yellow') ) 

	loop = 1				#	Flag para el loop de animacion
	step = 0				# 	Contador de pasos para el path
	litle_step = 0.0		#	Tamaño de paso
	dir_h = 0				# 	Variables para la dirrecion de moviemtos
	up_down = 1
	left_rigth = 1

	#	x,y position of the skull
	xb = pos_init[1] * tile_size 
	yb = pos_init[0] * tile_size 

	#	"Dibujar" es un ciclo: en cada clock tick, se refresca
	while loop:
		tiles(screen, map_cells, tile_green, tile_grey)
		screen.blit(treasure, (pos_target[1] * tile_size, pos_target[0] * tile_size) )
		
		yellow_path(pygame, screen, path_tile, path, step )
		screen.blit(skull, (xb, yb) )
		
		showCoors(pygame, screen, rows, cols, font, map_cells)
		

		for event in pygame.event.get():
			if event.type == QUIT:
				loop = 0

		

		# Averigua en que direccion se mueve para controlar la animacion
		if step < (len(path) -1) :
			if path[step][1] == path[step+1][1]:
				dir_h = 1
				if path[step][0] > path[step+1][0]:
					left_rigth = 1
				else: 
					left_rigth = -1
			else:
				dir_h = 0
				if path[step][1] > path[step+1][1]:
					up_down = 1
				else: 
					up_down = -1
		elif step >= len(path) :
			litle_step = 0
			step = 0

		litle_step += 0.10 
		xb = path[step][1] * tile_size   
		yb = path[step][0] * tile_size 


		#	Esto hace que avance despacio, y lo reinicia
		if litle_step > 0.90 :
			litle_step = 0
			step += 1
			if step >= len(path):
				step = 0


		# Todo lo que quieras dibujar va antes de estas lineas
		pygame.display.update()
		screen.fill((0, 0, 0))
		clock.tick(32)
	
	pygame.quit()



if __name__ == '__main__':
	main1()
