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

  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/5.4.2/math.js"></script>

  <script src="../js/jobs/processViewDistribution.js"></script>
  <script src="../js/jobs/processOptionSelecetd.js"></script>

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

                    </div>
                    <!--~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-->
                    <!--End page title-->
                </div>


                <!--Page content-->
                <!--===================================================-->
                <div id="page-content">

                <div class="row">
                  <div class="col-sm-7 col-md-7">

                    <div class="panel panel-bordered panel-primary">

                      <div class="panel-heading">
                        <h3 class="panel-title">
                          <h3 class="panel-title">Check distribution response</h3>
                        </h3>
                      </div>
                      <div class="panel-body">
                          <div id="histogram"></div>
                      </div>
                    </div>
                  </div>

                  <div class="col-lg-5 col-md-5 col-sm-5">
                    <div class="panel panel-bordered panel-primary">
                        <div class="panel-heading">
                            <h3 class="panel-title">What it is?</h3>
                        </div>
                        <div class="panel-body">
                          A histogram is an accurate representation of the distribution of numerical data. It is an estimate of the probability distribution of a continuous variable (quantitative variable). In a more general mathematical sense, a histogram is a function mi that counts the number of observations that fall into each of the disjoint categories (known as bins), whereas the graph of a histogram is merely one way to represent a histogram. Thus, if we let n be the total number of observations and k be the total number of bins.
                        </div>
                    </div>
                  </div>

                  <div class="col-lg-5 col-md-5 col-sm-5">

                    <div class="panel panel-bordered panel-primary">
                        <div class="panel-heading">
                            <h3 class="panel-title">Normal Distribution Evaluation</h3>
                        </div>
                        <div class="panel-body">
                          <table class="table table-hover table-vcenter">
                          <tbody>
                            <tr>
                              <td>
                                <span class="text-main text-semibold">Algorithm</span>
                              </td>
                              <td>
                                <span class="text-main text-semibold">Shapiro Wilk</span>
                              </td>
                             </tr>

                              <tr>
                                  <td>
                                    <span class="text-main text-semibold">Statistic Value</span>
                                  </td>
                                  <td>
                                      <span class="text-main text-semibold statisticValue"></span>
                                  </td>
                              </tr>

                              <tr>
                                  <td>
                                    <span class="text-main text-semibold">p-value</span>
                                  </td>
                                  <td>
                                      <span class="text-main text-semibold pvalue"></span>
                                  </td>
                              </tr>

                              <tr>
                                  <td>
                                    <span class="text-main text-semibold">Outliers</span>
                                  </td>
                                  <td>
                                      <span class="text-main text-semibold outliers"></span>
                                  </td>
                              </tr>

                              <tr>
                                  <td>
                                    <span class="text-main text-semibold">Threshold</span>
                                  </td>
                                  <td>
                                      <span class="text-main text-semibold"> 3</span>
                                  </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                    </div>
                  </div>

                  <!--panel asociado al job y a procesar el trabajo-->
                  <a id="goBack">
                    <div class="col-lg-4 col-md-4">
                      <div class="panel media middle pad-all">
                          <div class="media-left">
                              <span class="icon-wrap icon-wrap-sm icon-circle bg-success">
                              <i class="fa fa-backward fa-2x"></i>
                              </span>
                          </div>
                          <div class="media-body">
                              <p class="mar-no text-semibold text-main">Go back and selected new response</p>
                          </div>
                      </div>
                    </div>
                  </a>

                  <a id="removeOutliers">
                    <div class="col-lg-4 col-md-4">
                      <div class="panel media middle pad-all">
                          <div class="media-left">
                              <span class="icon-wrap icon-wrap-sm icon-circle bg-success">
                              <i class="fa fa-balance-scale fa-2x"></i>
                              </span>
                          </div>
                          <div class="media-body">
                              <p class="mar-no text-semibold text-main">Remove outliers and process job</p>
                          </div>
                      </div>
                    </div>
                  </a>

                  <a id="onlyProcess">
                    <div class="col-lg-4 col-md-4">
                      <div class="panel media middle pad-all">
                          <div class="media-left">
                              <span class="icon-wrap icon-wrap-sm icon-circle bg-success">
                              <i class="fa fa-file fa-2x"></i>
                              </span>
                          </div>
                          <div class="media-body">
                              <p class="mar-no text-semibold text-main">Process job without remove outliers</p>
                          </div>
                      </div>
                    </div>
                  </a>

                  <div class="col-sm-12 col-md-12 col-lg-12" id="errorResponse" style="display:none;">
                    <div class="alert alert-danger" role="alert">
                      Error during process job, please contact the administrator of system at email david.medina@cebib.cl
                    </div>
                  </div>

                  <div class="col-sm-12 col-md-12 col-lg-12" id="okResponse" style="display:none;">
                    <div class="alert alert-success" role="alert">
                      <p class="messageOK"></p>
                    </div>
                  </div>

                  <div class="col-sm-12 col-md-12 col-lg-12" id="loading" style="display:none;">
                      <div class="panel">
                          <div class="panel-body">
                              <div class="sk-three-bounce">
                                  <div class="sk-child sk-bounce1"></div>
                                  <div class="sk-child sk-bounce2"></div>
                                  <div class="sk-child sk-bounce3"></div>
                              </div>
                          </div>
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
</body>
</html>
