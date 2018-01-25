
import funcoes


x=funcoes.generatePopulation(1000)
for i in range(len(x)):
	print x[i].getvalor(),x[i].getfitness()

#newpopulation=funcoes.generateNextGeneration(x,6800)
print "\n","\n","\n","\n","\n"
#for i in range(len(newpopulation)):
#	print newpopulation[i].getvalor(),newpopulation[i].getfitness()
#roleta=funcoes.geradorRoleta(x)
x=funcoes.recalculaFitness(x,7000)
for i in range(len(x)):
	print x[i].getvalor(),x[i].getfitness()
