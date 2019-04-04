'''
script que permite crear una estructura de datos en formato json asociada a la informacion correspondiente obtenida desde los modelos
y la cantidad de veces que aparecen por medida de desempeno
'''

import pandas as pd
import json

class defineViewDiagram(object):

    def __init__(self, dataSet1, dataSet2, dataSet3, dataSet4, listPerformance, pathOutput):

        self.dataSet1 = dataSet1
        self.dataSet2 = dataSet2
        self.dataSet3 = dataSet3
        self.dataSet4 = dataSet4
        self.pathOutput = pathOutput
        self.listPerformance = listPerformance

    #metodo que permite formar la estructura de datos con respecto al set de datos correspondiente
    def createDataStruct(self, dataSet, performance):

        algorithms = dataSet['Algorithm']#obtenemos los algoritmos
        listUnique = list(set(algorithms))

        dictCount = []

        for element in listUnique:
            count=0

            for element2 in algorithms:
                if element == element2:
                    count+=1

            dictData = {'value': count, 'name': element}
            dictCount.append(dictData)

        dictResponse = {'name':performance, 'data':dictCount}

        return dictResponse

    #metodo que permite formar los diccionarios de respuestas segun la medida de desempeno
    def formatResponse(self):

        #precision, accuracy, recall, f1
        dictP1 = self.createDataStruct(self.dataSet1, self.listPerformance[0])
        dictP2 = self.createDataStruct(self.dataSet2, self.listPerformance[1])
        dictP3 = self.createDataStruct(self.dataSet3, self.listPerformance[2])
        dictP4 = self.createDataStruct(self.dataSet4, self.listPerformance[3])

        dictFull = [dictP1, dictP2, dictP3, dictP4]
        nameDoc = self.pathOutput+"result.json"
        with open(nameDoc, 'w') as fp:
            json.dump(dictFull, fp)
