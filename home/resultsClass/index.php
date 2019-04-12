<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Dashboard MLSTraining</title>

    <!--STYLESHEET-->
    <!--=================================================-->

    <!--Open Sans Font [ OPTIONAL ]-->
    <link href='https://fonts.googleapis.com/css?family=Open+Sans:400,300,600,700' rel='stylesheet' type='text/css'>


    <!--Bootstrap Stylesheet [ REQUIRED ]-->
    <link href="../css/bootstrap.min.css" rel="stylesheet">


    <!--Nifty Stylesheet [ REQUIRED ]-->
    <link href="../css/nifty.min.css" rel="stylesheet">
		<link href="../css/demo/nifty-demo-icons.min.css" rel="stylesheet">
    <link href="../plugins/magic-check/css/magic-check.min.css" rel="stylesheet">


    <!--Nifty Premium Icon [ DEMONSTRATION ]-->
    <link href="../css/demo/nifty-demo-icons.min.css" rel="stylesheet">


    <!--DataTables [ OPTIONAL ]-->
    <link href="../plugins/datatables/media/css/dataTables.bootstrap.css" rel="stylesheet">
    <link href="../plugins/datatables/extensions/Responsive/css/responsive.dataTables.min.css" rel="stylesheet">

    <!--Bootstrap Validator [ OPTIONAL ]-->
    <link href="../plugins/bootstrap-validator/bootstrapValidator.min.css" rel="stylesheet">
    <!--JAVASCRIPT-->
    <!--=================================================-->

    <!--Pace - Page Load Progress Par [OPTIONAL]-->
    <link href="../plugins/pace/pace.min.css" rel="stylesheet">
    <script src="../plugins/pace/pace.min.js"></script>


    <!--jQuery [ REQUIRED ]-->
    <script src="../js/jquery.min.js"></script>


    <!--BootstrapJS [ RECOMMENDED ]-->
    <script src="../js/bootstrap.min.js"></script>


    <!--NiftyJS [ RECOMMENDED ]-->
    <script src="../js/nifty.min.js"></script>
		<script src="../plugins/bootstrap-wizard/jquery.bootstrap.wizard.min.js"></script>
		<script src="../js/demo/form-wizard.js"></script>

    <!--=================================================-->

    <!--Font Awesome [ OPTIONAL ]-->
    <link href="../plugins/font-awesome/css/font-awesome.min.css" rel="stylesheet">
    <!--Ion Icons [ OPTIONAL ]-->
    <link href="../plugins/flag-icon-css/css/flag-icon.min.css" rel="stylesheet">
    <!--Ion Icons [ OPTIONAL ]-->
    <link href="../plugins/ionicons/css/ionicons.min.css" rel="stylesheet">
    <!--Themify Icons [ OPTIONAL ]-->
    <link href="../plugins/themify-icons/themify-icons.min.css" rel="stylesheet">
    <!--Premium Line Icons [ OPTIONAL ]-->
    <link href="../premium/icon-sets/icons/line-icons/premium-line-icons.min.css" rel="stylesheet">
    <link href="../plugins/spinkit/css/spinkit.min.css" rel="stylesheet">
    <script src="../plugins/bootstrap-validator/bootstrapValidator.min.js"></script>

    <!--DataTables [ OPTIONAL ]-->
    <link href="../plugins/datatables/media/css/dataTables.bootstrap.css" rel="stylesheet">
	  <link href="../plugins/datatables/extensions/Responsive/css/responsive.dataTables.min.css" rel="stylesheet">

    <!--DataTables [ OPTIONAL ]-->
    <script src="../plugins/datatables/media/js/jquery.dataTables.js"></script>
	  <script src="../plugins/datatables/media/js/dataTables.bootstrap.js"></script>
	  <script src="../plugins/datatables/extensions/Responsive/js/dataTables.responsive.min.js"></script>


    <!-- para los higcharts-->
		<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
		<!-- para los higcharts-->
    <script src="http://code.highcharts.com/highcharts.js"></script>
    <script src="https://code.highcharts.com/highcharts-more.js"></script>
    <script src="http://code.highcharts.com/modules/exporting.js"></script>
    <script src="https://code.highcharts.com/modules/series-label.js"></script>
    <script src="http://code.highcharts.com/modules/heatmap.js"></script>

    <script src="http://d3js.org/d3.v4.js"></script>
    <script src="http://d3js.org/d3.v3.min.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/holtzy/D3-graph-gallery@master/LIB/d3.layout.cloud.js"></script>
    <script src="https://rawgit.com/jasondavies/d3-cloud/master/build/d3.layout.cloud.js"></script>
    <script src="../js/resultsClf/viewResponseJobClass.js"></script>
		<script src="../js/resultsClf/processViewStatisticsClass.js"></script>
		<script src="../js/resultsClf/processViewSummaryClass.js"></script>

		<!-- mostrar la seleccion de modelos-->
		<script src="../js/resultsClf/viewSelectModels.js"></script>
		<script src="../js/resultsClf/viewSelectModelsGraphic.js"></script>
    <script src="../js/resultsClf/worldcloud.js"></script>
    <script src="../js/resultsClf/loadResponseDiagramm.js"></script>
    <script src="../js/resultsClf/viewPerformanceData.js"></script>
    <script src="../js/resultsClf/showResultsForClf.js"></script>

    <script src="../js/resultsClf/downloadMetaModels.js"></script>

    <style media="screen">
      #viewDiagramm {
        min-width: 320px;
        max-width: 800px;
        margin: 0 auto;
      }
    </style>
</head>

<!--TIPS-->
<!--You may remove all ID or Class names which contain "demo-", they are only used for demonstration. -->
<body>
    <div id="container" class="effect aside-float aside-bright mainnav-lg">

        <!--NAVBAR-->
        <!--===================================================-->
        <header id="navbar">
            <div id="navbar-container" class="boxed">

                <!--Brand logo & name-->
                <!--================================-->
								<div class="navbar-header">
                    <a href="" class="navbar-brand">
                        <img src="../img/logo.png" alt="Nifty Logo" class="brand-icon">
                        <div class="brand-title">
                            <span class="brand-text">MLSTraining</span>
                        </div>
                    </a>
                </div>
                <!--================================-->
                <!--End brand logo & name-->


                <!--Navbar Dropdown-->
                <!--================================-->
                <div class="navbar-content clearfix">
                    <ul class="nav navbar-top-links pull-left">

                        <!--Navigation toogle button-->
                        <!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
                        <li class="tgl-menu-btn">
                            <a class="mainnav-toggle" href="#">
                                <i class="demo-pli-view-list"></i>
                            </a>
                        </li>
                        <!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
                        <!--End Navigation toogle button-->

                    </ul>
                </div>
                <!--================================-->
                <!--End Navbar Dropdown-->

            </div>
        </header>
        <!--===================================================-->
        <!--END NAVBAR-->

        <div class="boxed">

            <!--CONTENT CONTAINER-->
            <!--===================================================-->
            <div id="content-container">
                <div id="page-head">

                    <!--Page Title-->
                    <!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
                    <div id="page-title">
                        <h1 class="page-header text-overflow nameJob">
												</h1>

                    </div>
                    <!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
                    <!--End page title-->
                </div>


                <!--Page content-->
                <!--===================================================-->
              <div id="page-content">
								<div class="col-lg-12 col-md-12 col-sm-12">
										<div class="panel">

								<div id="demo-cir-wz">
										<div class="wz-heading pad-ver">

												<!--Progress bar-->
												<div class="progress progress-xs progress-light-base">
														<div class="progress-bar progress-bar-primary"></div>
												</div>

												<!--Nav-->
												<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
												<ul class="wz-nav-off">
														<li class="col-xs-2">
																<a data-toggle="tab" href="#models" title="Models Results and Performance" class="add-tooltip">
																		<div class="icon-wrap icon-wrap-sm bg-gray">
																				<i class="wz-icon demo-pli-information icon-lg"></i>
																				<i class="wz-icon-done demo-pli-like icon-lg"></i>
																		</div>
																</a>
														</li>
														<li class="col-xs-2">
																<a data-toggle="tab" href="#selected" title="Selected Model" class="add-tooltip">
																		<div class="icon-wrap icon-wrap-sm bg-gray">
																				<i class="wz-icon demo-pli-information icon-lg"></i>
																				<i class="wz-icon-done demo-pli-like icon-lg"></i>
																		</div>
																</a>
														</li>
														<li class="col-xs-2">
																<a data-toggle="tab" href="#statisticSummary" title="Statistical Summary" class="add-tooltip">
																		<div class="icon-wrap icon-wrap-sm bg-gray">
																				<i class="wz-icon demo-pli-information icon-lg"></i>
																				<i class="wz-icon-done demo-pli-like icon-lg"></i>
																		</div>
																</a>
														</li>
														<li class="col-xs-2">
																<a data-toggle="tab" href="#distribution" title="Distribution Performance" class="add-tooltip">
																		<div class="icon-wrap icon-wrap-sm bg-gray">
																				<i class="wz-icon demo-pli-information icon-lg"></i>
																				<i class="wz-icon-done demo-pli-like icon-lg"></i>
																		</div>
																</a>
														</li>
														<li class="col-xs-2">
																<a data-toggle="tab" href="#summary" title="Summary Process" class="add-tooltip">
																		<div class="icon-wrap icon-wrap-sm bg-gray">
																				<i class="wz-icon demo-pli-information icon-lg"></i>
																				<i class="wz-icon-done demo-pli-like icon-lg"></i>
																		</div>
																</a>
														</li>
														<li class="col-xs-2">
																<a data-toggle="tab" href="#tryModel" title="Try Model" class="add-tooltip">
																		<div class="icon-wrap icon-wrap-sm bg-gray">
																				<i class="wz-icon demo-pli-information icon-lg"></i>
																				<i class="wz-icon-done demo-pli-like icon-lg"></i>
																		</div>
																</a>
														</li>
												</ul>
										</div>

										<!--Form-->
										<form class="form-horizontal">
												<div class="panel-body">
														<div class="tab-content">

																<!--First tab-->
																<div id="distribution" class="tab-pane">
																	<div class="row">

																		<div class="col-lg-12 col-md-12 col-sm-12">
																	    <div class="panel panel-bordered panel-primary">
																	        <div class="panel-heading">
																	            <h3 class="panel-title">Histogram by Precision</h3>
																	        </div>
																	        <div class="panel-body">
																	          <div id="precisionHistogram"></div>
																	        </div>
																	    </div>
																	  </div>

																	  <div class="col-lg-12 col-md-12 col-sm-12">
																	    <div class="panel panel-bordered panel-primary">
																	        <div class="panel-heading">
																	            <h3 class="panel-title">Histogram by Accuracy</h3>
																	        </div>
																	        <div class="panel-body">
																	          <div id="accuracyHistogram"></div>
																	        </div>
																	    </div>
																	  </div>

																		<div class="col-lg-12 col-md-12 col-sm-12">
																	    <div class="panel panel-bordered panel-primary">
																	        <div class="panel-heading">
																	            <h3 class="panel-title">Histogram by Recall</h3>
																	        </div>
																	        <div class="panel-body">
																	          <div id="recallHistogram"></div>
																	        </div>
																	    </div>
																	  </div>

																	  <div class="col-lg-12 col-md-12 col-sm-12">
																	    <div class="panel panel-bordered panel-primary">
																	        <div class="panel-heading">
																	            <h3 class="panel-title">Histogram by F1</h3>
																	        </div>
																	        <div class="panel-body">
																	          <div id="f1Histogram"></div>
																	        </div>
																	    </div>
																	  </div>
																	</div>
																</div>

																<!--Second tab-->
																<div id="statisticSummary" class="tab-pane fade">
																	<div class="row">
																	  <div class="col-lg-12 col-md-12 col-sm-12">
																	    <div class="panel panel-bordered panel-primary">
																	        <div class="panel-heading">
																	            <h3 class="panel-title">Summary Statistics data of Performance</h3>
																	        </div>
																	        <div class="panel-body">

																	          <table id="statistical" class="table table-striped table-bordered" cellspacing="0" width="100%">
																	              <thead>
																	                <tr>
																	                  <th class="min-tablet">Performance</th>
																	                  <th class="min-tablet">Average</th>
																	                  <th class="min-tablet">Standar Deviation</th>
																	                  <th class="min-tablet">Variance</th>
																	                  <th class="min-tablet">Max Value</th>
																	                  <th class="min-tablet">Min Value</th>
																	                </tr>
																	              </thead>
																	          </table>

																	        </div>
																	    </div>
																	  </div>
																	</div>
																</div>

																<!--Third tab-->
																<div id="summary" class="tab-pane">
																	<div class="row">
																	  <div class="col-lg-12 col-md-12 col-sm-12">
																	    <div class="panel panel-bordered panel-primary">
																	        <div class="panel-heading">
																	            <h3 class="panel-title">Summary Process and Definition</h3>
																	        </div>
																	        <div class="panel-body">
																	          <table class="table table-hover table-vcenter">
																	          <tbody>
																	            <tr>
																	              <td>
																	                <span class="text-main text-semibold">Start Process</span>
																	              </td>
																	              <td>
																	                <span class="text-main text-semibold start"></span>
																	                <br>
																	              </td>
																	             </tr>

																	              <tr>
																	                  <td>
																	                    <span class="text-main text-semibold">End Process</span>
																	                  </td>
																	                  <td>
																	                      <span class="text-main text-semibold end"></span>
																	                      <br>
																	                  </td>
																	              </tr>

																	              <tr>
																	                  <td>
																	                    <span class="text-main text-semibold">Duration in minutes</span>
																	                  </td>
																	                  <td>
																	                      <span class="text-main text-semibold duration"></span>
																	                      <br>
																	                  </td>
																	              </tr>

																	              <tr>
																	                  <td>
																	                    <span class="text-main text-semibold">Correct executions</span>
																	                  </td>
																	                  <td>
																	                      <span class="text-main text-semibold correct"></span>
																	                      <br>
																	                  </td>
																	              </tr>

																	              <tr>
																	                  <td>
																	                    <span class="text-main text-semibold">Incorrect executions</span>
																	                  </td>
																	                  <td>
																	                      <span class="text-main text-semibold incorrect"></span>
																	                      <br>
																	                  </td>
																	              </tr>

																	              <tr>
																	                  <td>
																	                    <span class="text-main text-semibold">Accuracy</span>
																	                  </td>
																	                  <td>
																	                      <span class="text-main  accuracyDefinition"></span>
																	                      <br>
																	                  </td>
																	              </tr>

																	              <tr>
																	                  <td>
																	                    <span class="text-main text-semibold">Precision</span>
																	                  </td>
																	                  <td>
																	                      <span class="text-main  precisionDefinition"></span>
																	                      <br>
																	                  </td>
																	              </tr>

																	              <tr>
																	                  <td>
																	                    <span class="text-main text-semibold">Recall</span>
																	                  </td>
																	                  <td>
																	                      <span class="text-main  recallDefinition"></span>
																	                      <br>
																	                  </td>
																	              </tr>

																	              <tr>
																	                  <td>
																	                    <span class="text-main text-semibold">F1 Score</span>
																	                  </td>
																	                  <td>
																	                      <span class="text-main f1Definition"></span>
																	                      <br>
																	                  </td>
																	              </tr>

																	          </tbody>
																	      </table>
																	        </div>
																	    </div>
																	  </div>
																	</div>

                                  <div class="row">
																	  <div class="col-lg-12 col-md-12 col-sm-12">
																	    <div class="panel panel-bordered panel-primary">
																	        <div class="panel-heading">
																	            <h3 class="panel-title">Job Summary Process</h3>
																	        </div>
																	        <div class="panel-body">

																	          <table id="jobSummary" class="table table-striped table-bordered" cellspacing="0" width="100%">
																	              <thead>
																	                <tr>
																	                  <th class="min-tablet">Algorithm</th>
																	                  <th class="min-tablet">Params</th>
																	                  <th class="min-tablet">CV</th>
																	                  <th class="min-tablet">Accuracy</th>
																	                  <th class="min-tablet">Recall</th>
																	                  <th class="min-tablet">Precision</th>
																	                  <th class="min-tablet">F1 Score</th>
																	                </tr>
																	              </thead>
																	          </table>

																	        </div>
																	    </div>
																	  </div>
																	</div>

																</div>

																<!--Fourth tab-->
																<div id="selected" class="tab-pane">

																	<div class="row">

                                    <div class="col-lg-6 col-md-6 col-sm-12">
																	    <div class="panel panel-bordered panel-primary">
																	        <div class="panel-heading">
																	            <h3 class="panel-title">Distribution models by Performance</h3>
																	        </div>
																	        <div class="panel-body">
                                            <div id="distributionPerformanceModel"></div>
																	        </div>
																	    </div>
																	  </div>

                                    <div class="col-lg-6 col-md-6 col-sm-12">
																	    <div class="panel panel-bordered panel-primary">
																	        <div class="panel-heading">
																	            <h3 class="panel-title">Wordcloud of Algorithm</h3>
																	        </div>
																	        <div class="panel-body">
                                            <img id="worldcloudView" class="img-thumbnail"></img>
																	        </div>
																	    </div>
																	  </div>

																	  <div class="col-lg-12 col-md-12 col-sm-12">
																	    <div class="panel panel-bordered panel-primary">
																	        <div class="panel-heading">
																	            <h3 class="panel-title">Selected Models By Precision</h3>
																	        </div>
																	        <div class="panel-body">

																	          <table id="modelP" class="table table-striped table-bordered" cellspacing="0" width="100%">
																	              <thead>
																	                <tr>
																	                  <th class="min-tablet">Algorithm</th>
																	                  <th class="min-tablet">Params</th>
																	                  <th class="min-tablet">Precision</th>
																	                </tr>
																	              </thead>
																	          </table>

																	        </div>
																	    </div>
																	  </div>

																		<div class="col-lg-12 col-md-12 col-sm-12">
																	    <div class="panel panel-bordered panel-primary">
																	        <div class="panel-heading">
																	            <h3 class="panel-title">Selected Models By Accuracy</h3>
																	        </div>
																	        <div class="panel-body">

																	          <table id="modelA" class="table table-striped table-bordered" cellspacing="0" width="100%">
																	              <thead>
																	                <tr>
																	                  <th class="min-tablet">Algorithm</th>
																	                  <th class="min-tablet">Params</th>
																	                  <th class="min-tablet">Accuracy</th>
																	                </tr>
																	              </thead>
																	          </table>

																	        </div>
																	    </div>
																	  </div>

																		<div class="col-lg-12 col-md-12 col-sm-12">
																	    <div class="panel panel-bordered panel-primary">
																	        <div class="panel-heading">
																	            <h3 class="panel-title">Selected Models By Recall</h3>
																	        </div>
																	        <div class="panel-body">

																	          <table id="modelR" class="table table-striped table-bordered" cellspacing="0" width="100%">
																	              <thead>
																	                <tr>
																	                  <th class="min-tablet">Algorithm</th>
																	                  <th class="min-tablet">Params</th>
																	                  <th class="min-tablet">Recall</th>
																	                </tr>
																	              </thead>
																	          </table>
																	        </div>
																	    </div>
																	  </div>

																		<div class="col-lg-12 col-md-12 col-sm-12">
																	    <div class="panel panel-bordered panel-primary">
																	        <div class="panel-heading">
																	            <h3 class="panel-title">Selected Models By F1</h3>
																	        </div>
																	        <div class="panel-body">

																	          <table id="modelF" class="table table-striped table-bordered" cellspacing="0" width="100%">
																	              <thead>
																	                <tr>
																	                  <th class="min-tablet">Algorithm</th>
																	                  <th class="min-tablet">Params</th>
																	                  <th class="min-tablet">F1</th>
																	                </tr>
																	              </thead>
																	          </table>
																	        </div>
																	    </div>
																	  </div>
																	</div>
																</div>

                                <!--Five tab-->
                                <div id="models" class="tab-pane">

                                  <div class="col-lg-12 col-md-12 col-sm-12">
                                    <div class="panel panel-bordered panel-primary">
                                        <div class="panel-heading">
                                            <h3 class="panel-title">Join Models in view Diagramm</h3>
                                        </div>
                                        <div class="panel-body">
                                          <div id="viewDiagramm"></div>
                                        </div>
                                    </div>
                                  </div>

                                  <!-- medidas de desempeno -->
                                  <div class="col-lg-12 col-md-12 col-sm-12">
                                    <div class="panel panel-bordered panel-primary">
                                        <div class="panel-heading">
                                            <h3 class="panel-title">Weighted Performance for the selected models</h3>
                                        </div>
                                        <div class="panel-body">
                                          <div class="row">

                                            <div class="col-lg-3 col-md-3">
                                              <div class="panel media middle pad-all">
                                                  <div class="media-left">
                                                      <span class="icon-wrap icon-wrap-sm icon-circle bg-primary">
                                                      <i class="fa fa-bar-chart fa-2x"></i>
                                                      </span>
                                                  </div>
                                                  <div class="media-body">
                                                      <p class="text-2x mar-no text-semibold text-main precision"></p>
                                                      <p class="text-muted mar-no">Precision</p>
                                                  </div>
                                              </div>
                                            </div>
                                            <div class="col-lg-3 col-md-3">
                                              <div class="panel media middle pad-all">
                                                  <div class="media-left">
                                                      <span class="icon-wrap icon-wrap-sm icon-circle bg-primary">
                                                      <i class="fa fa-line-chart fa-2x"></i>
                                                      </span>
                                                  </div>
                                                  <div class="media-body">
                                                      <p class="text-2x mar-no text-semibold text-main accuracy"></p>
                                                      <p class="text-muted mar-no">Accuracy</p>
                                                  </div>
                                              </div>
                                            </div>
                                            <div class="col-lg-3 col-md-3">
                                              <div class="panel media middle pad-all">
                                                  <div class="media-left">
                                                      <span class="icon-wrap icon-wrap-sm icon-circle bg-primary">
                                                      <i class="fa fa-code-fork fa-2x"></i>
                                                      </span>
                                                  </div>
                                                  <div class="media-body">
                                                      <p class="text-2x mar-no text-semibold text-main recall"></p>
                                                      <p class="text-muted mar-no">Recall</p>
                                                  </div>
                                              </div>
                                            </div>
                                            <div class="col-lg-3 col-md-3">
                                              <div class="panel media middle pad-all">
                                                  <div class="media-left">
                                                      <span class="icon-wrap icon-wrap-sm icon-circle bg-primary">
                                                      <i class="fa fa-pie-chart fa-2x"></i>
                                                      </span>
                                                  </div>
                                                  <div class="media-body">
                                                      <p class="text-2x mar-no text-semibold text-main f1Values"></p>
                                                      <p class="text-muted mar-no">F1 Score</p>
                                                  </div>
                                              </div>
                                            </div>

                                          </div>
                                        </div>
                                    </div>
                                  </div>

                                  <div class="col-lg-12 col-md-12 col-sm-12">
                                    <div class="panel panel-bordered panel-primary">
                                        <div class="panel-heading">
                                            <h3 class="panel-title">Confusion Matrix</h3>
                                        </div>
                                        <div class="panel-body">
                                          <div id="confusionMatrixGraph"></div>
                                        </div>

                                    </div>
                                  </div>
                                </div>

																<!--Six tab-->
																<div id="tryModel" class="tab-pane">

                                  <div class="row">

                                    <div class="col-sm-6 col-md-6">

                                      <div class="panel panel-bordered panel-primary pos-rel">
                                        <div class="pad-all text-center">
                                            <div class="widget-control">
                                            </div>
                                            <?php
                                              $job = $_REQUEST['job'];
                                              echo "<a href='../tryModelClf/?job=".$job."'>";
                                            ?>

                                              <img alt="Profile Picture" class="img-lg img-circle mar-ver" src="../img/other/use.jpg">
                                              <p class="text-lg text-semibold mar-no text-main">Try with web tool</p>
                                              <p class="text-sm">Using models with the web tool involves uploading a file in csv format through the platform. We remind you of the permanence of the files in our system, so this use is limited.</p>
                                            </a>
                                          </div>
                                        </div>
                                      </div>

                                      <div class="col-sm-6 col-md-6">

                                        <div class="panel panel-bordered panel-primary pos-rel">
                                          <div class="pad-all text-center">
                                              <div class="widget-control">
                                              </div>

                                                <a id="downloadAnchorElem">
                                                <img alt="Profile Picture" class="img-lg img-circle mar-ver" src="../img/other/try.jpg">
                                                <p class="text-lg text-semibold mar-no text-main">Try with export models</p>
                                                <p class="text-sm">Using models locally involves downloading the meta models in JSON format and using the loader provided in the repository in the model/bin section. See README for more information.</p>
                                              </a>
                                            </div>
                                          </div>
                                        </div>

                                  </div>
															</div>
														</div>
												</div>

												<!--Footer button-->
												<div class="panel-footer text-right">
														<div class="box-inline">
																<button type="button" class="previous btn btn-primary">Previous</button>
																<button type="button" class="next btn btn-primary">Next</button>
																<button type="button" class="finish btn btn-success" disabled>Finish</button>
														</div>
												</div>
										</form>
								</div>
							</div>
					</div>
              </div>
            </div>

            <!--MAIN NAVIGATION-->
            <!--===================================================-->
						<nav id="mainnav-container">
                <div id="mainnav">

                    <!--Menu-->
                    <!--================================-->
                    <div id="mainnav-menu-wrap">
                        <div class="nano">
                            <div class="nano-content">

                                <!--Profile Widget-->
                                <!--================================-->
                                <div id="mainnav-profile" class="mainnav-profile">
                                    <div class="profile-wrap text-center">
                                        <div class="pad-btm">
                                            <img class="img-circle img-md" src="../img/profile-photos/11.png" alt="Profile Picture">
                                        </div>

                                        <p class="mnp-name">
                                            User View
                                        </p>
                                    </div>
                                </div>

                                <ul id="mainnav-menu" class="list-group">

                                  <li class="list-header">Dashboard</li>

                                  <li>
          						                <a href="../query/">
          						                    <i class="fa fa fa-list"></i>
          						                    <span class="menu-title">Query Job</span><i class="arrow"></i>
          						                </a>

          						            </li>

                                  <li>
          						                <a href="../dataSet/">
          						                    <i class="fa fa fa-archive"></i>
          						                    <span class="menu-title">Data Sets Demo</span><i class="arrow"></i>
          						                </a>

          						            </li>

                                  <li>
          						                <a href="../about">
          						                    <i class="fa fa fa-users"></i>
          						                    <span class="menu-title">About Us</span><i class="arrow"></i>
          						                </a>

          						            </li>

                                  <li>
          						                <a href="../userManual">
          						                    <i class="fa fa fa-file"></i>
          						                    <span class="menu-title">How to use</span><i class="arrow"></i>
          						                </a>

          						            </li>

                                  <li>
          						                <a href="../">
          						                    <i class="fa fa fa-home"></i>
          						                    <span class="menu-title">Home</span><i class="arrow"></i>
          						                </a>

          						            </li>

						            </ul>

                    <!--================================-->
                    <!--End menu-->

                </div>
            </nav>
            <!--===================================================-->
            <!--END MAIN NAVIGATION-->

        </div>



        <!-- FOOTER -->
        <!--===================================================-->
        <footer id="footer">

            <!-- Visible when footer positions are fixed -->
            <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
            <div class="show-fixed pad-rgt pull-right">
                You have <a href="#" class="text-main"><span class="badge badge-danger">3</span> pending action.</a>
            </div>

            <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
            <!-- Remove the class "show-fixed" and "hide-fixed" to make the content always appears. -->
            <!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

            <p class="pad-lft">&#0169; 2019 Developed by <a href="http://pesb2.cl/"> PESB2 Group, </a>Centre for Biothecnology and Bioengineering, FCFM, University of Chile</p>

        </footer>
        <!--===================================================-->
        <!-- END FOOTER -->


        <!-- SCROLL PAGE BUTTON -->
        <!--===================================================-->
        <button class="scroll-top btn">
            <i class="pci-chevron chevron-up"></i>
        </button>
        <!--===================================================-->



    </div>
    <!--===================================================-->
    <!-- END OF CONTAINER -->

   <!-- modal section -->

   <div>
   	<form id="frmEditar" action="" method="POST" data-parsley-validate class="form-horizontal form-label-left">
   		<input type="hidden" id="idjob" name="idjob" value="">
   		<div class="modal fade" id="myModalEditar" tabindex="-1" role="dialog" aria-labelledby="myModalLabelEdit" aria-hidden="true">
   				<div class="modal-dialog">
   					<div class="modal-content">
   						<div class="modal-header">
   							<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
   							<h4 class="modal-title" id="myModalLabelEdit">Drop job</h4>
   						</div>
   						<div class="modal-body">

                <p>
                   Are you sure you want to delete the selected job?
                </p>


   						  <div class="ln_solid"></div>
   						  <div class="form-group">
   							<div class="col-md-9 col-sm-9 col-xs-12 col-md-offset-3">
   								<button type="button" id="editar-user" class="btn btn-primary" data-dismiss="modal">Delete</button>
   								<button type="button" class="btn btn-default" data-dismiss="modal">Cancelar</button>
   							</div>
   						  </div>

   						</div>

   					</div>
   				</div>
   		</div>
   		</form>
   </div>

   <!-- modal para agregar-->
  <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
            <h4 class="modal-title" id="myModalLabel">Add new job at queue system</h4>
          </div>
          <div class="modal-body">

             <form id="frmAgregarFile" action="../php/uploadFileQueue.php" class="dropzone" >
                    <div class="dz-default dz-message">
                        <div class="dz-icon">
                            <i class="demo-pli-upload-to-cloud icon-5x"></i>
                        </div>
                        <div>
                          <span class="dz-text">Drop files to upload</span>
                          <p class="text-sm text-muted">or click to pick manually</p>
                        </div>
                    </div>
                    <div class="fallback">
                        <input name="file" type="file" multiple>
                    </div>
                </form>

             <br>
             <br>

          <form id="frmAgregar" action="" method="POST" data-parsley-validate class="form-horizontal form-label-left">
            <div class="form-group">
            <label class="control-label col-md-3 col-sm-3 col-xs-12" for="name">Name Job <span class="required">*</span>
            </label>

            <div class="col-md-9 col-sm-9 col-xs-12">
              <input type="text" id="name" required="required" class="form-control col-md-7 col-xs-12" placeholder="Input name job">
            </div>
            </div>

            <div class="form-group">
            <label class="control-label col-md-3 col-sm-3 col-xs-12" for="desc">Description <span class="required">*</span>
            </label>

            <div class="col-md-9 col-sm-9 col-xs-12">
              <input type="text" id="desc" required="required" class="form-control col-md-7 col-xs-12" placeholder="Input description job">
            </div>

            </div>
            <div class="form-group">
              <label class="control-label col-md-3 col-sm-3 col-xs-12" for="option">Selected job <span class="required">*</span>
              </label>

              <div class="col-md-9 col-sm-9 col-xs-12">
                <select id="option" class="form-control">
                  <option value="1">CLASSIFICATION</option>
                  <option value="2">PREDICTION</option>
                </select>
              </div>
            </div>

            <div class="ln_solid"></div>
            <div class="form-group">
            <div class="col-md-9 col-sm-9 col-xs-12 col-md-offset-3">
              <button type="reset" class="btn btn-primary">Reset</button>
              <button type="button" id="add-job" class="btn btn-success" data-dismiss="modal">Add Job</button>
              <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>
            </div>
            </div>

          </div>

        </div>
      </div>
    </form>
  </div>

</body>
</html>
