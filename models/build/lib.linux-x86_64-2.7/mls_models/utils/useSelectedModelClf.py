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
from sklearn.model_selection import LeaveOneOut
from mls_models.utils import encodingFeatures

import pandas as pd
import json
import numpy as np

class useSelectedModels(object):

    def __init__(self, dataSet, metaModels, pathResponse, cv, featureResponse):

        self.dataSet = pd.read_csv(dataSet)
        self.metaModelsInfo = metaModels
        self.pathResponse = pathResponse
        self.cv = cv
        self.featureResponse = featureResponse

        #preparamos la data
        self.prepareDataSet()

    #metodo que permite preparar el set de datos
    def prepareDataSet(self):

        self.target = self.dataSet[self.featureResponse]#respuestas
        dataValues=self.dataSet
        del dataValues[self.featureResponse]

        #generamos la codificacion
        encoding = encodingFeatures.encodingFeatures(dataValues, 20)
        encoding.evaluEncoderKind()
        dataEncoding = encoding.dataSet

        #aplicamos la normalizacion
        applyNormal = ScaleNormalScore.applyNormalScale(dataEncoding)
        self.data = applyNormal.dataTransform

        #transformamos la clase si presenta atributos discretos
        transformData = transformDataClass.transformClass(self.target)
        self.target = transformData.transformData
        self.dictTransform = transformData.dictTransform

        self.data = dataValues

        print self.data
    #metodo que permite buscar elementos de un diccionario en un array de diccionario...
    def searchParamValue(self, paramData, key):

        response = 0
        for i in range(len(paramData)):

            keysData = paramData[i].keys()

            isData = 0

            if key in keysData:
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

        metaModels = json.loads(open(self.metaModelsInfo).read())
        predictionsData = []#matriz con las predicciones obtenidas del modelo
        for i in range(len(metaModels['models'])):

            #obtenemos el algoritmo...
            algorithm = metaModels['models'][i]['algorithm']
            parametros = metaModels['models'][i]['params']

            if algorithm == 'AdaBoostClassifier':
                algorithmData = self.searchParamValue(parametros,'Algorithm')
                n_estimators = int(self.searchParamValue(parametros,'n_estimators'))
                print algorithmData
                print n_estimators
                AdaBoostObject = AdaBoost.AdaBoost(self.data, self.target, int(n_estimators), algorithmData, self.cv)
                AdaBoostObject.trainingMethod(kindDataSet)
                predictionsData.append(AdaBoostObject.model.predict(self.data).tolist())

            if algorithm == 'Bagging':

                n_estimators = self.searchParamValue(parametros,'n_estimators')
                bootstrap = self.searchParamValue(parametros,'bootstrap')
                bagginObject = Baggin.Baggin(self.data,self.target, int(n_estimators), bootstrap,self.cv)
                bagginObject.trainingMethod(kindDataSet)
                predictionsData.append(bagginObject.model.predict(self.data).tolist())

            if algorithm == 'BernoulliNB':

                bernoulliNB = BernoulliNB.Bernoulli(self.data, self.target, self.cv)
                bernoulliNB.trainingMethod(kindDataSet)
                predictionsData.append(bernoulliNB.model.predict(self.data).tolist())

            if algorithm == 'DecisionTree':

                criterion = self.searchParamValue(parametros,'criterion')
                splitter = self.searchParamValue(parametros,'splitter')
                decisionTreeObject = DecisionTree.DecisionTree(self.data, self.target, criterion, splitter,self.cv)
                decisionTreeObject.trainingMethod(kindDataSet)
                predictionsData.append(decisionTreeObject.model.predict(self.data).tolist())

            if algorithm == 'GaussianNB':

                gaussianObject = GaussianNB.Gaussian(self.data, self.target, self.cv)
                gaussianObject.trainingMethod(kindDataSet)
                predictionsData.append(gaussianObject.model.predict(self.data).tolist())


            if algorithm == 'GradientBoostingClassifier':

                criterion = self.searchParamValue(parametros,'criterion')
                n_estimators = self.searchParamValue(parametros,'n_estimators')
                min_samples_split = self.searchParamValue(parametros,'min_samples_split')
                min_samples_leaf = self.searchParamValue(parametros,'min_samples_leaf')
                loss = self.searchParamValue(parametros,'loss')

                gradientObject = Gradient.Gradient(self.data,self.target, int(n_estimators), loss, int(min_samples_split), int(min_samples_leaf), self.cv)
                gradientObject.trainingMethod(kindDataSet)
                predictionsData.append(gradientObject.model.predict(self.data).tolist())

            if algorithm == 'KNeighborsClassifier':

                n_neighbors = self.searchParamValue(parametros,'n_neighbors')
                algorithmData = self.searchParamValue(parametros,'algorithm')
                metric = self.searchParamValue(parametros,'metric')
                weights = self.searchParamValue(parametros,'weights')

                knnObect = knn.knn(self.data, self.target, int(n_neighbors), algorithmData, metric,  weights,self.cv)
                knnObect.trainingMethod(kindDataSet)
                predictionsData.append(knnObect.model.predict(self.data).tolist())

            if algorithm == 'MLPClassifier':

                activation = self.searchParamValue(parametros,'activation')
                solver = self.searchParamValue(parametros,'solver')
                learning_rate = self.searchParamValue(parametros,'learning')
                hidden_layer_sizes_a = int(self.searchParamValue(parametros,'hidden_a'))
                hidden_layer_sizes_b = int(self.searchParamValue(parametros,'hidden_b'))
                hidden_layer_sizes_c = int(self.searchParamValue(parametros,'hidden_c'))
                alpha = float(self.searchParamValue(parametros,'alpha'))
                max_iter = int(self.searchParamValue(parametros,'max_iter'))
                shuffle = self.searchParamValue(parametros,'shuffle')

                MLPObject = MLP.MLP(self.data, self.target, activation, solver, learning_rate, hidden_layer_sizes_a,hidden_layer_sizes_b,hidden_layer_sizes_c, float(alpha), int(max_iter), shuffle, self.cv)
                MLPObject.trainingMethod(kindDataSet)
                predictionsData.append(MLPObject.model.predict(self.data).tolist())

            if algorithm == 'NuSVM':

                kernel = self.searchParamValue(parametros,'kernel')
                degree = self.searchParamValue(parametros,'degree')
                gamma = self.searchParamValue(parametros,'gamma')
                nu = self.searchParamValue(parametros,'nu')

                nuSVM = NuSVM.NuSVM(self.data, self.target, kernel, float(nu), int(degree), 0.01, self.cv)
                nuSVM.trainingMethod(kindDataSet)

                predictionsData.append(nuSVM.model.predict(self.data).tolist())


            if algorithm == 'SVM':

                kernel = self.searchParamValue(parametros,'kernel')
                degree = self.searchParamValue(parametros,'degree')
                gamma = self.searchParamValue(parametros,'gamma')
                C_value = self.searchParamValue(parametros,'c')

                svm = SVM.SVM(self.data, self.target, kernel, float(C_value), int(degree), 0.01, self.cv)
                svm.trainingMethod(kindDataSet)
                predictionsData.append(svm.model.predict(self.data).tolist())

            if algorithm == 'RandomForestClassifier':

                criterion = self.searchParamValue(parametros,'criterion')
                n_estimators = self.searchParamValue(parametros,'n_estimators')
                bootstrap = self.searchParamValue(parametros,'bootstrap')
                min_samples_split = self.searchParamValue(parametros,'min_samples_split')
                min_samples_leaf = self.searchParamValue(parametros,'min_samples_leaf')

                rf = RandomForest.RandomForest(self.data, self.target, int(n_estimators), criterion, 2, 1, bootstrap, self.cv)
                rf.trainingMethod(kindDataSet)
                predictionsData.append(rf.model.predict(self.data).tolist())

        #hacemos la ponderacion para obtener la data final
        dataResponseWeight = self.meanPredictions(predictionsData)

        #estimamos las medidas de desempeno
        if kindDataSet == 1:#binario
            accuracy = accuracy_score(self.target, dataResponseWeight)
            precision = precision_score(self.target, dataResponseWeight)
            recall = recall_score(self.target, dataResponseWeight)
            f1 = f1_score(self.target, dataResponseWeight)
        else:#multiclass
            accuracy = accuracy_score(self.target, dataResponseWeight)
            precision = precision_score(self.target, dataResponseWeight, average='micro')
            recall = recall_score(self.target, dataResponseWeight, average='micro')
            f1 = f1_score(self.target, dataResponseWeight, average='micro')

        #exportamos la respuestas al JSON
        dictResponse = {"Recall": recall, "F1": f1, "Precision":precision, "Accuracy":accuracy}
        nameDoc = self.pathResponse+"performance_model.json"
        with open(nameDoc, 'w') as fp:
            json.dump(dictResponse, fp)

        #traemos la data para hacer la matriz de confusion
        uniqueList = list(set(self.target))
        confusionMatrixDemo = createConfusionMatrix.confusionMatrix(self.target, dataResponseWeight, uniqueList)
        responseMatrix = confusionMatrixDemo.createConfusionMatrixResponseYet(self.dictTransform)

        #exportamos el resultado a un JSON para almacenar la respuesta
        nameDoc = self.pathResponse+"confusionMatrix.json"
        with open(nameDoc, 'w') as fp:
            json.dump(responseMatrix, fp)


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
