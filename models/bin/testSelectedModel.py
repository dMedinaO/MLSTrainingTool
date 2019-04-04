import pandas as pd
import sys

from mls_models.utils import selectorModels
from mls_models.utils import joinModels
from mls_models.utils import makeworld_cloud
from mls_models.utils import makeDiagrammRepresent
from mls_models.utils import getPerformanceModel

dataSet = pd.read_csv(sys.argv[1])
listKey = ['R_Score','Pearson','Spearman','Kendalltau']
otherKeys = ['Algorithm', 'Params']
modelSelecter = selectorModels.selectedModel(dataSet, sys.argv[2], listKey, otherKeys)
dataSetsSelected = []

for i in range(len(listKey)):
    modelSelecter.selectedModelData(modelSelecter.meanData[i], modelSelecter.stdData[i], listKey[i])
    dataSetsSelected.append(modelSelecter.dataFrame)

#testeamos la union de modelos
joinModelsObject = joinModels.joinModels(dataSetsSelected[0], dataSetsSelected[1], dataSetsSelected[2], dataSetsSelected[3], listKey, sys.argv[2])
joinModelsObject.joinAndGetUnique()

#testeamos la generacion del wordcloud
makeWord = makeworld_cloud.createWorldCloud(dataSetsSelected[0], dataSetsSelected[1], dataSetsSelected[2], dataSetsSelected[3], sys.argv[2])
makeWord.createGraphic()

#testeamos la generacion de la data para el grafico de valores anidados
makeDiagram = makeDiagrammRepresent.defineViewDiagram(dataSetsSelected[0], dataSetsSelected[1], dataSetsSelected[2], dataSetsSelected[3], listKey, sys.argv[2])
makeDiagram.formatResponse()

#testeamos la generacion de las medidas de desempeno del modelo de meta learning
performancePond = getPerformanceModel.ponderatedModelPerformance(dataSetsSelected[0], dataSetsSelected[1], dataSetsSelected[2], dataSetsSelected[3], listKey, sys.argv[2])
performancePond.getMeanValuesPerformance()
