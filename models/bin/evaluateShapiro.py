'''
script que permite hacer la prueba de shapiro sobre un set de datos
'''

import pandas as pd
import numpy as np
import sys
import json
from scipy import stats

dataSet = pd.read_csv(sys.argv[1])
feature = sys.argv[2]

dataValues = dataSet[feature]

#evaluamos shapiro
response = stats.shapiro(dataValues)
dictResponse = {'statistic':response[0], 'pvalue':response[1]}

#obtenemos la cantidad de outliers existentes en la respuesta
outliers = []
threshold=3
mean_1 = np.mean(dataValues)
std_1 =np.std(dataValues)

for y in dataValues:
    z_score= (y - mean_1)/std_1
    if np.abs(z_score) > threshold:
        outliers.append(y)

dictResponse.update({'outliers':len(outliers)})
        
print json.dumps(dictResponse)
