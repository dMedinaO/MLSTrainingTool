'''
script que permite obtener las medidas de desempeno generales del modelo,
genera un archivo json con las respuestas obtenidas y procesa la informacion con respecto a la ponderacion de
los elementos existenes en los set de datos seleccionados versus el aporte de estos al set de datos existente
'''

import pandas as pd
import numpy as np
import json

class ponderatedModelPerformance(object):

    def __init__(self, data1, data2, data3, data4, listPerformance, pathOutput):

        self.data1 = data1
        self.data2 = data2
        self.data3 = data3
        self.data4 = data4
        self.listPerformance = listPerformance
        self.pathOutput = pathOutput

    #obtenemos las medias de los resultados segun la performance correspondiente
    def getMeanValuesPerformance(self):

        meanPerformance1 = np.mean(self.data1[self.listPerformance[0]])
        meanPerformance2 = np.mean(self.data2[self.listPerformance[1]])
        meanPerformance3 = np.mean(self.data3[self.listPerformance[2]])
        meanPerformance4 = np.mean(self.data4[self.listPerformance[3]])

        #generamos un diccionario con la informacion asociada
        dictResponse = {self.listPerformance[0]:meanPerformance1, self.listPerformance[1]:meanPerformance2, self.listPerformance[2]:meanPerformance3, self.listPerformance[3]:meanPerformance4}

        #exportamos el resultado
        nameDoc = self.pathOutput+"performance_model.json"
        with open(nameDoc, 'w') as fp:
            json.dump(dictResponse, fp)
