function descuento(){
    let porc,valor,desc,total;

    valor = document.getElementById("total").innerHTML;
    desc = document.getElementById("desc").innerHTML;
    porc = 0.85;
    
    
    valor = parseInt(valor);

    total = (valor*porc);
    desc = (valor-total);
    document.getElementById("total").innerHTML = ("$"+total);
    document.getElementById("desc").innerHTML = ("$"+desc);
    
}
function valCupon(){

    let cup,text;
    cup = "PRIMERACOMPRA";
    text = document.getElementById("cupon").value;
    text = text.toUpperCase();
    

    if(text == cup){
        document.getElementById("cupon").value = "";
        document.getElementById("mensaje").innerHTML = "Tienes un descuento activo del 15%";
        descuento();

    }else{
        document.getElementById("mensaje").innerHTML = "El cupón ingresado no es válido";
    }
}

/*$(document).ready(function(){
    let suma, precio;
    suma = $("#total").val();
    parseInt(suma);
    precio = $("#precio").val();
    console.log("hola")
    parseInt(precio);
    suma = suma + precio;


    
    $("#total").val = suma;
    
    
})*/
$(document).ready(function(){
    $('#compraLista').modal('show');
});


/*Consumo de API*/
$(document).ready(function(){
    $("#linkHombre").click(function(){
        let url = 'https://ropa-americana-55547-default-rtdb.firebaseio.com/categorias/ropaHombre.json';
        fetch(url)
            .then( response => response.json() )
            .then( data => mostrarData(data) )
            .catch( error => console.log(error) )
        const mostrarData = (data) => {
            let i=0;
            
            while(i<data.length){
                console.log(data[i].nombre);
                document.getElementById("nom"+i).innerHTML = data[i].nombre;
                document.getElementById("desc"+i).innerHTML = data[i].descripcion;
                document.getElementById("talla"+i).innerHTML = "Talla: " + data[i].talla;
                document.getElementById("precio"+i).innerHTML = "Precio: " + data[i].precio;
                i=i+1
            };
        };
    });

    $("#linkMujer").click(function(){
        
        let url = 'https://ropa-americana-55547-default-rtdb.firebaseio.com/categorias/ropaMujer.json';
        fetch(url)
            .then( response => response.json() )
            .then( data => mostrarData(data) )
            .catch( error => console.log(error) )
        const mostrarData = (data) => {
            let i=0;
            
            while(i<data.length){
                console.log(data[i].nombre);
                document.getElementById("nom"+i).innerHTML = data[i].nombre;
                document.getElementById("desc"+i).innerHTML = data[i].descripcion;
                document.getElementById("talla"+i).innerHTML = "Talla: " + data[i].talla;
                document.getElementById("precio"+i).innerHTML = "Precio: " + data[i].precio;
                i=i+1
            };
        };
    });

    $("#linkInfantil").click(function(){
        let url = 'https://ropa-americana-55547-default-rtdb.firebaseio.com/categorias/ropaInfantil.json';
        fetch(url)
            .then( response => response.json() )
            .then( data => mostrarData(data) )
            .catch( error => console.log(error) )
        const mostrarData = (data) => {
            let i=0;
            
            while(i<data.length){
                console.log(data[i].nombre);
                document.getElementById("nom"+i).innerHTML = data[i].nombre;
                document.getElementById("desc"+i).innerHTML = data[i].descripcion;
                document.getElementById("talla"+i).innerHTML = "Talla: " + data[i].talla;
                document.getElementById("precio"+i).innerHTML = "Precio: " + data[i].precio;
                i=i+1
            };
        };
    });

    $("#linkUnisex").click(function(){

        let url = 'https://ropa-americana-55547-default-rtdb.firebaseio.com/categorias/ropaUnisex.json';
        fetch(url)
            .then( response => response.json() )
            .then( data => mostrarData(data) )
            .catch( error => console.log(error) )
        const mostrarData = (data) => {
            let i=0;
            
            while(i<data.length){
                console.log(data[i].nombre);
                document.getElementById("nom"+i).innerHTML = data[i].nombre;
                document.getElementById("desc"+i).innerHTML = data[i].descripcion;
                document.getElementById("talla"+i).innerHTML = "Talla: " + data[i].talla;
                document.getElementById("precio"+i).innerHTML = "Precio: " + data[i].precio;
                i=i+1
            };
        };
    });
});
/*Validacion correos y contraseñas 
$(document).ready(function(){
    $("#error1").hide();
    $("#error2").hide();
    $("#error3").hide();
    
    $("#enviar").click(function() {
        let email = $("#email").val();
        let password1 = $("#password1").val();
        let password2 = $("#password2").val();
        let expr = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (email == "" || !expr.test(email)){
            $("#error1").show();
            return false;
        }else{
            $("#error1").hide();
            if (password1.length < 12){
                $("#error2").show();
                return false;
            }else{
                $("#error2").hide();
                if (password2.length < 12 || password2 != password1){
                    $("#error3").show()
                    return false;
                }else{
                    $("#error3").hide()
                    alert("USUARIO REGISTRADO EXITOSAMENTE")
                };
            };
        };
    });
});*/


