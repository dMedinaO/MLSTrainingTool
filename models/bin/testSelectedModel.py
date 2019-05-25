import pandas as pd
import sys

from mls_models.utils import selectorModels
from mls_models.utils import joinModels
from mls_models.utils import makeworld_cloud
from mls_models.utils import makeDiagrammRepresent
from mls_models.utils import getPerformanceModel
from mls_models.utils import exportMetaModel
from mls_models.utils import useSelectedModelClf
from sklearn.model_selection import LeaveOneOut

dataSet = pd.read_csv(sys.argv[1])
listKey = ['Accuracy_MAX','recall_MAX','precision_MAX']
otherKeys = ['algorithm', 'description', 'validation']
modelSelecter = selectorModels.selectedModel(dataSet, sys.argv[2], listKey, otherKeys)
dataSetsSelected = []

for i in range(len(listKey)):
    modelSelecter.selectedModelData(modelSelecter.meanData[i], modelSelecter.stdData[i], listKey[i])
    dataSetsSelected.append(modelSelecter.dataFrame)


#testeamos la generacion del wordcloud
makeWord = makeworld_cloud.createWorldCloud(dataSetsSelected[0], dataSetsSelected[1], dataSetsSelected[2], sys.argv[2])
makeWord.createGraphic()

#testeamos la generacion de la data para el grafico de valores anidados
makeDiagram = makeDiagrammRepresent.defineViewDiagram(dataSetsSelected[0], dataSetsSelected[1], dataSetsSelected[2], listKey, sys.argv[2])
makeDiagram.formatResponse()

'''
#testeamos la generacion del archivo de meta modelos
exportModel = exportMetaModel.exportMetaModel(dataSetsSelected[0], dataSetsSelected[1], dataSetsSelected[2], dataSetsSelected[3], sys.argv[2])
exportModel.getUniqueModels()
'''

#usamos el meta modelo para obtener las medidas de desempeno
modelsMeta = useSelectedModelClf.useSelectedModels(sys.argv[3], sys.argv[2]+"meta_models.json", sys.argv[2], 5)
modelsMeta.applyModelsSelected()
