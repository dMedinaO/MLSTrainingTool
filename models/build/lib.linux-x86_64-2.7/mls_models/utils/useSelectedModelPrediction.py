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
from mls_models.utils import encodingFeatures

import pandas as pd
import json
import numpy as np

class useSelectedModels(object):

    def __init__(self, dataSet, metaModels, pathResponse, featureResponse):

        self.dataSet = pd.read_csv(dataSet)
        self.metaModelsInfo = metaModels
        self.pathResponse = pathResponse
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
        for i in range(len(metaModels['models'])):

            #obtenemos el algoritmo...
            algorithm = metaModels['models'][i]['algorithm']
            parametros = metaModels['models'][i]['params']

            if algorithm == 'AdaBoostRegressor':
                n_estimators = self.searchParamValue(parametros,'n_estimators')
                loss = self.searchParamValue(parametros,'loss')
                AdaBoostObject = AdaBoost.AdaBoost(self.data, self.target, int(n_estimators), loss)
                AdaBoostObject.trainingMethod()
                predictionsData.append(AdaBoostObject.predicctions.tolist())

            if algorithm == 'Bagging':

                n_estimators = self.searchParamValue(parametros,'n_estimators')
                bootstrap = self.searchParamValue(parametros,'bootstrap')
                bagginObject = Baggin.Baggin(self.data,self.target,int(n_estimators), bootstrap)
                bagginObject.trainingMethod()
                predictionsData.append(bagginObject.predicctions.tolist())

            if algorithm == 'DecisionTree':

                criterion = self.searchParamValue(parametros,'criterion')
                splitter = self.searchParamValue(parametros,'splitter')
                decisionTreeObject = DecisionTree.DecisionTree(self.data, self.target, criterion, splitter)
                decisionTreeObject.trainingMethod()
                predictionsData.append(decisionTreeObject.predicctions.tolist())

            if algorithm == 'GradientBoostingRegressor':

                criterion = self.searchParamValue(parametros,'criterion')
                n_estimators = self.searchParamValue(parametros,'n_estimators')
                loss = self.searchParamValue(parametros,'loss')
                min_samples_split = self.searchParamValue(parametros,'min_samples_split')
                min_samples_leaf = self.searchParamValue(parametros,'min_samples_leaf')

                gradientObject = Gradient.Gradient(self.data,self.target, int(n_estimators), loss, criterion, int(min_samples_split), int(min_samples_leaf))
                gradientObject.trainingMethod()
                predictionsData.append(gradientObject.predicctions.tolist())

            if algorithm == 'KNeighborsRegressor':

                n_neighbors = self.searchParamValue(parametros,'n_neighbors')
                algorithmData = self.searchParamValue(parametros,'algorithm')
                metric = self.searchParamValue(parametros,'metric')
                weights = self.searchParamValue(parametros,'weights')

                knnObect = knn_regression.KNN_Model(self.data, self.target, int(n_neighbors), algorithmData, metric,  weights)
                knnObect.trainingMethod()
                predictionsData.append(knnObect.predicctions.tolist())

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
                predictionsData.append(MLPObject.predicctions.tolist())

            if algorithm == 'NuSVM':

                kernel = self.searchParamValue(parametros,'kernel')
                degree = self.searchParamValue(parametros,'degree')
                gamma = self.searchParamValue(parametros,'gamma')
                nu = self.searchParamValue(parametros,'nu')

                nuSVM = NuSVR.NuSVRModel(self.data, self.target, kernel, int(degree), float(gamma), float(nu))
                nuSVM.trainingMethod()
                predictionsData.append(nuSVM.predicctions.tolist())

            if algorithm == 'SVM':

                kernel = self.searchParamValue(parametros,'kernel')
                degree = self.searchParamValue(parametros,'degree')
                gamma = self.searchParamValue(parametros,'gamma')

                svm = SVR.SVRModel(self.data, self.target, kernel, int(degree), float(gamma))
                svm.trainingMethod()
                predictionsData.append(svm.predicctions.tolist())

            if algorithm == 'RandomForestRegressor':

                criterion = self.searchParamValue(parametros,'criterion')
                n_estimators = self.searchParamValue(parametros,'n_estimators')
                bootstrap = self.searchParamValue(parametros,'bootstrap')
                min_samples_split = self.searchParamValue(parametros,'min_samples_split')
                min_samples_leaf = self.searchParamValue(parametros,'min_samples_leaf')

                rf = RandomForest.RandomForest(self.data, self.target, int(n_estimators), criterion, int(min_samples_split), int(min_samples_leaf), bootstrap)
                rf.trainingMethod()
                predictionsData.append(rf.predicctions.tolist())

        #hacemos el promedio por fila de los modelos obtenidos para generar la correspondiente prediccion
        predictionMean, predictionSTD = self.meanPredictions(predictionsData)

        #obtenemos las nuevas medidas de desempeno del meta modelo:
        performanceValues = performanceData.performancePrediction(self.target, predictionMean)
        pearsonValue = performanceValues.calculatedPearson()['pearsonr']
        spearmanValue = performanceValues.calculatedSpearman()['spearmanr']
        kendalltauValue = performanceValues.calculatekendalltau()['kendalltau']
        rScore = performanceValues.calculateRscore()

        #estas medidas las exportamos a un json para cargar la informacion...
        dictResponse = {"Spearman": spearmanValue, "R_Score": rScore, "Pearson":pearsonValue, "Kendalltau":kendalltauValue}
        nameDoc = self.pathResponse+"performance_model.json"
        with open(nameDoc, 'w') as fp:
            json.dump(dictResponse, fp)

        #dejamos en un json adicional la data del entrenamiento para graficar la regresion asociada a la data predicha v/s la real
        dictResponseData = {"real": self.target.tolist(), "prediccion": predictionMean}
        nameDoc = self.pathResponse+"prediction_data.json"
        with open(nameDoc, 'w') as fp:
            json.dump(dictResponseData, fp)

    #metodo que permite obtener las predicciones ponderadas
    def meanPredictions(self, matrixData):

        predictionMean = []
        predictionSTD = []

        for i in range(len(matrixData[0])):
            dataValues = []
            for j in range(len(matrixData)):
                dataValues.append(matrixData[j][i])
            npdata = np.mean(dataValues)
            std = np.std(dataValues)
            predictionMean.append(npdata)
            predictionSTD.append(std)

        return predictionMean, predictionSTD
