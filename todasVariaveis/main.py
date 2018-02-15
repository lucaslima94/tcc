import csv
import datetime
import socket
import funcoes

def socketStuff():
    HOST = 'localhost'
    PORT = 50001

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)

    print("Iniciando simulacao\nEsperando inicializacao do BCVTB")

    conn, addr = s.accept()


    return conn

def organizeData(data):
    data = data.decode("utf-8").split(" ")
    data[0] = data[0].split("[")[1]
    data[-1] = data[-1].split("]")[0]
    return data

conn = socketStuff()

simulacao = []
past = []
contador=6699
population=funcoes.generatePopulation(10,contador)
openings = population[0].getvalor()
start =  str(datetime.datetime.now())


while True:
    data = conn.recv(1024)

    if not data:
        break

    data = organizeData(data)

    #SALVAR NO BANCO DE DADOS
    simulacao.append(past + openings[:-4]) #past e T e data eh T + 1
    past = data
    if (contador==2235 or contador==4467 or contador==6699):
		population=funcoes.recalculaFitness(population,contador)
    openings = population[0].getvalor()
    openingsStr = ', '.join(str(e) for e in openings)
    conn.sendall(str.encode(openingsStr))
    population=funcoes.generateNextGeneration(population,contador)
    print contador
    contador=contador+1
conn.close()

#salvando no arquivo
with open("resultados/primavera.csv", 'a') as resultados:
    writer = csv.writer(resultados, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for timestep in simulacao[97:-1]:
        writer.writerow(timestep)

print(start)
print(str(datetime.datetime.now()))
