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

//alternate text
//about
$(document).ready(function () {
  $("#click-about").click(function() {
	  $("#main-text").text($("#about").text());
	  $(".selected").removeClass("selected");
	  $(this).addClass("selected");
  });
});

//data
$(document).ready(function () {
  $("#click-science").click(function() {
	  $("#main-text").text($("#science").text());
	  $(".selected").removeClass("selected");
	  $(this).addClass("selected");
  });
});

//django
$(document).ready(function () {
  $("#click-django").click(function() {
	  $("#main-text").text($("#django").text());
	  $(".selected").removeClass("selected");
	  $(this).addClass("selected");
  });
});