import csv
import datetime
import socket
from random import randint, uniform
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

def generateopenings():
	openings=[]
	for i in range(6):
		openings.append(round(uniform(0,1),1))
	openings.extend([0,0,0,0])
	return openings




openings=[1,1,1,1,1,1,0,0,0,0]
conn = socketStuff()
simulacao = []
past = []
start =  str(datetime.datetime.now())
contadorTimeStep=0
contadorAuxiliarTimeStep=0

while True:
    data = conn.recv(1024)

    if not data:
        break

    data = organizeData(data)

    #SALVAR NO BANCO DE DADOS
    simulacao.append(past + openings[:-4]) #past e T e data eh T + 1
    past = data
    openings=[1,1,1,1,1,1,0,0,0,0]
    openingsStr = ', '.join(str(e) for e in openings)
    conn.sendall(str.encode(openingsStr))
    contadorAuxiliarTimeStep=contadorAuxiliarTimeStep+1
    if (contadorAuxiliarTimeStep>98):
		contadorTimeStep=contadorTimeStep+1
    print contadorAuxiliarTimeStep,"\n"
    print contadorTimeStep,"\n"
conn.close()


#salvando no arquivo
with open("resultados/111111.csv", 'a') as resultados:
    writer = csv.writer(resultados, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for timestep in simulacao[97:-1]:
        writer.writerow(timestep)

#print(start)
#print(str(datetime.datetime.now()))
