'''
script que permite crear una estructura de datos en formato json asociada a la informacion correspondiente obtenida desde los modelos
y la cantidad de veces que aparecen por medida de desempeno
'''

import pandas as pd
import json

class defineViewDiagram(object):

    def __init__(self, dataSet1, dataSet2, dataSet3, dataSet4, pathOutput):

        self.dataSet1 = dataSet1
        self.dataSet2 = dataSet2
        self.dataSet3 = dataSet3
        self.dataSet4 = dataSet4
        self.pathOutput = pathOutput

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
        dictPrecision = self.createDataStruct(self.dataSet1, "Precision")
        dictAccuracy = self.createDataStruct(self.dataSet2, "Accuracy")
        dictRecall = self.createDataStruct(self.dataSet3, "Recall")
        dictF1 = self.createDataStruct(self.dataSet4, "F1")

        dictFull = [dictPrecision, dictAccuracy, dictRecall, dictF1]
        nameDoc = self.pathOutput+"result.json"
        with open(nameDoc, 'w') as fp:
            json.dump(dictFull, fp)
