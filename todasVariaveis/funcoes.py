from __future__ import division
from random import randint
import copy

class Gene(object):
	def __init__(self,valor,fitness):
		self.valor=valor
		self.fitness=fitness
		
	def setvalor(self,valor):
		self.valor=valor
	def getvalor(self):
		return self.valor
	def setfitness(self,fitness):
		self.fitness=fitness
	def getfitness(self):
		return self.fitness


class numeroRoleta(object):
	def __init__(self,valor,fitness,valorinicial,valorfinal):
		self.valor=valor
		self.fitness=fitness
		self.valorinicial=valorinicial
		self.valorfinal=valorfinal
		
	def setvalor(self,valor):
		self.valor=valor
	def getvalor(self):
		return self.valor
	def setfitness(self,fitness):
		self.fitness=fitness
	def getfitness(self):
		return self.fitness
	def setvalorinicial(self,valorinicial):
		self.valorinicial=valorinicial
	def setvalorfinal(self,valorfinal):
		self.valorfinal=valorfinal
	def getvalorinicial(self):
		return self.valorinicial
	def getvalorfinal(self):
		return self.valorfinal

def generatePopulation(tamPopulation):
	Population=[]
	valoratual=[]
	fitnessatual=0
	for contador1 in range(0,tamPopulation):
		valoratual=[]
		for i in range(0,6):
			valoratual.append(randint(0,1))
		valoratual.extend([0,0,0,0])
		geneatual=Gene(valoratual,calcularFitness(valoratual,0))
		Population.append(copy.copy(geneatual))
	populacaoOrdenada = sorted(Population, key = Gene.getfitness,reverse=True)	
	return populacaoOrdenada

def calcularFitness(valorGeneAtual,contadorTimeStep):
	if(contadorTimeStep<=2234):
		valorFitness= valorGeneAtual[0]*100
	if (contadorTimeStep>2234 and contadorTimeStep<=4466):
		valorFitness= 20
	if(contadorTimeStep>4466 and contadorTimeStep<=6698):
		valorFitness= 30
	if(contadorTimeStep>6698):
		valorFitness= 40
	return valorFitness
	
	
def generateNextGeneration(population,contadorTimeStep):
	nextPopulation=[]
	for i in range(0,int(len(population)/10)):
		nextPopulation.append(copy.deepcopy(population[i]))
	for i in range(0,int(len(population)/10)):
		del(population[0])
	for i in range(int(len(population)/2)):
		filho1,filho2=cruzamento(copy.deepcopy(population[randint(0,len(population)-1)]),copy.deepcopy(population[randint(0,len(population)-1)]),contadorTimeStep)
		nextPopulation.append(filho1)
		nextPopulation.append(filho2)
	populacaoOrdenada = sorted(nextPopulation, key = Gene.getfitness,reverse=True)
	return populacaoOrdenada
	
def geradorRoleta(population):
	roleta=[]
	fitnesstotal=0
	acumuladorfitness=0
	for i in range(len(population)):
		fitnesstotal=fitnesstotal+int(population[i].getfitness())
	for i in range(len(population)):
		numeroroletaatual=numeroRoleta(population[i].getvalor(),population[i].getfitness(),acumuladorfitness,acumuladorfitness+int(population[i].getfitness())-1)
		acumuladorfitness=acumuladorfitness+int(population[i].getfitness())
		roleta.append(numeroroletaatual)
	return roleta

def cruzamento(pai1,pai2,contadorTimeStep):
		genefilho1=[]
		genefilho2=[]
		pivo=randint(0,5)
		for i in range(0,pivo):
			genefilho1.append(pai1.getvalor()[i])
			genefilho2.append(pai2.getvalor()[i])
		for i in range(pivo,6):
			genefilho1.append(pai2.getvalor()[i])
			genefilho2.append(pai1.getvalor()[i])
		genefilho1.extend([0,0,0,0])
		genefilho1=mutacao(genefilho1)
		genefilho2.extend([0,0,0,0])
		genefilho2=mutacao(genefilho2)
		filho1=Gene(genefilho1,calcularFitness(genefilho1,contadorTimeStep))
		filho2=Gene(genefilho2,calcularFitness(genefilho2,contadorTimeStep))
		return (filho1,filho2)
		
def mutacao(valorgene):
	x=randint(0,1)
	y=randint(0,5)
	if (x==1):
		if(valorgene[y]==1):
			valorgene[y]=0
		else:
			valorgene[y]=1
	return valorgene
			
