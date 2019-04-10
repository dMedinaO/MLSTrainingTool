'''
script que permite la seleccion de modelos a partir de la data obtenida en el csv,
recolecta las medidas de desempeno y genera una distribucion por cada elemento, aplica un zscore con
respecto a los valores de la desviacion estandar y obtiene los modelos que superen las 3 desviaciones estandar,
si la cantidad es baja, continua con 2 y si prosigue, continua con 1.5

cada modelo seleccionado se obtiene los parametros y el algoritmo y se almacenan en archivos diferentes para la
posterior union de los modelos
'''

import pandas as pd
import numpy as np
import json

class selectedModel(object):

    def __init__(self, dataSet, pathOutput, listKey, otherKeys):

        self.dataSet = dataSet
        self.pathOutput = pathOutput
        self.listKey = listKey#representa la lista de performance
        self.otherKeys = otherKeys#representa la otra lista de elementos

        #obtenemos los estadisticos
        self.getSatistics()

    #metodo que permite obtener las desviaciones estandar y promedios correspondientes para cada medida
    def getSatistics(self):

        self.meanData = []
        self.stdData = []

        for key in self.listKey:
            self.meanData.append(np.mean(self.dataSet[key]))
            self.stdData.append(np.std(self.dataSet[key]))

    #selected by standar deviation
    def selectedByStandarDV(self, data, stdValue, mean, index):

        index_response = []
        check = mean+(stdValue*index)
        for i in range(len(data)):
            if data[i] >=check:
                index_response.append(i)
        return index_response

    #get index with max values
    def getIndexMaxValues(self, data, maxValue):

        indexData = []

        for i in range(len(data)):
            if data[i]>=maxValue:
                indexData.append(i)
        return indexData

    #metodo que permite seleccionar los elementos a cada medida de desempeno
    def selectedModelData(self, meanValue, stdValue, performance):

        #formamos la lista completa con la informacion asociada
        dataInformation = []

        three_dv = self.selectedByStandarDV(self.dataSet[performance], stdValue, meanValue, 3)
        two_dv = self.selectedByStandarDV(self.dataSet[performance], stdValue, meanValue, 2)
        onepoint_dv = self.selectedByStandarDV(self.dataSet[performance], stdValue, meanValue, 1.5)

        #manejamos los largos asociados y obtenemos los valores correspondientes
        indexJoin = []

        if len(three_dv)>0:
            indexJoin = three_dv
        else:
            if len(two_dv)>0:
                indexJoin = two_dv
            else:
                if len(onepoint_dv)>0:
                    indexJoin = onepoint_dv
                else:#trabajamos solo con el mayor valor.
                    indexJoin = self.getIndexMaxValues(self.dataSet[performance], max(self.dataSet[performance]))

        #a partir de la lista de indices obtenemos los valores para formar el set de datos
        matrixResponse = []

        for index in indexJoin:
            row = []

            for key in self.otherKeys:#completamos con las primeras keys
                row.append(self.dataSet[key][index])

            for performanceData in self.listKey:
                row.append(self.dataSet[performanceData][index])#completamos con las performance
            matrixResponse.append(row)

        #exportamos la data
        header = self.otherKeys + self.listKey
        self.dataFrame = pd.DataFrame(matrixResponse, columns=header)

        nameFile = self.pathOutput+performance+".csv"
        self.dataFrame.to_csv(nameFile, index=False)
    
