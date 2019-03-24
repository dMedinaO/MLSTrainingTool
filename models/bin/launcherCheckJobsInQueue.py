'''
script que permite revisar los procesos en cola y ejecutarlos
'''

from mls_models.checks_module import checksJobInQueue

#instancia al objeto
checkObject = checksJobInQueue.checkJobs()
checkObject.getJobsInit()#obtenemos los jobs

for job in checkObject.listJobs:
    checkObject.execJob(job)
