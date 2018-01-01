//validate username
$("#id_username").change(function() {
    var form = $(this).closest("form");
	$.ajax( {
	  url: form.attr("data-validate-username-url"),
	  data: form.serialize(),
	  dataType: 'json',
	  success: function (data) {
		if (data.is_taken) {
		  $("#username-check").text(data.error_message)
		} else {
		  $("#username-check").text("Username available")		    
		}
	  }
	});  
  
});