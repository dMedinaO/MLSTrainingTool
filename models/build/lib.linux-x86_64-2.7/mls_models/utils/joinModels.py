'''
script que permite generar la union de modelos y generar el archivo json con los set de elementos
para crear el diagrama de venn de los modelos con la union de los elementos
'''

import pandas as pd
import json

class joinModels(object):

    def __init__(self, data1, data2, data3, data4, listPerformance):

        self.data1 = data1
        self.data2 = data2
        self.data3 = data3
        self.data4 = data4
        self.listPerformance = listPerformance

    #metodo que permite formar un arreglo con el algoritmo y los parametros
    def getListData(self, data):

        dataArray = []

        for i in range(len(data)):
            value = "%s;%s" % (data['Algorithm'][i], data['Params'][i])
            dataArray.append(value)
        return dataArray

    #funcion que permite comparar dos listas y obtener los elementos interaccionantes
    def compareTwoList(self, list1, list2):

        countElement = 0

        for element in list1:
            for element2 in list2:
                if element == element2:
                    countElement+=1
                    break
        return countElement

    #funcion que permite comparar 3 listas y obtener los elementos interaccionantes
    def compareThreeList(self, list1, list2, list3):

        countElement = 0

        for element1 in list1:
            for element2 in list2:
                for element3 in list3:
                    if (element1 == element2) and (element1 == element3):
                        countElement+=1
                        break
        return countElement

    #funcion que permite comparar 4 listas y obtener los elementos interaccionantes
    def compareFourList(self, list1, list2, list3, list4):

        countElement = 0

        for element1 in list1:
            for element2 in list2:
                for element3 in list3:
                    for element4 in list4:
                        if (element1 == element2) and (element1 == element3) and (element1 == element4) and (element2 == element3) and (element2 == element4) and (element3 == element4):
                            countElement+=1
                            break

        return countElement

    #metodo que permite formar el json con la informacion asociada al diagrama de venn
    def joinAndGetUnique(self):

        arrayData1 = self.getListData(self.data1)
        arrayData2 = self.getListData(self.data2)
        arrayData3 = self.getListData(self.data3)
        arrayData4 = self.getListData(self.data4)

        #formamos el diccionario con los elementos asociados
        dictResponse = {"sets":[0], "label": self.listPerformance[0], "size": len(arrayData1)}
        dictResponse = {"sets":[1], "label": self.listPerformance[1], "size": len(arrayData2)}
        dictResponse = {"sets":[2], "label": self.listPerformance[2], "size": len(arrayData3)}
        dictResponse = {"sets":[3], "label": self.listPerformance[3], "size": len(arrayData4)}

        #hacemos la comparacion de las listas en dos
        dictResponse = {"sets":[0,1], "size": self.compareTwoList(arrayData1, arrayData2)}
        dictResponse = {"sets":[0,2], "size": self.compareTwoList(arrayData1, arrayData3)}
        dictResponse = {"sets":[0,3], "size": self.compareTwoList(arrayData1, arrayData4)}
        dictResponse = {"sets":[1,2], "size": self.compareTwoList(arrayData2, arrayData3)}
        dictResponse = {"sets":[1,3], "size": self.compareTwoList(arrayData2, arrayData4)}
        dictResponse = {"sets":[3,4], "size": self.compareTwoList(arrayData3, arrayData4)}

        #hacemos la comparacion de las listas en tres elementos
        dictResponse = {"sets":[0,1,2], "size": self.compareThreeList(arrayData1, arrayData2, arrayData3)}
        dictResponse = {"sets":[0,1,3], "size": self.compareThreeList(arrayData1, arrayData2, arrayData4)}
        dictResponse = {"sets":[1,2,3], "size": self.compareThreeList(arrayData2, arrayData3, arrayData4)}

        #hacemos la comparacion de los elementos en las 4 listas
        dictResponse = {"sets":[0,1,2,3], "size": self.compareFourList(arrayData1, arrayData2, arrayData3, arrayData4)}
