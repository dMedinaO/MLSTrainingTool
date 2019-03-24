from distutils.core import setup
import ConfigParser
import os

class SetupConfiguration:

    def __init__(self):

        self.setupInstall()

    def setupInstall(self):

        setup(name='mlsTrainingTool',
            version='alpha',
            description='Meta Learning System Training',
            author='David Medina',
            author_email='david.medina@cebib.cl',
            license='Open GPL 3',
            packages=['mls_models', 'mls_models.checks_module', 'mls_models.supervised_learning_clf', 'mls_models.dataBase_module', 'mls_models.supervised_learning_predicction', 'mls_models.utils', 'mls_models.statistics_analysis'],)

def main():

    setup = SetupConfiguration()
    return 0

if __name__ == '__main__':
    main()
