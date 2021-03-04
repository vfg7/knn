# import os
# scriptpath = os.path.dirname(C:\Users\victorfg\Download\iris.data.txt)
# relpath

import csv
with open('iris.data.txt',"r") as csvfile:
    lines = csv.reader(csvfile)
    # for row in lines:
    #     print(','.join(row))

import random
def dados(nome, share, treinamento=[], teste=[]):
    with open(nome, "r") as csvfile:
        lines = csv.reader(csvfile)
        # print(lines)
        # print("lines")
        dataset = list(lines)
        # print(dataset)
        # print(len(dataset))
        # print("dataset")

        for x in range(len(dataset)-1):
                # print(x, "(x)", dataset[x])
                #caso aleatório
                if random.random() < share:
                    treinamento.append(dataset[x])
                else:
                    teste.append(dataset[x])

                #caso teste
                # if x % 50 > 15:
                #     treinamento.append(dataset[x])
                # else:
                #     teste.append(dataset[x])
        print(len(treinamento), " treinamento", len(teste), " teste")


def normalize(matriz=[]):
    #normalizar só o dataset inteiro, se não dá erro
    max = [5, 3, 2, 2]
    min = [5, 3, 2, 2]
    #valores inciais fazem sentido pro iris e apenas pra ele
    resp = []
    resp = matriz
    for x in range(len(matriz) - 1):
      for y in range(4):
        # print(x, "(x)", y, "(y)", matriz[x][y], "(cell)")
        if float(matriz[x][y]) > max[y]:
            max[y] = float(matriz[x][y])
        if float(matriz[x][y]) < min[y]:
            min[y] = float(matriz[x][y])

    # print(max)
    # print(min)

    delta = [0, 0, 0, 0]
    for x in range(4):
        delta[x] = max[x]-min[x]

    # print(delta)

    for x in range(len(matriz) - 1):
        for y in range(4):
            # print(matriz[x][y], "cell", min[y], " (min)", delta[y]," (delta)")
            resp[x][y] = (float(matriz[x][y])-min[y])/delta[y]

    return resp

import math


def euclidistance(teste, compara):
    distancia = 0
    length = len(teste)
    for x in range(length):
        distancia += pow((float(teste[x])-float(compara[x])), 2)
    return math.sqrt(distancia)


def kpoints(k, casoteste=[], dados=[]):
    resposta = []
    for x in range(k):
        resposta.append([100, "a"])
    # print(resposta)
    # print("deve ter", k, " elementos")

    for x in range(len(dados)-1):
        caso = euclidistance(casoteste, dados[x])
        # print("caso")
        # print(caso)
        for y in range(k):
            if caso < float(resposta[y][0]):
                resposta.insert(y, [caso, dados[x][4]])
                resposta.pop()
               # print("inseriu caso na posição ",y , "e deu pop no último. quebra loop")
                break

        # print("resposta atual em ", x)
        # print(resposta)
    # return resposta
    # print('para k = ', k)
    print("menores distancias/ classificação da flor")
    print(resposta)
    answer = decide(resposta)
    return answer

def decide(caso=[]):
    decisao = [['Iris-virginica', 0], ['Iris-setosa', 0], ['Iris-versicolor', 0]]

    for i in range(len(caso)):
        if caso[i][1] == decisao[0][0]:
            decisao[0][1] += 1
        elif caso[i][1] == decisao[1][0]:
            decisao[1][1] += 1
        elif caso[i][1] == decisao[2][0]:
            decisao[2][1] += 1

    print(decisao)
    answer = ""

    if decisao[0][1] > decisao[1][1]:
        if decisao[0][1] > decisao[2][1]:
           # print(decisao[0][0])
            answer = decisao[0][0]
        else:
           # print(decisao[2][0])
            answer = decisao[2][0]
    else:
        if decisao[1][1] > decisao[2][1]:
          #  print(decisao[1][0])
            answer = decisao[1][0]
        else:
            #print(decisao[2][0])
            answer = decisao[2][0]

    return answer


#-----------------------main------------------------

treinamento=[]
teste =[]
dados("iris.data.txt", 0.66, treinamento, teste)
normal = []
normal = treinamento
# print(normal)
# normal = normalize(normal)
# print("normalizado")
# print(normal)

print('----------------------------------------------kpoints-------------------------------------------------------------------------')

testcase = teste
# print(teste)
# testcase = normalize(testcase)
# print(testcase)

# testcase = [5, 2, 2, 1]

accuracy = []
accres =0;

for i in range(len(teste)):
    testcase = teste[i]
    check = testcase[4]
    testcase.pop()
    print("testcase (", i, "): ", testcase)
    print("caso atual", check)
    print("\n")
    result = ""

    for j in range(1, 10, 2):

        result = kpoints(j, testcase, normal)

        if result == check:
            accuracy.append(1)
            accres += 1
            print("respota certa! Acurácia+")
            print("\n")
        else:
            accuracy.append(0)


acc_result = accres/len(accuracy)
print("Acurácia =", acc_result, "%")

