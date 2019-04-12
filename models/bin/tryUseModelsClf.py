'''
script que permite el uso de los modelos de prediccion para un trabajo
ya generado
'''

import sys
from mls_models.utils import useSelectedModelClfTry

#recibimos la data de interes
dataSet = sys.argv[1]#entrenamiento
dataSetNew = sys.argv[2]#ejemplos
metaModels = sys.argv[3]#modelos
pathResponse = sys.argv[4]#path result

#instancia al objeto
tryModel = useSelectedModelClfTry.useSelectedModels(dataSet, dataSetNew, metaModels, pathResponse)
tryModel.applyModelsSelected()
