#	
#	Un generador de instancias simples para closest-pair
#	Crea n puntos aleatorios y los guarda en un archivo
#
import random 

def get_points(n):
	#	rango de los puntos 
	a = -n
	b = n

	#	lista de puntos
	points = list()

	#	Crea los puntos aleatorios y los agrega a la lista
	for i in range (0, n):
		x = round( random.uniform(a, b), 3)
		y = round( random.uniform(a, b), 3)

		points.append( [x, y] )

	#	Muestra los puntos
	for p in points:
		print( str(p) )


	#	Guarda los puntos en un archivo nuevo, sobrescribe si existe
	f = open("puntos-n"+ str(n)+ ".txt", "w")

	f.write(str(n) +  "\n")
	for p in points:
		f.write( str(p[0])+ "\t" + str(p[1]) + "\n")

	f.close()

	return points

get_points(10)
get_points(15)
get_points(20)
get_points(50)
get_points(100)

