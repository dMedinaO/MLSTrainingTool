'''
script que permite usar el json seleccionado para obtener la data de los modelos
y a partir de esta, procesar la info y usarla como predictor o en caso contrario
usarla para obtener las medidas de desempeno asociadas al meta modelo en si
'''
from mls_models.supervised_learning_clf import AdaBoost
from mls_models.supervised_learning_clf import Baggin
from mls_models.supervised_learning_clf import BernoulliNB
from mls_models.supervised_learning_clf import DecisionTree
from mls_models.supervised_learning_clf import GaussianNB
from mls_models.supervised_learning_clf import Gradient
from mls_models.supervised_learning_clf import knn
from mls_models.supervised_learning_clf import MLP
from mls_models.supervised_learning_clf import NuSVM
from mls_models.supervised_learning_clf import RandomForest
from mls_models.supervised_learning_clf import SVM

#utils para el manejo de set de datos y su normalizacion
from mls_models.utils import transformDataClass
from mls_models.utils import transformFrequence
from mls_models.utils import ScaleNormalScore
from mls_models.utils import ScaleMinMax
from mls_models.utils import ScaleDataSetLog
from mls_models.utils import ScaleLogNormalScore

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from mls_models.supervised_learning_clf import createConfusionMatrix

import pandas as pd
import json
import numpy as np

class useSelectedModels(object):

    def __init__(self, dataSet, dataSetNew, metaModels, pathResponse):

        self.dataSet = pd.read_csv(dataSet)
        self.dataSetNew = pd.read_csv(dataSetNew)#set de datos de nuevos ejemplos
        self.metaModelsInfo = metaModels
        self.pathResponse = pathResponse

        #preparamos la data
        self.prepareDataSet()

    #metodo que permite preparar el set de datos
    def prepareDataSet(self):

        columnas=self.dataSet.columns.tolist()
        x=columnas[len(columnas)-1]
        targetResponse=self.dataSet[x]#clases
        y=columnas[0:len(columnas)-1]
        dataValues=self.dataSet[y]#atributos

        #transformamos la clase si presenta atributos discretos
        transformData = transformDataClass.transformClass(targetResponse)
        self.target = transformData.transformData
        self.dictTransform = transformData.dictTransform

        #ahora transformamos el set de datos por si existen elementos discretos...
        transformDataSet = transformFrequence.frequenceData(dataValues)
        dataSetNewFreq = transformDataSet.dataTransform

        #ahora aplicamos el procesamiento segun lo expuesto
        applyNormal = ScaleNormalScore.applyNormalScale(dataSetNewFreq)
        self.data = applyNormal.dataTransform

        #manejo de los nuevos ejemplos....
        #ahora transformamos el set de datos por si existen elementos discretos...
        transformDataSetNew = transformFrequence.frequenceData(self.dataSetNew)
        dataSetNewFreqNew = transformDataSetNew.dataTransform

        applyNormalNew = ScaleNormalScore.applyNormalScale(dataSetNewFreqNew)
        self.dataNew = applyNormalNew.dataTransform

    #metodo que permite buscar elementos de un diccionario en un array de diccionario...
    def searchParamValue(self, paramData, key):

        response = 0
        for i in range(len(paramData)):

            keysData = paramData[i].keys()
            isData = 0
            if keysData[0] == key:
                isData = 1

            if isData == 1:
                response = paramData[i][key]
                break
        return response

    #metodo que permite aplicar los modelos seleccionados
    def applyModelsSelected(self):

        classArray = list(set(self.target))#evaluamos si es arreglo binario o no
        kindDataSet = 1

        if len(classArray) ==2:
            kindDataSet =1
        else:
            kindDataSet =2

        try:
            metaModels = json.loads(open(self.metaModelsInfo).read())
            predictionsData = []#matriz con las predicciones obtenidas del modelo
            for i in range(len(metaModels['models'])):

                #obtenemos el algoritmo...
                algorithm = metaModels['models'][i]['algorithm']
                parametros = metaModels['models'][i]['params']

                if algorithm == 'AdaBoostClassifier':
                    algorithmData = self.searchParamValue(parametros,'Algorithm')
                    n_estimators = self.searchParamValue(parametros,'n_estimators')
                    AdaBoostObject = AdaBoost.AdaBoost(self.data, self.target, int(n_estimators), algorithmData, 2)
                    AdaBoostObject.trainingMethod(kindDataSet)
                    predictionsData.append(AdaBoostObject.model.predict(self.dataNew).tolist())

                if algorithm == 'Bagging':

                    n_estimators = self.searchParamValue(parametros,'n_estimators')
                    bootstrap = self.searchParamValue(parametros,'bootstrap')
                    bagginObject = Baggin.Baggin(self.data,self.target, int(n_estimators), bootstrap,2)
                    bagginObject.trainingMethod(kindDataSet)
                    predictionsData.append(bagginObject.model.predict(self.dataNew).tolist())

                if algorithm == 'BernoulliNB':

                    bernoulliNB = BernoulliNB.Bernoulli(self.data, self.target, 2)
                    bernoulliNB.trainingMethod(kindDataSet)
                    predictionsData.append(bernoulliNB.model.predict(self.dataNew).tolist())

                if algorithm == 'DecisionTree':

                    criterion = self.searchParamValue(parametros,'criterion')
                    splitter = self.searchParamValue(parametros,'splitter')
                    decisionTreeObject = DecisionTree.DecisionTree(self.data, self.target, criterion, splitter,2)
                    decisionTreeObject.trainingMethod(kindDataSet)
                    predictionsData.append(decisionTreeObject.model.predict(self.dataNew).tolist())

                if algorithm == 'GaussianNB':

                    gaussianObject = GaussianNB.Gaussian(self.data, self.target, 2)
                    gaussianObject.trainingMethod(kindDataSet)
                    predictionsData.append(gaussianObject.model.predict(self.dataNew).tolist())


                if algorithm == 'GradientBoostingClassifier':

                    criterion = self.searchParamValue(parametros,'criterion')
                    n_estimators = self.searchParamValue(parametros,'n_estimators')
                    min_samples_split = self.searchParamValue(parametros,'min_samples_split')
                    min_samples_leaf = self.searchParamValue(parametros,'min_samples_leaf')

                    gradientObject = Gradient.Gradient(self.data,self.target, int(n_estimators), loss, int(min_samples_split), int(min_samples_leaf), 2)
                    gradientObject.trainingMethod(kindDataSet)
                    predictionsData.append(gradientObject.model.predict(self.dataNew).tolist())

                if algorithm == 'KNeighborsClassifier':

                    n_neighbors = self.searchParamValue(parametros,'n_neighbors')
                    algorithmData = self.searchParamValue(parametros,'algorithm')
                    metric = self.searchParamValue(parametros,'metric')
                    weights = self.searchParamValue(parametros,'weights')

                    knnObect = knn.knn(self.data, self.target, int(n_neighbors), algorithmData, metric,  weights,2)
                    knnObect.trainingMethod(kindDataSet)
                    predictionsData.append(knnObect.model.predict(self.dataNew).tolist())

                if algorithm == 'MLPClassifier':

                    activation = self.searchParamValue(parametros,'activation')
                    solver = self.searchParamValue(parametros,'solver')
                    learning_rate = self.searchParamValue(parametros,'learning')
                    hidden_layer_sizes_a = 1
                    hidden_layer_sizes_b = 1
                    hidden_layer_sizes_c = 1
                    alpha = self.searchParamValue(parametros,'alpha')
                    max_iter = self.searchParamValue(parametros,'max_iter')
                    shuffle = self.searchParamValue(parametros,'shuffle')

                    MLPObject = MLP.MLP(self.data, self.target, activation, solver, learning_rate, hidden_layer_sizes_a,hidden_layer_sizes_b,hidden_layer_sizes_c, float(alpha), int(max_iter), shuffle, 2)
                    MLPObject.trainingMethod(kindDataSet)
                    predictionsData.append(MLPObject.model.predict(self.dataNew).tolist())

                if algorithm == 'NuSVM':

                    kernel = self.searchParamValue(parametros,'kernel')
                    degree = self.searchParamValue(parametros,'degree')
                    gamma = self.searchParamValue(parametros,'gamma')
                    nu = self.searchParamValue(parametros,'nu')

                    nuSVM = NuSVM.NuSVM(self.data, self.target, kernel, float(nu), int(degree), 0.01, 2)
                    nuSVM.trainingMethod(kindDataSet)

                    predictionsData.append(nuSVM.model.predict(self.dataNew).tolist())


                if algorithm == 'SVM':

                    kernel = self.searchParamValue(parametros,'kernel')
                    degree = self.searchParamValue(parametros,'degree')
                    gamma = self.searchParamValue(parametros,'gamma')
                    C_value = self.searchParamValue(parametros,'c')

                    svm = SVM.SVM(self.data, self.target, kernel, float(C_value), int(degree), 0.01, 2)
                    svm.trainingMethod(kindDataSet)
                    predictionsData.append(svm.model.predict(self.dataNew).tolist())

                if algorithm == 'RandomForestClassifier':

                    criterion = self.searchParamValue(parametros,'criterion')
                    n_estimators = self.searchParamValue(parametros,'n_estimators')
                    bootstrap = self.searchParamValue(parametros,'bootstrap')
                    min_samples_split = self.searchParamValue(parametros,'min_samples_split')
                    min_samples_leaf = self.searchParamValue(parametros,'min_samples_leaf')

                    rf = RandomForest.RandomForest(self.data, self.target, int(n_estimators), criterion, 2, 1, bootstrap, 2)
                    rf.trainingMethod(kindDataSet)
                    predictionsData.append(rf.model.predict(self.dataNew).tolist())

            self.exportResultModel(predictionsData)
            print 0
        except:
            print 1
    #metodo que permite exportar los resultados obtenidos
    def exportResultModel(self, predictionsData):

        #hacemos la ponderacion para obtener la data final
        dataResponseWeight = self.meanPredictions(predictionsData)
        uniqueList = list(set(self.target))

        matrixData = []

        #formamos el csv con la data y obtenemos la distribucion de valores segun la lista para generar las pbb de la clase
        for i in range(len(dataResponseWeight)):
            columnValues = self.getValuesColumnOfMatrix(predictionsData, i)
            contData = []

            #obtengo la distribucion
            for element in uniqueList:
                cont=0
                for element2 in columnValues:
                    if element == element2:
                        cont+=1
                prob = float(cont)/float(len(columnValues))*50
                contData.append(prob)

            #formamos un string con las probabilidades para agregarlo al csv
            stringProb = ""
            uniqueListTransform = self.traductorDict(uniqueList)
            for j in range(len(uniqueListTransform)):
                stringProb = stringProb+ " class: "+str(uniqueListTransform[j]) + "-prob: "+ str(contData[j])

            classResponse = ""
            for key in self.dictTransform:
                if self.dictTransform[key] == dataResponseWeight[i]:
                    classResponse = key
                    break

            row = [i+1, classResponse, stringProb]
            matrixData.append(row)

        #exportamos a csv
        header = ["example", "class", "Prob"]
        df = pd.DataFrame(matrixData, columns=header)
        df.to_csv(self.pathResponse+"responseTryModel.csv", index=False)

    #metodo que permite hacer la traduccion de elementos
    def traductorDict(self, uniqueList):
        uniqueListTransform = []

        for data in uniqueList:
            for element in self.dictTransform:
                if self.dictTransform[element] == data:
                    uniqueListTransform.append(element)
                    break
        return uniqueListTransform

    #metodo que permite obtener los elementos de una columna en una matriz de datos
    def getValuesColumnOfMatrix(self, matrix, column):

        columnData = []

        for i in range(len(matrix)):
            columnData.append(matrix[i][column])
        return columnData

    #metodo que permite buscar el maximo de elementos por lista, a partir de ella, retornar el valor correspondiente a la clase
    def getMaxValues(self, dataValues, listUnique):

        dictCount = {}
        dictLista = []
        for classData in listUnique:
            count = 0
            for data in dataValues:
                if data == classData:
                    count+=1
            dictCount.update({str(classData): count})
            dictLista.append(count)

        #obtenemos el mayor valor de todas...
        response = listUnique[0]

        for key in dictCount:
            if dictCount[key] == max(dictLista):
                response = key
                break
        return int(response)

    #metodo que permite obtener las predicciones ponderadas
    def meanPredictions(self, matrixData):

        dataClassValues = []

        #obtenemos las listas unicas
        uniqueList = list(set(self.target))

        for i in range(len(matrixData[0])):
            dataValues = []
            for j in range(len(matrixData)):
                dataValues.append(matrixData[j][i])

            #buscamos el maximo por lista
            dataClassValues.append(self.getMaxValues(dataValues, uniqueList))
        return dataClassValues
