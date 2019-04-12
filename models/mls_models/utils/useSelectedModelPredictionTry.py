'''
script que permite usar el json seleccionado para obtener la data de los modelos
y a partir de esta, procesar la info y usarla como predictor o en caso contrario
usarla para obtener las medidas de desempeno asociadas al meta modelo en si
'''
from mls_models.supervised_learning_predicction import AdaBoost
from mls_models.supervised_learning_predicction import Baggin
from mls_models.supervised_learning_predicction import DecisionTree
from mls_models.supervised_learning_predicction import Gradient
from mls_models.supervised_learning_predicction import knn_regression
from mls_models.supervised_learning_predicction import MLP
from mls_models.supervised_learning_predicction import NuSVR
from mls_models.supervised_learning_predicction import RandomForest
from mls_models.supervised_learning_predicction import SVR
from mls_models.supervised_learning_predicction import performanceData

#utils para el manejo de set de datos y su normalizacion
from mls_models.utils import transformDataClass
from mls_models.utils import transformFrequence
from mls_models.utils import ScaleNormalScore
from mls_models.utils import ScaleMinMax
from mls_models.utils import ScaleDataSetLog
from mls_models.utils import ScaleLogNormalScore

import pandas as pd
import json
import numpy as np

class useSelectedModels(object):

    def __init__(self, dataSet, dataSetNew, metaModels, pathResponse):

        self.dataSet = pd.read_csv(dataSet)#set de datos de entrenamiento
        self.dataSetNew = pd.read_csv(dataSetNew)#set de datos de nuevos ejemplos
        self.metaModelsInfo = metaModels
        self.pathResponse = pathResponse

        #preparamos la data
        self.prepareDataSet()

    #metodo que permite preparar el set de datos y el set de datos de nuevos ejemplos
    def prepareDataSet(self):

        columnas=self.dataSet.columns.tolist()
        x=columnas[len(columnas)-1]
        targetResponse=self.dataSet[x]#clases
        y=columnas[0:len(columnas)-1]
        dataValues=self.dataSet[y]#atributos

        #transformamos la clase si presenta atributos discretos
        transformData = transformDataClass.transformClass(targetResponse)
        self.target = transformData.transformData

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

        metaModels = json.loads(open(self.metaModelsInfo).read())

        predictionsData = []#matriz con las predicciones obtenidas del modelo
        response = 0

        try:

            for i in range(len(metaModels['models'])):

                #obtenemos el algoritmo...
                algorithm = metaModels['models'][i]['algorithm']
                parametros = metaModels['models'][i]['params']

                if algorithm == 'AdaBoostRegressor':
                    n_estimators = self.searchParamValue(parametros,'n_estimators')
                    loss = self.searchParamValue(parametros,'loss')
                    AdaBoostObject = AdaBoost.AdaBoost(self.data, self.target, int(n_estimators), loss)
                    AdaBoostObject.trainingMethod()

                    #usamos el modelo entrenado para predecir los nuevos valores
                    predictionsData.append(AdaBoostObject.model.predict(self.dataNew))
                if algorithm == 'Bagging':

                    n_estimators = self.searchParamValue(parametros,'n_estimators')
                    bootstrap = self.searchParamValue(parametros,'bootstrap')
                    bagginObject = Baggin.Baggin(self.data,self.target,int(n_estimators), bootstrap)
                    bagginObject.trainingMethod()

                    #usamos el modelo entrenado para predecir los nuevos valores
                    predictionsData.append(bagginObject.model.predict(self.dataNew))

                if algorithm == 'DecisionTree':

                    criterion = self.searchParamValue(parametros,'criterion')
                    splitter = self.searchParamValue(parametros,'splitter')
                    decisionTreeObject = DecisionTree.DecisionTree(self.data, self.target, criterion, splitter)
                    decisionTreeObject.trainingMethod()

                    #usamos el modelo entrenado para predecir los nuevos valores
                    predictionsData.append(decisionTreeObject.model.predict(self.dataNew))

                if algorithm == 'GradientBoostingRegressor':

                    criterion = self.searchParamValue(parametros,'criterion')
                    n_estimators = self.searchParamValue(parametros,'n_estimators')
                    loss = self.searchParamValue(parametros,'loss')
                    min_samples_split = self.searchParamValue(parametros,'min_samples_split')
                    min_samples_leaf = self.searchParamValue(parametros,'min_samples_leaf')

                    gradientObject = Gradient.Gradient(self.data,self.target, int(n_estimators), loss, criterion, int(min_samples_split), int(min_samples_leaf))
                    gradientObject.trainingMethod()

                    #usamos el modelo entrenado para predecir los nuevos valores
                    predictionsData.append(gradientObject.model.predict(self.dataNew))

                if algorithm == 'KNeighborsRegressor':

                    n_neighbors = self.searchParamValue(parametros,'n_neighbors')
                    algorithmData = self.searchParamValue(parametros,'algorithm')
                    metric = self.searchParamValue(parametros,'metric')
                    weights = self.searchParamValue(parametros,'weights')

                    knnObect = knn_regression.KNN_Model(self.data, self.target, int(n_neighbors), algorithmData, metric,  weights)
                    knnObect.trainingMethod()

                    #usamos el modelo entrenado para predecir los nuevos valores
                    predictionsData.append(knnObect.model.predict(self.dataNew))

                if algorithm == 'MLPRegressor':

                    activation = self.searchParamValue(parametros,'activation')
                    solver = self.searchParamValue(parametros,'solver')
                    learning_rate = self.searchParamValue(parametros,'learning')
                    hidden_layer_sizes_a = 1
                    hidden_layer_sizes_b = 1
                    hidden_layer_sizes_c = 1
                    alpha = self.searchParamValue(parametros,'alpha')
                    max_iter = self.searchParamValue(parametros,'max_iter')
                    shuffle = self.searchParamValue(parametros,'shuffle')

                    MLPObject = MLP.MLP(self.data, self.target, activation, solver, learning_rate, hidden_layer_sizes_a,hidden_layer_sizes_b,hidden_layer_sizes_c, float(alpha), int(max_iter), shuffle)
                    MLPObject.trainingMethod()

                    #usamos el modelo entrenado para predecir los nuevos valores
                    predictionsData.append(MLPObject.model.predict(self.dataNew))

                if algorithm == 'NuSVM':

                    kernel = self.searchParamValue(parametros,'kernel')
                    degree = self.searchParamValue(parametros,'degree')
                    gamma = self.searchParamValue(parametros,'gamma')
                    nu = self.searchParamValue(parametros,'nu')

                    nuSVM = NuSVR.NuSVRModel(self.data, self.target, kernel, int(degree), float(gamma), float(nu))
                    nuSVM.trainingMethod()

                    #usamos el modelo entrenado para predecir los nuevos valores
                    predictionsData.append(nuSVM.model.predict(self.dataNew))

                if algorithm == 'SVM':

                    kernel = self.searchParamValue(parametros,'kernel')
                    degree = self.searchParamValue(parametros,'degree')
                    gamma = self.searchParamValue(parametros,'gamma')

                    svm = SVR.SVRModel(self.data, self.target, kernel, int(degree), float(gamma))
                    svm.trainingMethod()

                    #usamos el modelo entrenado para predecir los nuevos valores
                    predictionsData.append(svm.model.predict(self.dataNew))

                if algorithm == 'RandomForestRegressor':

                    criterion = self.searchParamValue(parametros,'criterion')
                    n_estimators = self.searchParamValue(parametros,'n_estimators')
                    bootstrap = self.searchParamValue(parametros,'bootstrap')
                    min_samples_split = self.searchParamValue(parametros,'min_samples_split')
                    min_samples_leaf = self.searchParamValue(parametros,'min_samples_leaf')

                    rf = RandomForest.RandomForest(self.data, self.target, int(n_estimators), criterion, int(min_samples_split), int(min_samples_leaf), bootstrap)
                    rf.trainingMethod()

                    #usamos el modelo entrenado para predecir los nuevos valores
                    predictionsData.append(rf.model.predict(self.dataNew))

                self.exportResponseResult(predictionsData)
        except:
            response = 1
        print response

    #metodo que permite formar la data de salida y obtener la informacion con respecto a los datos de interes
    def exportResponseResult(self, predictionsData):

        #obtenemos los vectores asociados a los ejemplos y formamos una matriz con la data para exportar a csv con pandas
        predictionMean, predictionSTD, predictionMax, predictionMin = self.meanPredictions(predictionsData)
        matrixResponse = []
        dictResponse = []

        for i in range(len(predictionMin)):
            #agregamos los valores al diccionario
            dictDataValues = {"mean": predictionMean[i], "std": predictionSTD[i], "max": predictionMax[i], "min": predictionMin[i]}

            #agrego los datos de las medidas por cada modelo existente
            columnValues = self.getValuesColumnOfMatrix(predictionsData, i)
            dictDataValues.update({"valuesPrediction" : columnValues})

            row = [predictionMean[i], predictionSTD[i], predictionMax[i], predictionMin[i]]
            matrixResponse.append(row)

            dictResponse.append(dictDataValues)

        header = ['mean', 'std', 'max', 'min']
        df = pd.DataFrame(matrixResponse, columns=header)
        df.to_csv(self.pathResponse+"resultResponseExamples.csv", index=False)

        dictResponseV = {"response": dictResponse}
        #exportamos el JSON
        nameDoc = self.pathResponse+"summaryResponsePredictions.json"
        with open(nameDoc, 'w') as fp:
            json.dump(dictResponseV, fp)

    #metodo que permite obtener los elementos de una columna en una matriz de datos
    def getValuesColumnOfMatrix(self, matrix, column):

        columnData = []

        for i in range(len(matrix)):
            columnData.append(matrix[i][column])
        return columnData

    #metodo que permite obtener las predicciones ponderadas
    def meanPredictions(self, matrixData):

        predictionMean = []
        predictionSTD = []
        predictionMax = []
        predictionMin = []

        for i in range(len(matrixData[0])):
            dataValues = []
            for j in range(len(matrixData)):
                dataValues.append(matrixData[j][i])
            npdata = np.mean(dataValues)
            std = np.std(dataValues)
            maxData = max(dataValues)
            minData = min(dataValues)

            predictionMean.append(npdata)
            predictionSTD.append(std)
            predictionMax.append(maxData)
            predictionMin.append(minData)

        return predictionMean, predictionSTD, predictionMax, predictionMin
