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

def generatePopulation(tamPopulation,contadorTimeStep):
	Population=[]
	valoratual=[]
	fitnessatual=0
	for contador1 in range(0,tamPopulation):
		valoratual=[]
		for i in range(0,6):
			valoratual.append(randint(0,1))
		valoratual.extend([0,0,0,0])
		geneatual=Gene(valoratual,calcularFitness(valoratual,contadorTimeStep))
		Population.append(copy.copy(geneatual))
	populacaoOrdenada = sorted(Population, key = Gene.getfitness,reverse=True)	
	return populacaoOrdenada

def calcularFitness(valorGeneAtual,contadorTimeStep):
	if(contadorTimeStep<=2234):
		valorFitness= valorGeneAtual[4]*45+valorGeneAtual[5]*45+valorGeneAtual[0]*40+valorGeneAtual[1]*40+valorGeneAtual[2]*35+valorGeneAtual[3]*35
	if (contadorTimeStep>2234 and contadorTimeStep<=4466):
		valorFitness=valorGeneAtual[0]*45+valorGeneAtual[1]*45-valorGeneAtual[2]*35-valorGeneAtual[3]*35+valorGeneAtual[4]*40+valorGeneAtual[5]*40
	if(contadorTimeStep>4466 and contadorTimeStep<=6698):
		valorFitness=valorGeneAtual[0]*35+valorGeneAtual[1]*35-valorGeneAtual[2]*45-valorGeneAtual[3]*45-valorGeneAtual[4]*40-valorGeneAtual[5]*40
	if(contadorTimeStep>6698):
		valorFitness=valorGeneAtual[0]*35+valorGeneAtual[1]*35-valorGeneAtual[2]*40-valorGeneAtual[3]*40-valorGeneAtual[4]*45-valorGeneAtual[5]*45
	return valorFitness+200
	
	
def generateNextGeneration(population,contadorTimeStep):
	nextPopulation=[]
	pospai1=0
	pospai2=0
	roleta,valormaximo=geradorRoleta(population)
	#print len(roleta)
	#print len(population)
	for i in range(0,int(len(population)/10)):
		nextPopulation.append(copy.deepcopy(population[i]))
	for i in range(0,int(len(population)/10)):
		del(population[0])
	for i in range(int(len(population)/2)):
		randpai1=randint(0,valormaximo)
		randpai2=randint(0,valormaximo)
		for j in range(len(population)):
			if((randpai1>=roleta[j].getvalorinicial()) and (randpai1<=roleta[j].getvalorfinal())):
				pospai=j
			if((randpai2>=roleta[j].getvalorinicial()) and (randpai2<=roleta[j].getvalorfinal())):
				pospai2=j
		filho1,filho2=cruzamento(copy.deepcopy(population[pospai1]),copy.deepcopy(population[pospai2]),contadorTimeStep)
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
	return roleta,acumuladorfitness

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


def recalculaFitness(population,contadorTimeStep):
	for i in range(len(population)):
		population[i].setfitness(calcularFitness(population[i].getvalor(),contadorTimeStep))
	populacaoOrdenada = sorted(population, key = Gene.getfitness,reverse=True)
	return populacaoOrdenada			
