'''
clase que tiene la responsabilidad de revisar si existen jobs en cola, en caso de que existan, los ejecuta y cambia
el estado del job a procesando, ademas... cuando el job se ejecuta se notifica via correo electronico que el job
cambio de estado
'''

from mls_models.dataBase_module import ConnectDataBase
from mls_models.dataBase_module import HandlerQuery
from mls_models.utils import sendEmail
import os

class checkJobs(object):

    def __init__(self):

        #hacemos las instancias de conexion y handler de la bd
        self.connect = ConnectDataBase.ConnectDataBase()
        self.handler = HandlerQuery.HandlerQuery()

    #metodo que permite obtener los jobs en estado init...
    def getJobsInit(self):

        self.connect.initConnectionDB()
        query = "select jobData.idjobData from jobData where jobData.statusJob = 'START'"
        listResponse = self.handler.queryBasicDataBase(query, self.connect)

        self.listJobs = []
        for element in listResponse:
            self.listJobs.append(element[0])

        self.connect.closeConnectionDB()

    #metodo que permite obtener la informacion del usuario...
    def getUserInfoByJob(self, jobID):

        query = "select jobData.mailUser, jobData.kind from jobData where jobData.idjobData = %s" % jobID
        self.connect.initConnectionDB()
        listResponse = self.handler.queryBasicDataBase(query, self.connect)

        self.connect.closeConnectionDB()
        return str(listResponse[0][0]), str(listResponse[0][1])#retornamos el mail y el tipo job

    #metodo que permite obtener el nombre del set de datos...
    def getNameDataSet(self, job):

        query = "select jobData.nameDoc from jobData where jobData.idjobData = %s" %job
        self.connect.initConnectionDB()
        listResponse = self.handler.queryBasicDataBase(query, self.connect)

        self.connect.closeConnectionDB()
        return listResponse[0][0]#retornamos el nombre del set de datos

    #metodo que permite obtener el nombre de la feature de respuesta en el set de datos
    def getFeatureResponse(self, job):

        query = "select response.nameFeature from response where response.dataSet = %s" %job
        self.connect.initConnectionDB()
        listResponse = self.handler.queryBasicDataBase(query, self.connect)

        self.connect.closeConnectionDB()
        return listResponse[0][0]#retornamos la caracteristica respuesta

    #metodo que permite obtener el valor del procesamiento a la respuesta
    def getValuesProcessResponse(self, job):

        query = "select response.removeElements from response where response.dataSet = %s" %job
        self.connect.initConnectionDB()
        listResponse = self.handler.queryBasicDataBase(query, self.connect)

        self.connect.closeConnectionDB()
        return listResponse[0][0]#retornamos la caracteristica respuesta

    #metodo que permite recibir un job y hacer la ejecucion del job, cambia estado y notifica el cambio via correo electronico
    def execJob(self, job):

        nameDataset = self.getNameDataSet(job)
        emailUser, tipo_job = self.getUserInfoByJob(job)
        featureResponse = self.getFeatureResponse(job)
        removeElements = self.getValuesProcessResponse(job)

        #hacemos la actualizacion del job en el servidor
        query = "update jobData set jobData.statusJob = 'PROCESSING', jobData.dateFinish=NOW() where jobData.idjobData = %s" % job
        self.connect.initConnectionDB()
        self.handler.insertToTable(query, self.connect)

        #hacemos la notificacion al usuario...
        body = "Dear User MLSTraining Tool.\nThe job with ID: %s has been update to status: PROCESSING. It will notify by email when job finish.\nBest Regards, MLSTraining Team" % (job)
        emailData = sendEmail.sendEmail('smarttrainingserviceteam@gmail.com', emailUser, "Change status in job "+ str(job), body, 'smart123ewq')
        emailData.sendEmailUser()
        self.connect.closeConnectionDB()

        dataSet = "/var/www/html/MLSTrainingTool/jobs/%s/%s" % (job, nameDataset)
        if tipo_job == "PREDICTION":#prediction launcher

            command = "python /var/www/html/MLSTrainingTool/models/bin/launcherFullProcessPrediction.py %s %s %s /var/www/html/MLSTrainingTool/jobs/ %s %s &" % (emailUser, job, dataSet, featureResponse, removeElements)
            #os.system(command)
            print command
        else:#classification launcher
            command = "python /var/www/html/MLSTrainingTool/models/bin/launcherFullProcessClassification.py %s %s %s /var/www/html/MLSTrainingTool/jobs/ %s %s &" % (emailUser, job, dataSet, featureResponse, removeElements)
            #os.system(command)
            print command
