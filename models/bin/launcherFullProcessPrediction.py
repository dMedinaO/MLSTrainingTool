'''
script que permite ejecutar todos los algoritmos con distintas variaciones para generar
clasificadores y sus respectivos modelos, almacena en un archivo csv la data que se genera con
respecto a las diversas medidas que se obtienen como resultado del proceso...
'''

import sys
import pandas as pd
import numpy as np
import time
import datetime
import json

from mls_models.supervised_learning_predicction import AdaBoost
from mls_models.supervised_learning_predicction import Baggin
from mls_models.supervised_learning_predicction import DecisionTree
from mls_models.supervised_learning_predicction import Gradient
from mls_models.supervised_learning_predicction import knn_regression
from mls_models.supervised_learning_predicction import MLP
from mls_models.supervised_learning_predicction import NuSVR
from mls_models.supervised_learning_predicction import RandomForest
from mls_models.supervised_learning_predicction import SVR

from mls_models.statistics_analysis import summaryStatistic

from mls_models.dataBase_module import ConnectDataBase
from mls_models.dataBase_module import HandlerQuery
from mls_models.utils import sendEmail

#utils para el manejo de set de datos y su normalizacion
from mls_models.utils import transformDataClass
from mls_models.utils import transformFrequence
from mls_models.utils import ScaleNormalScore
from mls_models.utils import ScaleMinMax
from mls_models.utils import ScaleDataSetLog
from mls_models.utils import ScaleLogNormalScore

#para evaluar la performance
from mls_models.supervised_learning_predicction import performanceData

from mls_models.utils import selectorModels
from mls_models.utils import joinModels
from mls_models.utils import makeworld_cloud
from mls_models.utils import makeDiagrammRepresent
from mls_models.utils import getPerformanceModel
from mls_models.utils import exportMetaModel
from mls_models.utils import useSelectedModelPrediction
from mls_models.utils import encodingFeatures

#funcion que permite eliminar outliers
def removeOutliersData(dataSet, featureResponse):

    outliers = []
    dataValues = dataSet[featureResponse]
    threshold=3
    mean_1 = np.mean(dataValues)
    std_1 =np.std(dataValues)
    index=0
    for y in dataValues:
        z_score= (y - mean_1)/std_1
        if np.abs(z_score) > threshold:
            outliers.append(index)
        index+=1
    return outliers

def completeProcess(dataSetName, pathResponse, dataSetOriginal, featureResponse):

    dataSet = pd.read_csv(dataSetName)
    listKey = ['R_Score','Pearson','Spearman','Kendalltau']
    otherKeys = ['Algorithm', 'Params']
    modelSelecter = selectorModels.selectedModel(dataSet, pathResponse, listKey, otherKeys)
    dataSetsSelected = []

    for i in range(len(listKey)):
        modelSelecter.selectedModelData(modelSelecter.meanData[i], modelSelecter.stdData[i], listKey[i])
        dataSetsSelected.append(modelSelecter.dataFrame)

    #testeamos la generacion del wordcloud
    makeWord = makeworld_cloud.createWorldCloud(dataSetsSelected[0], dataSetsSelected[1], dataSetsSelected[2], dataSetsSelected[3], pathResponse)
    makeWord.createGraphic()

    #testeamos la generacion de la data para el grafico de valores anidados
    makeDiagram = makeDiagrammRepresent.defineViewDiagram(dataSetsSelected[0], dataSetsSelected[1], dataSetsSelected[2], dataSetsSelected[3], listKey, pathResponse)
    makeDiagram.formatResponse()

    #testeamos la generacion del archivo de meta modelos
    exportModel = exportMetaModel.exportMetaModel(dataSetsSelected[0], dataSetsSelected[1], dataSetsSelected[2], dataSetsSelected[3], pathResponse)
    exportModel.getUniqueModels()

    #usamos el meta modelo para obtener las medidas de desempeno
    modelsMeta = useSelectedModelPrediction.useSelectedModels(dataSetOriginal, pathResponse+"meta_models.json", pathResponse, featureResponse)
    modelsMeta.applyModelsSelected()


#funcion que permite calcular los estadisticos de un atributo en el set de datos, asociados a las medidas de desempeno
def estimatedStatisticPerformance(summaryObject, attribute):

    statistic = summaryObject.calculateValuesForColumn(attribute)
    row = [attribute, statistic['mean'], statistic['std'], statistic['var'], statistic['max'], statistic['min']]

    return row

#recibimos los parametros desde la terminal...
emailUser = sys.argv[1]
job = sys.argv[2]
dataSetNameInput = sys.argv[3]
dataSet = pd.read_csv(sys.argv[3])
pathResponse = sys.argv[4]
featureResponse = sys.argv[5]#atributo respuesta
removeOutliers = int(sys.argv[6])

#valores iniciales
start_time = time.time()
inicio = datetime.datetime.now()
iteracionesCorrectas = 0
iteracionesIncorrectas = 0

#revisamos si debo eliminar outliers
if removeOutliers == 2:#se eliminan outliers

    outliers = removeOutliersData(dataSet, featureResponse)
    dataSet.drop(outliers)

#procesamos el set de datos para obtener los atributos y las clases...
targResponse=dataSet[featureResponse]#clases

#generamos una copia y eliminamos la respuesta de los atributos
dataValues = dataSet
del dataValues[featureResponse]

#generamos la codificacion
encoding = encodingFeatures.encodingFeatures(dataValues, 20)
encoding.evaluEncoderKind()
dataEncoding = encoding.dataSet

#aplicamos la normalizacion
applyNormal = ScaleNormalScore.applyNormalScale(dataEncoding)
data = applyNormal.dataTransform

#generamos una lista con los valores obtenidos...
header = ["Algorithm", "Params", "R_Score", "Pearson", "Spearman", "Kendalltau"]
matrixResponse = []

#comenzamos con las ejecuciones...
#AdaBoost

for loss in ['linear', 'square', 'exponential']:
    for n_estimators in [10,50,100,200,500,1000,1500,2000]:
        try:
            print "Excec AdaBoostRegressor with %s - %d" % (loss, n_estimators)
            AdaBoostObject = AdaBoost.AdaBoost(data, targResponse, n_estimators, loss)
            AdaBoostObject.trainingMethod()

            #obtenemos el restante de performance
            performanceValues = performanceData.performancePrediction(targResponse, AdaBoostObject.predicctions.tolist())
            pearsonValue = performanceValues.calculatedPearson()['pearsonr']
            spearmanValue = performanceValues.calculatedSpearman()['spearmanr']
            kendalltauValue = performanceValues.calculatekendalltau()['kendalltau']

            if (pearsonValue!= "ERROR" and spearmanValue != "ERROR" and kendalltauValue != "ERROR" and AdaBoostObject.r_score != "ERROR"):
                params = "loss:%s-n_estimators:%d" % (loss, n_estimators)
                row = ["AdaBoostRegressor", params, AdaBoostObject.r_score, pearsonValue, spearmanValue, kendalltauValue]
                matrixResponse.append(row)
                iteracionesCorrectas+=1
            else:
                iteracionesIncorrectas+=1
        except:
            iteracionesIncorrectas+=1
            pass

#Baggin
for bootstrap in [True, False]:
    for n_estimators in [10,50,100,200,500,1000,1500,2000]:
        try:
            print "Excec Bagging with %s - %d" % (bootstrap, n_estimators)
            bagginObject = Baggin.Baggin(data,targResponse,n_estimators, bootstrap)
            bagginObject.trainingMethod()

            performanceValues = performanceData.performancePrediction(targResponse, bagginObject.predicctions.tolist())
            pearsonValue = performanceValues.calculatedPearson()['pearsonr']
            spearmanValue = performanceValues.calculatedSpearman()['spearmanr']
            kendalltauValue = performanceValues.calculatekendalltau()['kendalltau']

            if (pearsonValue!= "ERROR" and spearmanValue != "ERROR" and kendalltauValue != "ERROR" and bagginObject.r_score != "ERROR"):

                params = "bootstrap:%s-n_estimators:%d" % (str(bootstrap), n_estimators)
                row = ["Bagging", params, bagginObject.r_score, pearsonValue, spearmanValue, kendalltauValue]

                matrixResponse.append(row)
                iteracionesCorrectas+=1
            else:
                iteracionesIncorrectas+=1
        except:
            iteracionesIncorrectas+=1
            pass

#DecisionTree
for criterion in ['mse', 'friedman_mse', 'mae']:
    for splitter in ['best', 'random']:
        try:
            print "Excec DecisionTree with %s - %s" % (criterion, splitter)
            decisionTreeObject = DecisionTree.DecisionTree(data, targResponse, criterion, splitter)
            decisionTreeObject.trainingMethod()

            performanceValues = performanceData.performancePrediction(targResponse, decisionTreeObject.predicctions.tolist())
            pearsonValue = performanceValues.calculatedPearson()['pearsonr']
            spearmanValue = performanceValues.calculatedSpearman()['spearmanr']
            kendalltauValue = performanceValues.calculatekendalltau()['kendalltau']

            if (pearsonValue!= "ERROR" and spearmanValue != "ERROR" and kendalltauValue != "ERROR" and decisionTreeObject.r_score != "ERROR"):
                params = "criterion:%s-splitter:%s" % (criterion, splitter)
                row = ["DecisionTree", params, decisionTreeObject.r_score, pearsonValue, spearmanValue, kendalltauValue]
                matrixResponse.append(row)
                iteracionesCorrectas+=1
            else:
                iteracionesIncorrectas+=1
        except:
            iteracionesIncorrectas+=1
            pass

#gradiente
for loss in ['ls', 'lad', 'huber', 'quantile']:
    for criterion in ['friedman_mse', 'mse', 'mae']:
        for n_estimators in [10,50,100,200,500,1000,1500,2000]:
            try:
                min_samples_leaf=1
                min_samples_split=2
                print "Excec GradientBoostingRegressor with %s - %d - %d - %d" % (loss, n_estimators, min_samples_split, min_samples_leaf)
                gradientObject = Gradient.Gradient(data,targResponse,n_estimators, loss, criterion, min_samples_split, min_samples_leaf)
                gradientObject.trainingMethod()

                performanceValues = performanceData.performancePrediction(targResponse, gradientObject.predicctions.tolist())
                pearsonValue = performanceValues.calculatedPearson()['pearsonr']
                spearmanValue = performanceValues.calculatedSpearman()['spearmanr']
                kendalltauValue = performanceValues.calculatekendalltau()['kendalltau']

                if (pearsonValue!= "ERROR" and spearmanValue != "ERROR" and kendalltauValue != "ERROR" and gradientObject.r_score != "ERROR"):
                    params = "criterion:%s-n_estimators:%d-loss:%s-min_samples_split:%d-min_samples_leaf:%d" % (criterion, n_estimators, loss, min_samples_split, min_samples_leaf)
                    row = ["GradientBoostingRegressor", params, gradientObject.r_score, pearsonValue, spearmanValue, kendalltauValue]
                    matrixResponse.append(row)
                    iteracionesCorrectas+=1
                else:
                    iteracionesIncorrectas+=1
            except:
                iteracionesIncorrectas+=1
                pass

#knn
for n_neighbors in range(1,11):
    for algorithm in ['auto', 'ball_tree', 'kd_tree', 'brute']:
        for metric in ['minkowski', 'euclidean']:
            for weights in ['uniform', 'distance']:
                try:
                    print "Excec KNeighborsRegressor with %d - %s - %s - %s" % (n_neighbors, algorithm, metric, weights)
                    knnObect = knn_regression.KNN_Model(data, targResponse, n_neighbors, algorithm, metric,  weights)
                    knnObect.trainingMethod()

                    performanceValues = performanceData.performancePrediction(targResponse, knnObect.predicctions.tolist())
                    pearsonValue = performanceValues.calculatedPearson()['pearsonr']
                    spearmanValue = performanceValues.calculatedSpearman()['spearmanr']
                    kendalltauValue = performanceValues.calculatekendalltau()['kendalltau']

                    if (pearsonValue!= "ERROR" and spearmanValue != "ERROR" and kendalltauValue != "ERROR" and knnObect.r_score != "ERROR"):
                        params = "n_neighbors:%d-algorithm:%s-metric:%s-weights:%s" % (n_neighbors, algorithm, metric, weights)
                        row = ["KNeighborsRegressor", params, knnObect.r_score, pearsonValue, spearmanValue, kendalltauValue]
                        matrixResponse.append(row)
                        iteracionesCorrectas+=1
                    else:
                        iteracionesIncorrectas+=1
                except:
                    iteracionesIncorrectas+=1
                    pass

#NuSVR
for kernel in ['rbf', 'linear', 'poly', 'sigmoid', 'precomputed']:
    for nu in [0.01, 0.05, 0.1, 0.5]:
        for degree in range(3, 15):
            try:
                gamma= 0.001
                nuSVM = NuSVR.NuSVRModel(data, targResponse, kernel, degree, gamma, nu)
                nuSVM.trainingMethod()

                performanceValues = performanceData.performancePrediction(targResponse, nuSVM.predicctions.tolist())
                pearsonValue = performanceValues.calculatedPearson()['pearsonr']
                spearmanValue = performanceValues.calculatedSpearman()['spearmanr']
                kendalltauValue = performanceValues.calculatekendalltau()['kendalltau']
                if (pearsonValue!= "ERROR" and spearmanValue != "ERROR" and kendalltauValue != "ERROR" and nuSVM.r_score != "ERROR"):
                    params = "kernel:%s-nu:%f-degree:%d-gamma:%f" % (kernel, nu, degree, gamma)
                    print params
                    row = ["NuSVM", params, nuSVM.r_score, pearsonValue, spearmanValue, kendalltauValue]
                    matrixResponse.append(row)
                    iteracionesCorrectas+=1
                else:
                    iteracionesIncorrectas+=1
            except:
                iteracionesIncorrectas+=1
                pass

#SVC
for kernel in ['rbf', 'linear', 'poly', 'sigmoid', 'precomputed']:
    for degree in range(3, 15):
        for gamma in [0.01, 0.1, 1]:
            try:
                print "Excec SVM"
                svm = SVR.SVRModel(data, targResponse, kernel, degree, gamma)
                svm.trainingMethod()

                performanceValues = performanceData.performancePrediction(targResponse, svm.predicctions.tolist())
                pearsonValue = performanceValues.calculatedPearson()['pearsonr']
                spearmanValue = performanceValues.calculatedSpearman()['spearmanr']
                kendalltauValue = performanceValues.calculatekendalltau()['kendalltau']

                if (pearsonValue!= "ERROR" and spearmanValue != "ERROR" and kendalltauValue != "ERROR" and svm.r_score != "ERROR"):
                    params = "kernel:%s-degree:%d-gamma:%f" % (kernel, degree, gamma)
                    row = ["SVM", params, svm.r_score, pearsonValue, spearmanValue, kendalltauValue]
                    matrixResponse.append(row)
                    iteracionesCorrectas+=1
                else:
                    iteracionesIncorrectas+=1
            except:
                iteracionesIncorrectas+=1
                pass

#RF
for n_estimators in [10,50,100,200,500,1000,1500,2000]:
    for criterion in ['mse', 'mae']:
        for bootstrap in [True, False]:
            try:
                min_samples_leaf=1
                min_samples_split=2
                print "Excec RF"
                rf = RandomForest.RandomForest(data, targResponse, n_estimators, criterion, min_samples_split, min_samples_leaf, bootstrap)
                rf.trainingMethod()

                performanceValues = performanceData.performancePrediction(targResponse, rf.predicctions.tolist())
                pearsonValue = performanceValues.calculatedPearson()['pearsonr']
                spearmanValue = performanceValues.calculatedSpearman()['spearmanr']
                kendalltauValue = performanceValues.calculatekendalltau()['kendalltau']

                if (pearsonValue!= "ERROR" and spearmanValue != "ERROR" and kendalltauValue != "ERROR" and rf.r_score != "ERROR"):
                    params = "n_estimators:%d-criterion:%s-min_samples_split:%d-min_samples_leaf:%d-bootstrap:%s" % (n_estimators, criterion, min_samples_split, min_samples_leaf, str(bootstrap))
                    row = ["RandomForestRegressor", params, rf.r_score, pearsonValue, spearmanValue, kendalltauValue]
                    matrixResponse.append(row)
                    iteracionesCorrectas+=1
                else:
                    iteracionesIncorrectas+=1
            except:
                iteracionesIncorrectas+=1
                pass

#generamos el export de la matriz convirtiendo a data frame
dataFrame = pd.DataFrame(matrixResponse, columns=header)

#generamos el nombre del archivo
nameFileExport = "%s/summaryProcessJob_%s.csv" % (pathResponse, job)
dataFrame.to_csv(nameFileExport, index=False)

#estimamos los estadisticos resumenes para cada columna en el header
#instanciamos el object
statisticObject = summaryStatistic.createStatisticSummary(nameFileExport)
matrixSummaryStatistic = []

#"Accuracy", "Recall", "Precision", "Neg_log_loss", "F1", "FBeta"
matrixSummaryStatistic.append(estimatedStatisticPerformance(statisticObject, 'R_Score'))

#generamos el nombre del archivo
dataFrame = pd.DataFrame(matrixSummaryStatistic, columns=['Performance','Mean', 'STD', 'Variance', 'MAX', 'MIN'])
nameFileExport = "%s/statisticPerformance_%s.csv" % (pathResponse, job)
dataFrame.to_csv(nameFileExport, index=False)

#cambiamos el estado al job
connectDB = ConnectDataBase.ConnectDataBase()
handler = HandlerQuery.HandlerQuery()

#hacemos la consulta
query = "update jobData set jobData.statusJob = 'FINISH', jobData.dateFinish= NOW() where jobData.idjobData=%s" % job

connectDB.initConnectionDB()
handler.insertToTable(query, connectDB)
connectDB.closeConnectionDB()

finishTime = time.time() - start_time
termino = datetime.datetime.now()

dictionary = {}
dictionary.update({"inicio": str(inicio)})
dictionary.update({"termino": str(termino)})
dictionary.update({"ejecucion": finishTime})
dictionary.update({"job": job})
dictionary.update({"iteracionesCorrectas": iteracionesCorrectas})
dictionary.update({"iteracionesIncorrectas": iteracionesIncorrectas})

nameFileExport = "%s/summaryProcess_%s.json" % (pathResponse, job)
with open(nameFileExport, 'w') as fp:
    json.dump(dictionary, fp)

nameFileExportCSV = "%s/summaryProcessJob_%s.csv" % (pathResponse, job)
pathResponseExport = pathResponse

print pathResponseExport
print dataSetNameInput
completeProcess(nameFileExportCSV, pathResponseExport, dataSetNameInput, featureResponse)

#enviar correo con finalizacion del job....
body = "Dear User.\nThe job with ID: %s has been update to status: FINISH.\nBest Regards, SmartTraining Team" % (job)
emailData = sendEmail.sendEmail('smarttrainingserviceteam@gmail.com', emailUser, "Change status in job "+ str(job), body, 'smart123ewq')
emailData.sendEmailUser()
