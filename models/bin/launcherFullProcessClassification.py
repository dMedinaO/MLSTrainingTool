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

from mls_models.utils import selectorModels
from mls_models.utils import joinModels
from mls_models.utils import makeworld_cloud
from mls_models.utils import makeDiagrammRepresent
from mls_models.utils import getPerformanceModel
from mls_models.utils import exportMetaModel
from mls_models.utils import useSelectedModelClf
from mls_models.utils import encodingFeatures
from sklearn.model_selection import LeaveOneOut
from mls_models.utils import encodingFeatures
from imblearn.over_sampling import SMOTE, ADASYN

#funcion para completar el proceso de la informacion correspondiente a la data empleada y permite crear los graficos para la vista en web
def completeProcess(dataSetName, pathResponse, dataSetOriginal, cvValue, featureResponse):

    dataSet = pd.read_csv(dataSetName)
    listKey = ['Accuracy','Recall','Precision','F1']
    otherKeys = ['Algorithm', 'Params', 'Validation']
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
    modelsMeta = useSelectedModelClf.useSelectedModels(dataSetOriginal, pathResponse+"meta_models.json", pathResponse, cvValue, featureResponse)
    modelsMeta.applyModelsSelected()


#funcion que permite calcular los estadisticos de un atributo en el set de datos, asociados a las medidas de desempeno
def estimatedStatisticPerformance(summaryObject, attribute):

    statistic = summaryObject.calculateValuesForColumn(attribute)
    row = [attribute, statistic['mean'], statistic['std'], statistic['var'], statistic['max'], statistic['min']]

    return row

#funcion que permite estimar el valor de validacion cruzada a ser utilizado dependiendo del tamano de los set de datos
def checkCrossValidationKValues(numberExamples):

    response = ""
    cvValue = 0

    if (numberExamples<=20):
        cvValue = LeaveOneOut()
        response = "CV-LeaveOneOut"
    elif numberExamples>20 and numberExamples<=50:
        cvValue = 3
        response = "CV-3"
    elif numberExamples>50 and numberExamples<=100:
        cvValue = 5
        response = "CV-5"
    else:
        cvValue = 10
        response = "CV-10"

    return response, cvValue

#recibimos los parametros desde la terminal...
emailUser = sys.argv[1]
job = sys.argv[2]
dataSetNameInput = sys.argv[3]
dataSet = pd.read_csv(sys.argv[3])
pathResponse = sys.argv[4]
featureResponse = sys.argv[5]
removeInbalance = int(sys.argv[6])

#valores iniciales
start_time = time.time()
inicio = datetime.datetime.now()
iteracionesCorrectas = 0
iteracionesIncorrectas = 0

#procesamos el set de datos para obtener los atributos y las clases...
targetResponse=dataSet[featureResponse]#clases

#generamos una copia y eliminamos la respuesta de los atributos
dataValues = dataSet
del dataValues[featureResponse]

#transformamos la clase si presenta atributos categoricos
transformData = transformDataClass.transformClass(targetResponse)
target = transformData.transformData
dictTransform = transformData.dictTransform
classArray = list(set(target))#evaluamos si es arreglo binario o no

kindDataSet = 1

if len(classArray) ==2:
    kindDataSet =1
else:
    kindDataSet =2


listFeatures = list(dataValues.keys())

#generamos la codificacion
encoding = encodingFeatures.encodingFeatures(dataValues, 20)
encoding.evaluEncoderKind()
dataEncoding = encoding.dataSet

#preguntamos por el manejo de desbalance de clases
if removeInbalance == 2:
    dataEncoding, target = SMOTE().fit_resample(dataEncoding, target)

    #transformamos los valores a dataFrame
    dataEncoding = pd.DataFrame(dataEncoding, columns=listFeatures)

#aplicamos la normalizacion
applyNormal = ScaleNormalScore.applyNormalScale(dataEncoding)
data = applyNormal.dataTransform

#obtenemos la validacion y el string para formar la respuesta
responseString, cvValue = checkCrossValidationKValues(len(data))

#generamos una lista con los valores obtenidos...
header = ["Algorithm", "Params", "Validation", "Accuracy", "Recall", "Precision", "F1"]
matrixResponse = []

#comenzamos con las ejecuciones...
#AdaBoost
for algorithm in ['SAMME', 'SAMME.R']:
    for n_estimators in [10,50,100,200,500,1000,1500,2000]:
        try:
            print "Excec AdaBoost with %s - %d" % (algorithm, n_estimators)
            AdaBoostObject = AdaBoost.AdaBoost(data, target, n_estimators, algorithm, cvValue)
            AdaBoostObject.trainingMethod(kindDataSet)
            params = "Algorithm:%s-n_estimators:%d" % (algorithm, n_estimators)
            row = ["AdaBoostClassifier", params, responseString, AdaBoostObject.performanceData.scoreData[3], AdaBoostObject.performanceData.scoreData[4], AdaBoostObject.performanceData.scoreData[5], AdaBoostObject.performanceData.scoreData[6]]
            matrixResponse.append(row)
            iteracionesCorrectas+=1

        except:
            iteracionesIncorrectas+=1
            pass
#Baggin
for bootstrap in [True, False]:
    for n_estimators in [10,50,100,200,500,1000,1500,2000]:
        try:
            print "Excec Bagging with %s - %d" % (bootstrap, n_estimators)
            bagginObject = Baggin.Baggin(data,target,n_estimators, bootstrap,cvValue)
            bagginObject.trainingMethod(kindDataSet)
            params = "bootstrap:%s-n_estimators:%d" % (str(bootstrap), n_estimators)
            row = ["Bagging", params, responseString, bagginObject.performanceData.scoreData[3], bagginObject.performanceData.scoreData[4], bagginObject.performanceData.scoreData[5], bagginObject.performanceData.scoreData[6]]
            matrixResponse.append(row)
            iteracionesCorrectas+=1
            break
        except:
            iteracionesIncorrectas+=1
            pass

#BernoulliNB
try:
    bernoulliNB = BernoulliNB.Bernoulli(data, target, cvValue)
    bernoulliNB.trainingMethod(kindDataSet)
    print "Excec Bernoulli Default Params"
    params = "Default"
    row = ["BernoulliNB", params, responseString, bernoulliNB.performanceData.scoreData[3], bernoulliNB.performanceData.scoreData[4], bernoulliNB.performanceData.scoreData[5], bernoulliNB.performanceData.scoreData[6]]
    matrixResponse.append(row)
    iteracionesCorrectas+=1
except:
    iteracionesIncorrectas+=1
    pass


#DecisionTree
for criterion in ['gini', 'entropy']:
    for splitter in ['best', 'random']:
        try:
            print "Excec DecisionTree with %s - %s" % (criterion, splitter)
            decisionTreeObject = DecisionTree.DecisionTree(data, target, criterion, splitter, cvValue)
            decisionTreeObject.trainingMethod(kindDataSet)
            params = "criterion:%s-splitter:%s" % (criterion, splitter)
            row = ["DecisionTree", params, responseString, decisionTreeObject.performanceData.scoreData[3], decisionTreeObject.performanceData.scoreData[4], decisionTreeObject.performanceData.scoreData[5], decisionTreeObject.performanceData.scoreData[6]]
            matrixResponse.append(row)
            iteracionesCorrectas+=1
        except:
            iteracionesIncorrectas+=1
            pass

try:
    #GaussianNB
    gaussianObject = GaussianNB.Gaussian(data, target, cvValue)
    gaussianObject.trainingMethod(kindDataSet)
    print "Excec GaussianNB Default Params"
    params = "Default"

    row = ["GaussianNB", params, responseString, gaussianObject.performanceData.scoreData[3], gaussianObject.performanceData.scoreData[4], gaussianObject.performanceData.scoreData[5], gaussianObject.performanceData.scoreData[6]]
    matrixResponse.append(row)
except:
    pass

#gradiente
for loss in ['deviance', 'exponential']:
    for n_estimators in [10,50,100,200,500,1000,1500,2000]:
        try:
            print "Excec GradientBoostingClassifier with %s - %d - %d - %d" % (loss, n_estimators, 2, 1)
            gradientObject = Gradient.Gradient(data,target,n_estimators, loss, 2, 1, cvValue)
            gradientObject.trainingMethod(kindDataSet)
            params = "n_estimators:%d-loss:%s-min_samples_split:%d-min_samples_leaf:%d" % (n_estimators, loss, 2, 1)
            row = ["GradientBoostingClassifier", params, responseString, gradientObject.performanceData.scoreData[3], gradientObject.performanceData.scoreData[4], gradientObject.performanceData.scoreData[5], gradientObject.performanceData.scoreData[6]]
            matrixResponse.append(row)
            iteracionesCorrectas+=1
        except:
            iteracionesIncorrectas+=1
            pass

#knn
for n_neighbors in range(1,11):
    for algorithm in ['auto', 'ball_tree', 'kd_tree', 'brute']:
        for metric in ['minkowski', 'euclidean']:
            for weights in ['uniform', 'distance']:
                try:
                    print "Excec KNeighborsClassifier with %d - %s - %s - %s" % (n_neighbors, algorithm, metric, weights)
                    knnObect = knn.knn(data, target, n_neighbors, algorithm, metric,  weights,cvValue)
                    knnObect.trainingMethod(kindDataSet)

                    params = "n_neighbors:%d-algorithm:%s-metric:%s-weights:%s" % (n_neighbors, algorithm, metric, weights)
                    row = ["KNeighborsClassifier", params, responseString, knnObect.performanceData.scoreData[3], knnObect.performanceData.scoreData[4], knnObect.performanceData.scoreData[5], knnObect.performanceData.scoreData[6]]
                    matrixResponse.append(row)
                    iteracionesCorrectas+=1
                except:
                    iteracionesIncorrectas+=1
                    pass

#NuSVC
for kernel in ['rbf', 'linear', 'poly', 'sigmoid', 'precomputed']:
    for nu in [0.01, 0.05, 0.1, 0.5]:
        for degree in range(3, 15):
            try:
                print "Excec NuSVM"
                nuSVM = NuSVM.NuSVM(data, target, kernel, nu, degree, 0.01, cvValue)
                nuSVM.trainingMethod(kindDataSet)
                params = "kernel:%s-nu:%f-degree:%d-gamma:%f" % (kernel, nu, degree, 0.001)
                row = ["NuSVM", params, responseString, nuSVM.performanceData.scoreData[3], nuSVM.performanceData.scoreData[4], nuSVM.performanceData.scoreData[5], nuSVM.performanceData.scoreData[6]]
                matrixResponse.append(row)
                iteracionesCorrectas+=1
            except:
                iteracionesIncorrectas+=1
                pass

#SVC
for kernel in ['rbf', 'linear', 'poly', 'sigmoid', 'precomputed']:
    for C_value in [0.01, 0.05, 0.1, 0.5]:
        for degree in range(3, 15):
            try:
                print "Excec SVM"
                svm = SVM.SVM(data, target, kernel, C_value, degree, 0.01, cvValue)
                svm.trainingMethod(kindDataSet)
                params = "kernel:%s-c:%f-degree:%d-gamma:%f" % (kernel, C_value, degree, 0.001)
                row = ["SVM", params, responseString, svm.performanceData.scoreData[3], svm.performanceData.scoreData[4], svm.performanceData.scoreData[5], svm.performanceData.scoreData[6]]
                matrixResponse.append(row)
                iteracionesCorrectas+=1
            except:
                iteracionesIncorrectas+=1
                pass

#RF
for n_estimators in [10,50,100,200,500,1000,1500,2000]:
    for criterion in ['gini', 'entropy']:
        for bootstrap in [True, False]:
            try:
                print "Excec RF"
                rf = RandomForest.RandomForest(data, target, n_estimators, criterion, 2, 1, bootstrap, cvValue)
                rf.trainingMethod(kindDataSet)

                params = "n_estimators:%d-criterion:%s-min_samples_split:%d-min_samples_leaf:%d-bootstrap:%s" % (n_estimators, criterion, 2, 1, str(bootstrap))
                row = ["RandomForestClassifier", params, responseString, rf.performanceData.scoreData[3], rf.performanceData.scoreData[4], rf.performanceData.scoreData[5], rf.performanceData.scoreData[6]]
                matrixResponse.append(row)
                iteracionesCorrectas+=1
            except:
                iteracionesIncorrectas+=1
                pass

#generamos el export de la matriz convirtiendo a data frame
dataFrame = pd.DataFrame(matrixResponse, columns=header)

#generamos el nombre del archivo
nameFileExport = "%s%s/summaryProcessJob_%s.csv" % (pathResponse, job, job)
dataFrame.to_csv(nameFileExport, index=False)

#estimamos los estadisticos resumenes para cada columna en el header
#instanciamos el object
statisticObject = summaryStatistic.createStatisticSummary(nameFileExport)
matrixSummaryStatistic = []

#"Accuracy", "Recall", "Precision", "Neg_log_loss", "F1", "FBeta"
matrixSummaryStatistic.append(estimatedStatisticPerformance(statisticObject, 'Accuracy'))
matrixSummaryStatistic.append(estimatedStatisticPerformance(statisticObject, 'Recall'))
matrixSummaryStatistic.append(estimatedStatisticPerformance(statisticObject, 'Precision'))
matrixSummaryStatistic.append(estimatedStatisticPerformance(statisticObject, 'F1'))

#generamos el nombre del archivo
dataFrame = pd.DataFrame(matrixSummaryStatistic, columns=['Performance','Mean', 'STD', 'Variance', 'MAX', 'MIN'])
nameFileExport = "%s%s/statisticPerformance_%s.csv" % (pathResponse, job, job)
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

nameFileExport = "%s%s/summaryProcess_%s.json" % (pathResponse, job, job)
nameFileExportCSV = "%s%s/summaryProcessJob_%s.csv" % (pathResponse, job, job)

with open(nameFileExport, 'w') as fp:
    json.dump(dictionary, fp)

pathResponseExport = pathResponse+job+"/"
completeProcess(nameFileExportCSV, pathResponseExport, dataSetNameInput, cvValue, featureResponse)

#enviar correo con finalizacion del job....
body = "Dear User.\nThe job with ID: %s has been update to status: FINISH.\nBest Regards, SmartTraining Team" % (job)
emailData = sendEmail.sendEmail('smarttrainingserviceteam@gmail.com', emailUser, "Change status in job "+ str(job), body, 'smart123ewq')
emailData.sendEmailUser()
