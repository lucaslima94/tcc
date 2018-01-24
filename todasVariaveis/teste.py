
import funcoes


x=funcoes.generatePopulation(1000)
#for i in range(100,109):
#	print x[i].getvalor(),x[i].getfitness()

newpopulation=funcoes.generateNextGeneration(x,0)
#print "\n","\n","\n","\n","\n"
for i in range(990,999):
	print newpopulation[i].getvalor(),newpopulation[i].getfitness()
#roleta=funcoes.geradorRoleta(x)


