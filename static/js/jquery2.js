$(document).ready(function(){
	function ajax_login(){
		$.ajax({
			url: '/ajax-login',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	}
	function crear_usuario(){
		$.ajax({
			url: '/crear',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	}


	$("#contactFormlogin").submit(function(event){
		//event.preventDefault();
		//ajax_login();
	});
	$("#contactFormcrear2").submit(function(event){
		event.preventDefault();
		crear_usuario();
	});
});