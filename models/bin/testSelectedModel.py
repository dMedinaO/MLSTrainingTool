import pandas as pd
import sys

from mls_models.utils import selectorModels
from mls_models.utils import joinModels

dataSet = pd.read_csv(sys.argv[1])
listKey = ['Accuracy', 'Recall', 'Precision', 'F1']
otherKeys = ['Algorithm', 'Params', 'Validation']
modelSelecter = selectorModels.selectedModel(dataSet, sys.argv[2], listKey, otherKeys)
dataSetsSelected = []

for i in range(len(listKey)):
    modelSelecter.selectedModelData(modelSelecter.meanData[i], modelSelecter.stdData[i], listKey[i])
    dataSetsSelected.append(modelSelecter.dataFrame)

#testeamos la union de modelos
joinModelsObject = joinModels.joinModels(dataSetsSelected[0], dataSetsSelected[1], dataSetsSelected[2], dataSetsSelected[3], listKey, sys.argv[2])
joinModelsObject.joinAndGetUnique()
