var csrftoken = $.cookie('csrftoken');
function csrfSafeMethod(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$( "#completar" ).click(function(){
	valor = $("#datos" ).val();
	completa_datos(valor)
});

function completa_datos(valor){
    $.ajax({
        beforeSend : function(xhr, settings){
			if(!csrfSafeMethod(settings.type) && !this.crossDomain){
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
		},
		url : "ajax/search_extra/",
		type : "GET",
		data : { valor : valor},
		success : function(json){
            valor_retornado = '<ul class="contact"><li><h3>Código Postal</h3><span>json[0].zip</span></li><li><h3>Provincia</h3><span>json[0].name</span></li></ul>'
            $('#datos').html(valor_retornado);
            console.log(json[0].zip);
		},
		error : function(xhr, errmsg, err){
			console.log('Error en carga de respuesta');
		},
    });
}
