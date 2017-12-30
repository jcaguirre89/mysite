//Slider function with value on handle
var $element = $('input[type="range"]');

$element
  .rangeslider({
    polyfill: false,
    onInit: function() {
      var $handle = $('.rangeslider__handle', this.$range);
      updateHandle($handle[0], this.value);
    }
  })
  .on('input', function(e) {
    var $handle = $('.rangeslider__handle', e.target.nextSibling);
    updateHandle($handle[0], this.value);
  });

function updateHandle(el, val) {
  el.textContent = val;
}

//Count total function
$(function() {
  const sliders = document.querySelectorAll('input[type=range]');
  const result = document.getElementById('js-result');
  const values = getValues(sliders);
  
  $(sliders)
    .rangeslider({ polyfill: false })
    .on('change', function() {
      const values = getValues(sliders);
      updateResult(result, values);
    });
  
  // initially set result
  updateResult(result, values);  
});

function getValues(elements) {
  return Array.from(elements).map(el => el.value);
}

function updateResult(el, values) {
  el.textContent = values.reduce((a,b) => a + parseInt(b), 0);
}

//check if weights sum to 100
$("input[type=range]").change(function () {
	var result = parseInt(document.getElementById('js-result').value,10);	
	var sums = result + parseInt($(this).val(),10);
	console.log(sums);
});		
$('form').submit(function () {
	var result = parseInt(document.getElementById('js-result').value,10);		
	if (result!=100) {
		alert('Allocation must add up to 100.');
		return false;
	};

});

//change plotly width to 25%
$(document).ready(function () {
  $(".plotly-graph-div").css("width", "25%");
});