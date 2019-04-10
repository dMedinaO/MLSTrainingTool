'''
script que recibe los 4 set de datos y forma una lista unica con los algoritmos y parametros,
posterior a ello, representa los modelos en formato JSON para poder ser utilizados en las
predicciones y elementos asociados al meta modelo
'''

import pandas as pd
import json

class exportMetaModel(object):

    def __init__(self, data1, data2, data3, data4, pathOutput):

        self.data1 = data1
        self.data2 = data2
        self.data3 = data3
        self.data4 = data4
        self.pathOutput = pathOutput

    #obtener una lista con algorithm-modelos
    def createListData(self, values1, values2):

        listData = []
        for i in range (len(values1)):

            data = values1[i]+"+"+values2[i]
            listData.append(data)
        return listData

    #metodo para obtener los elementos unicos de la lista de datos
    def getUniqueModels(self):

        listData1 = self.createListData(self.data1['Algorithm'], self.data1['Params'])
        listData2 = self.createListData(self.data2['Algorithm'], self.data2['Params'])
        listData3 = self.createListData(self.data3['Algorithm'], self.data3['Params'])
        listData4 = self.createListData(self.data4['Algorithm'], self.data4['Params'])

        #formamos una lista unica
        listFull = listData1+listData2+listData3+listData4
        listUnique = list(set(listFull))

        #a partir de la lista... tomamos los modelos para formar el JSON
        dictResponse = []

        for element in listUnique:
            data = element.split("+")
            model = {}
            model.update({"algorithm":data[0]})
            parametros = []
            dataParams = data[1].split("-")
            for element in dataParams:
                values = element.split(":")
                dictParam = {values[0]:values[1]}
                parametros.append(dictParam)

            model.update({"params": parametros})
            dictResponse.append(model)

        dictResponse ={"models": dictResponse}

        #exportamos a JSON
        nameDoc = self.pathOutput+"meta_models.json"
        with open(nameDoc, 'w') as fp:
            json.dump(dictResponse, fp)
