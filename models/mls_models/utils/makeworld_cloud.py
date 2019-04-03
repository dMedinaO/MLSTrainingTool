'''
script que permite crear un worldcloud a partir de los set de datos que se generaron con respecto a las matrices expuestas
retorna una imagen asociada al grafico generado y se almacena en la ruta del job
'''

import pandas as pd
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

class createWorldCloud(object):

    def __init__(self, dataSet1, dataSet2, dataSet3, dataSet4, pathOutput):

        self.dataSet1 = dataSet1
        self.dataSet2 = dataSet2
        self.dataSet3 = dataSet3
        self.dataSet4 = dataSet4
        self.pathOutput = pathOutput

    #formamos la lista con todos los elementos
    def createList(self, listData):

        commentwords = ""

        for element in listData:
            commentwords = commentwords + element + " "

        return commentwords

    #metodo que permite crear el worldcloud
    def createGraphic(self):

        commentwords1 = self.createList(self.dataSet1['Algorithm'])
        commentwords2 = self.createList(self.dataSet2['Algorithm'])
        commentwords3 = self.createList(self.dataSet3['Algorithm'])
        commentwords4 = self.createList(self.dataSet4['Algorithm'])

        commentData = commentwords1 + commentwords2 + commentwords3 + commentwords4
        wordcloud = WordCloud(width = 800, height = 400,background_color ='white',min_font_size = 10).generate(commentData)
        plt.figure(figsize = (8, 4), facecolor = None)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.tight_layout(pad = 0)

        plt.savefig(self.pathOutput+"world_cloud.svg")
