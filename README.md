## README

MLS Training is a web tool which facilitates the training of classification or regression models by means of supervised learning algorithms.

# Inputs

CSV file with examples whose response is known. If the answer is of the discrete distribution type or letters, classification models will be trained, otherwise, if the answer belongs to the continuous domain, regression models will be trained.

# Preparation of the data set

The tool prepares the data set by removing null elements or empty columns. In a second instance, Pears criteria are applied to eliminate outliers within the sample, which alter the homogeneity of the data. After that, it normalizes the data applying a normalization based on selection according to the distribution of the data, for this, it uses statistical criteria based on the Shapiro test, if the results indicate that the data presents normal distribution, a Z-score is applied or a logarithmic Z-score to the data to generate said process, otherwise, maximum and minimum distributions or spatial transformations based on logarithmic distributions in base two are applied.

Given the above, the data set is ready to be processed by the model scanning and selection tool.

# Training algorithm

MLS Training has a training model based on the development of meta-learning systems and the use of statistical techniques to develop weighted performance measures of the models and determine the performance to be obtained for the use of these models in the face of new examples.

# Training Stages

There are 3 main stages in training, which are explained below.

## Massive training

The same data set is subjected to training by applying different supervised learning algorithms, which vary depending on the type of response that the data set has. Within the algorithms, we find those based on sample distances, others applying regressions to data and vector transformations to generate hyperplanes, while some take advantage of the spatial characteristics of the elements and others develop structures around capable of generating Deep Learning. In this stage, about 1,600 models are iterated, with different algorithms and variations of their parameters, generating a csv file with the summary of this process.

## Selection of Models

The selection of models is based on the application of statistical tests that allow the identification of positive outliers points within the sample, for which different performance measures are considered depending on the model. Precision, Accuracy, Recall and F1 for classification models and Pearson, R score, Spearman and Kendall Tau for regression models.

Each distribution of performance measures is applied to this statistical test consulted by the models with values on 3 standard deviations of the sample, if they do not exist, it is continued with 2 deviations and finally 1.5 above the average, in case of not fulfilling any criterion, the models with the maximum value in said performance are selected.

At the end of this stage there is a list of models with their parameters for each measurement, which are the inputs for the final stage of the algorithm associated with the formation of the meta models.

## Formation of meta models

The meta models consist in the union of the selected models, for it, only the unique models within the selection are used, and the corresponding union is applied, this process depends if the model is of the classification or regression type, which are explained then.

If the models are regression, the predicted values ​​for each model within the selection are obtained and a weighting of said values ​​is done, this new weighting is compared with the real value presented by the data set and the Pearson coefficients are recalculated , Spearman, Kendall Tau and R quadratic, thus obtaining the new performance indicators. The weighting is based on the use of an accumulated probability function for the real value, which approximates a normal function by using the gamma distribution and the central limit theorem, in this way, the over-adjustment of the information and a generalization of the process is delivered.

In the case where the models are of the classification type, the predicted values ​​for each model are obtained and they are submitted to a voting process to obtain the weighted value of each example, said voting is associated to a distribution of the binomial type, which Consider the number of examples per class and the probability of occurrence for that class is associated with a Dirichlet process, this avoids the overfitting of the data and problems associated with the existing imbalance. Once you have the new classification vectors, you compare the real with these and you obtain the corresponding performance measures.

# Use of meta models and response of these

The meta models can be used to predict new examples or classify new data, depending on the case, the tool uses the models and delivers a new response associated with the meta model and the data delivered. For the evaluation of classifiers, a Dirichlet distribution based on Bayesian processes is used, which allows altering the probabilities of occurrences of events and also associating an error function that is given by the probability of committing a false positive. Delivering, for classification models, the probability associated with the response and the probability of committing a type 1 error. In the case of regression, a distribution of responses is obtained based on the models used and a confidence interval is calculated to express the result. As input for the use of meta models, a csv file with the new data to be processed is necessary, the results will be reported as previously exposed.

# Results report

MLSTraining reports the results depending on the model type developed. However, in general, they are presented in stages:

1. Participant models and summary of performance measures: A Venn diagram is presented with the models and in turn the performance measures are shown. If the model is of the regression type, a scatter plot of the actual data v / s is shown as predicted by the meta model. If the model is classified, the confusion matrix and indicators associated with reliability, sensitivity and stability are reported.

2. Graph of quantity of selected models according to measurement, a wordcloud with the models and a list of selected models based on the performance measurement.

3. Statistical summary of the general performance measures in the search stage.

4. Histograms by performance measure associated with the distributions generated by these in the search stage.

5. A summary of the process, computation cost, correct and incorrect iterations, together with an indicator to interpret the results, associated with a summary table with all the iterations generated.

# Access to the tool

The tool is public access, has a GPL 3.0 license so it is associated with free software, and its repository is public, which has both the Python library under which it was designed and the web controller under the which is implemented the view: [MLSTraining](https://github.com/dMedinaO/MLSTrainingTool).

Access to the web tool is public. However, to send new jobs to the system of service queues, it is necessary to leave your email to be notified of the changes made to the job, and the results will only be stored for 15 days at the time of finishing the job. The tool can be accessed through the link: [MLSTrainingTool](http://pesb2.cl/MLSTrainingTool/home).

The web tool itself consists of 5 sections, which are described below.

1. Home: Section to upload jobs to the service queue.
2. Query: Given the ID of the job, search it in the system and evaluate in what state it is.
3. Data Sets demo: set of data with which the system was tested, 4 for classification models and 4 for prediction.
4. About Us: Section to know the authors and the research center to which they belong (this is promotion and they force me to put it in every tool I make)
5. How to use: Section with a dynamic user manual explaining the operation of the tool and what the results mean along with their interpretation.

# Key Scripts

Within the bin directory of the Python modules, there are some key scripts that are exposed below.

1. launcherFullProcessClassification.py : create meta models for classification data set.

2. launcherFullProcessPrediction.py : create meta models for prediction data set.

3. tryUseModelsClf.py : use meta models for classify models.

4. tryUseModelsPrediction.py : use meta models for prediction models.
