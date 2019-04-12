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

  <!--Dropzone [ OPTIONAL ]-->
  <script src="../plugins/dropzone/dropzone.min.js"></script>
  <link href="../plugins/dropzone/dropzone.min.css" rel="stylesheet">
  <script src="../js/formatDropzone.js"></script>

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


  <!-- script para la carga de datos -->
  <script src="../js/jobs/tryModelClf.js"></script>
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

                    <div class="col-sm-12 col-md-12">

                      <div class="panel panel-bordered panel-primary">

                        <div class="panel-heading">
                          <h3 class="panel-title">
                            Try new examples for meta models in classification data
                          </h3>
                        </div>
                        <div class="panel-body">

                          <form id="frmAgregarFile" action="../php/uploadFileTry.php" class="dropzone" >
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

                          <hr>

                          <div class="ln_solid"></div>

                            <div class="form-group">
                                <div class="col-sm-5 col-sm-offset-3">
                                  <button id="processJob" class="btn btn-primary">Try Model</button>
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

                          <div class="col-sm-12 col-md-12 col-lg-12" id="errorResponse" style="display:none;">
                            <div class="alert alert-danger" role="alert">
                              <p class="messageError"></p>
                            </div>
                          </div>

                        </div>
                    </div>
                  </div>

                </div>
                <div class="row">
                  <div class="col-sm-12 col-md-12">

                    <div class="panel panel-bordered panel-primary">

                      <div class="panel-heading">
                        <h3 class="panel-title">
                          Important information
                        </h3>
                      </div>
                      <div class="panel-body">
                        Please enter files in * .csv or * .tsv format. This process may take a maximum of 15 minutes. Please, do not reload the page.
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
