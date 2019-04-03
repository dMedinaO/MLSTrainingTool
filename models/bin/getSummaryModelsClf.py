'''
script que permite leer los archivos csv y obtener la informacion asociada a cada elemento
genera un json como respuesta
'''

import pandas as pd
import json
import sys

job = sys.argv[1]

pathResponse = "/var/www/html/MLSTrainingTool/jobs/"

#leemos los archivos...
pdPrecision = pd.read_csv(pathResponse+job+"/Precision.csv")
pdAccuracy = pd.read_csv(pathResponse+job+"/Accuracy.csv")
pdRecall = pd.read_csv(pathResponse+job+"/Recall.csv")
pdF1 = pd.read_csv(pathResponse+job+"/F1.csv")

dictResponse1 = {"values": len(pdPrecision), "performance": "Precision"}
dictResponse2 = {"values": len(pdAccuracy), "performance": "Accuracy"}
dictResponse3 = {"values": len(pdRecall), "performance": "Recall"}
dictResponse4 = {"values": len(pdF1), "performance": "F1"}

response = [dictResponse1, dictResponse2, dictResponse3, dictResponse4]
print json.dumps(response)
