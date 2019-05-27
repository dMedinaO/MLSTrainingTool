'''
Clase con la responsabilidad de revisar el desbalance de clases existente en el set de datos
'''

import pandas as pd

class checkUnbalance(object):

    def __init__(self, dataSet, classResponse):

        self.dataSet = dataSet
        self.classResponse = classResponse

    #metodo que permite obtener las categorias y sus cantidades
    def getCagetoriesInClass(self):

        categories = list(set(self.dataSet[self.classResponse]))
        self.dictCategories = {}

        #generamos un contador por cada categoria
        for categorie in categories:
            cont=0
            for element in self.dataSet[self.classResponse]:
                if categorie == element:
                    cont+=1

            self.dictCategories.update({categorie: cont})

    #metodo que permite obtener las proporciones
    def getProportionsCategories(self):

        for categorie in self.dictCategories:
            proportion = self.dictCategories[categorie]*100/len(self.dataSet)
            self.dictCategories[categorie] = proportion
        print  self.dictCategories
