'''
Definicion de la clase matriz y sus metodos

'''
import sys
import random
import time
import threading

MAX_NUM=sys.maxsize


class Matriz:

	def __init__(self):
		self.__data = []
		self.__filas = 0
		self.__colums = 0

	def printMat(self):
		print("Imprimiendo matriz...")
		for i in range(self.__filas):
			for j in range(self.__colums):
				if self.at(i,j) == MAX_NUM:
					print("G",end=' ')
				else:
					print(self.at(i,j),end=' ')
			print('\n')

	def llenarMat(self,nCols,nFils,value):
		self.__filas=nFils
		self.__colums=nCols
		self.__data=[]
		for i in range(nCols*nFils):
			self.__data.append(value)

	def initMat(self,nCols,nFils):
		self.__filas=nFils
		self.__colums=nCols
		self.__data=[]
		for i in range(nCols*nFils):
			self.__data.append(0)

	def getCols(self):
		return self.__colums

	def getFils(self):
		return self.__filas

	def at(self,posC,posF):
		idx=self.__colums*posC+posF
		return self.__data[idx]

	def suma(self,a,b):
		if a==MAX_NUM or b==MAX_NUM:
			return MAX_NUM
		else: 
			return a+b

	def editPos(self,posC,posF,val):
		idx=self.__colums*posC+posF
		self.__data[idx]=val

	def randomMat(self,maxValue):
		self.__data=[]
		for i in range(self.__filas*self.__colums):
			self.__data.append(random.randint(0,maxValue))

	def matMult(self,M,R):
		#start=time.time()
		#print("Multiplicando matrices...")
		#end=time.time()
		#print("Matriz llenada en: {} segundos".format(end-start))
		R.llenarMat(self.getCols(),M.getFils(),0)
		for i in range(self.__filas):
			for j in range(self.__colums):
				res=0
				for k in range(self.__colums):
					res+=self.at(i,k)*M.at(k,j)
					R.editPos(i,j,res)


	def matMult2(self,M,R):
		R.llenarMat(self.getCols(),M.getFils(),0)
		for i in range(self.__filas):
			for j in range(self.__colums):
				res=0
				for k in range(self.__colums):
					res+=self.at(i,k)*M.at(k,j)
					R.editPos(i,j,res)
			

	def multMatVec(self,b,c):
		c.llenarMat(len(b),1,0)
		for k in range (self.getFils()):
			c+=c+self.at(k,k)*b(k)


	def mult2(self, B, C):
		C.llenarMat(C.getCols(),C.getFils(),0)
		for j in range(B.getCols()):
			multMatVec(self,B.at(j,j),C)


	def filaXColumna(self,matB,nfila,ncolumn):
		res=0
		for k in range(self.__colums):
			res+=self.at(nfila,k)*matB.at(k,ncolumn)
			#R.editPos()

		print("Resultado: {}".format(res))
		return res










