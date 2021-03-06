########################################################################
# Copyright (C) 2019  David Medina Ortiz, david.medina@cebib.cl
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
########################################################################

import sys
import pandas as pd
import argparse

from modulesNLM.utils import createDataSetForTraining

#utils para el manejo de set de datos y su normalizacion
from modulesNLM.utils import transformDataClass
from modulesNLM.utils import transformFrequence
from modulesNLM.utils import ScaleNormalScore
from modulesNLM.utils import ScaleMinMax
from modulesNLM.utils import ScaleDataSetLog
from modulesNLM.utils import ScaleLogNormalScore
from modulesNLM.utils import summaryScanProcess
from modulesNLM.utils import responseResults
from modulesNLM.utils import encodingFeatures

parser.add_argument("-d", "--dataSet", help="full path and name to acces dataSet input process", required=True)
parser.add_argument("-p", "--pathResult", help="full path for save results", required=True)
parser.add_argument("-r", "--response", help="name of column with response values in dataset", required=True)

args = parser.parse_args()

#recibimos los parametros desde la terminal...
dataSet = pd.read_csv(args.dataSet)
pathResponse = args.pathResult
response = args.response

transformData = transformDataClass.transformClass(target)
target = transformData.transformData

#ahora transformamos el set de datos por si existen elementos categoricos...
#transformDataSet = transformFrequence.frequenceData(data)
#dataSetNewFreq = transformDataSet.dataTransform
encoding = encodingFeatures.encodingFeatures(dataSet, 20)
encoding.evaluEncoderKind()
dataSetNewFreq = encoding.dataSet
#ahora aplicamos el procesamiento segun lo expuesto
applyNormal = ScaleNormalScore.applyNormalScale(dataSetNewFreq)
data = applyNormal.dataTransform

#obtenemos el dataset de entrenamiento y validacion, junto con los arreglos correspondientes de respuestas
getDataProcess = createDataSetForTraining.createDataSet(data, target)
dataSetTraining = getDataProcess.dataSetTraining
classTraining =  getDataProcess.classTraining

dataSetTesting = getDataProcess.dataSetTesting
classTesting = getDataProcess.classTesting

#export training and testing to csv files
