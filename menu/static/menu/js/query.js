$(document).ready(function(){
    $("#form").submit(function(e){
        e.preventDefault();
        var nombre = $("#name").val();
        var correo = $("#email").val();
        var clave = $("#password").val();

        var msj = "";
        let enviar = false;

        if(nombre.trim().length < 4 || nombre.trim().length > 10){
            msj += "El nombre debe ser entre 4 y 10 caracteres";
            enviar = true;
        }

        var letra = nombre.charAt(0);
        if(!esMayuscula(letra)){
            msj += "<br>La primera letra debe ser mayúscula";
            enviar = true;
        }

        if(nombre == "Victor"){
            msj += "<br>El nombre no puede ser Victor";
            enviar = true;
        }

        if(enviar){
            $("#warnings").html(msj);
        }
        else{
            $("#warnings").html("Enviado");
        }




    });


    function esMayuscula(letra){
        console.log(letra);
        console.log(letra.toUpperCase());
        if(letra == letra.toUpperCase()){
            return true;
        }
        else{
            return false;
        }
         
    }

});