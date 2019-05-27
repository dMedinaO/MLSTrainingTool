$(document).ready(function() {

  $('#initNewJob').bootstrapValidator({
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {

            email: {
                validators: {
                    notEmpty: {
                        message: 'The email is required'
                    }
                }
            },

            nameJob: {
                validators: {
                    notEmpty: {
                        message: 'The nameJob is required'
                    }
                }
            },
            descJob: {
                validators: {
                    notEmpty: {
                        message: 'The description Job is required'
                    }
                }
            }
        }
    }).on('success.form.bv', function(e) {
      e.preventDefault();
      $('#loading').show();
      var email = $("#initNewJob #email").val();
      var nameJob = $("#initNewJob #nameJob").val();
      var descJob = $("#initNewJob #descJob").val();
      var optionProcess = $("#initNewJob #optionProcess").val();

      $.ajax({
        method: "POST",
        url: "php/jobs/addData.php",
        data: {
          "email"   : email,
          "nameJob"   : nameJob,
          "descJob"   : descJob,
          "optionProcess"   : optionProcess

        }
      }).done( function( info ){
        var response = JSON.parse(info);

        if (response.exec== "ERROR"){
          $('#loading').hide();
          var message = "Error during the creation of the job, please check the data set. If the error persists, please contact the administrator.";
          $(".messageError").html( message);

          $('#errorResponse').show();
          setTimeout("location.href=''", 5000);
        }else{
          var job = response.job;
          location.href="checkDataSet/?job="+job+"&kind="+optionProcess;
        }
      });
  });
});
