import pandas as pd
import sys

from mls_models.utils import selectorModels

dataSet = pd.read_csv(sys.argv[1])
listKey = ['Accuracy', 'Recall', 'Precision', 'F1']
otherKeys = ['Algorithm', 'Params', 'Validation']
modelSelecter = selectorModels.selectedModel(dataSet, sys.argv[2], listKey, otherKeys)

for i in range(len(listKey)):
    modelSelecter.selectedModelData(modelSelecter.meanData[i], modelSelecter.stdData[i], listKey[i])
