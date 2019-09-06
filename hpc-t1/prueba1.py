import sys
import matriz as m
import time
import timeit


def cargarMat(filename,nuevaMat1):
	print("Cargando matriz...")
	i=0
	f=0
	c=0

	with open(filename) as openfileobject:
		for line in openfileobject:
			vec=line.split('\n')[0].split(' ')
			#print(vec)
			if(vec[0]=='C'):
				print("# columnas: {}".format(vec[1]))
				i+=1
				c=int(vec[1])
			if(vec[0]=='F'):
				print("# filas: {}".format(vec[1]))
				i+=1
				f=int(vec[1])
			if i==2:
				print("Inicializando matriz {}x{}".format(c,f))
				nuevaMat1.initMat(c,f)
				i+=1
			if(len(vec)==3):
				posX=int(vec[0])
				posY=int(vec[1])
				valor=int(vec[2])
				#print("Ingresando valor: {} a la matriz A en la posicion {},{}".format(valor,posX,posY))
				nuevaMat1.editPos(posX,posY,valor)
	
	nuevaMat1.printMat()	#IMPRIMIENDO MATRIZ LEIDA


def main(tam):

	if(len(sys.argv)!=2):
		#print("Ejemplo de entrada: python prueba1.py <tamaño matriz>")
		#exit()
		pass

	#tam=int(sys.argv[1])

	filename='matA.txt'
	M1=m.Matriz()
	M2=m.Matriz()
	M3=m.Matriz()

	#cargarMat(filename,M1)
	#M1.matMult(M1,M2)
	#M2.printMat()

	print("multiplicando matrices de orden {}x{}".format(tam,tam))

	M1.initMat(tam,tam)
	M2.initMat(tam,tam)
	M3.initMat(tam,tam)

	M1.randomMat(100)
	M2.randomMat(100)

	x=timeit.default_timer()

	M1.matMult(M2,M3) #MULTIPLICACION DE MATRICES

	y=timeit.default_timer() - x #SE ALMACENA EN Y EL TIEMPO DE EJECUCIÓN

	return y #RETORNA EL TIEMPO DE EJECUCION DE LA MULTIPLICACION

	'''
	print("M1")
	M1.printMat()
	print("M2")
	M2.printMat()
	print("M3")
	M3.printMat()
	'''


if __name__ == '__main__':
	main()	