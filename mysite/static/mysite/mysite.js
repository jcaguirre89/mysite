//validate username
$("#id_username").change(function() {
    var form = $(this).closest("form");
	$.ajax( {
	  url: form.attr("data-validate-username-url"),
	  data: form.serialize(),
	  dataType: 'json',
	  success: function (data) {
		  $("#id_username").text(data.message);          
		  if (data.is_taken) {
		  $("#id_username").removeClass("user-ok").addClass("user-notok");
		} else {
		  $("#id_username").removeClass("user-notok").addClass("user-ok");
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