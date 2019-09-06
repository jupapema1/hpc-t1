import os,timeit,time
import prueba1

def main():
	f=open("data1.txt","w+")

	num_datos=2
	num_muestras=1

	for j in range(num_muestras):
		i=0
		for i in range (num_datos):
			#n=pow(10,i+1)	#n es el iterador sobre el tamaño de la matriz
			n=100*(i+1)
			result=prueba1.main(n)	#Se almacena el resultado
			f.write("{} {}\n".format(n,result))
			print("result: {}".format(result))


if __name__ == '__main__':
	main()