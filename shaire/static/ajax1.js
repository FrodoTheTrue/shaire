$(document).ready(function(){
	$('#text').keypress(function(e){
	    var cnt = 0;
	    if (e.which == 13)
	        {
	            $('#submt_{{ user_to_username }}').click();
	        }
		});
});