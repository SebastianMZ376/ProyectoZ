<?php

    include_once("funcionesR.php");

    $objeto = new Objeto;
    $crud = new CRUD;

    $nombre = $_POST['nombres'];
    $telefono = $_POST['telefono'];
    $salon = $_POST['salon']
    $edificio = $_POST['edificio'];
    $email = $_POST['correo'];
    $pswrd = $_POST['password'];
    $accion = $_POST['cmbAccion'];

    $objeto->nombre = $nombre;
    $objeto->telefono = $telefono;
    $objeto->salon = $salon;
    $objeto->edificio = $edificio;
    $objeto->email = $email;
    $objeto->pswrd = $pswrd;

    if ($accion == 'registrarr') {
        $crud->RegistrarUsuario($objeto);
    } else if ($accion == 'eliminar'){
        $crud->EliminarUsuario($nombre);
    }


}
?>