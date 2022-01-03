<?php //Conexion y Funciones de registro

    class CRUD {
        private $servidor = 'localhost';
        private $usuario  = 'root';
        private $contraseña = '';
        private $baseDeDatos = 'quicksnack';

        private function ConectarBD(){
            $conexion = mysql_connect(this->servidor, this->usuario, this->contraseña, this->baseDeDatos) or die ("error al conectar con la bd");

            return $conexion;
        }

        private function CerrarConexion($conexion){
            mysql_close();
        }

        public function RegistrarUsuario($objeto){
            $conexion = this->ConectarBD();
            $insertar = "INSERT INTO quicksnack VALUES ('$objeto->nombre','$objeto->telefono','$objeto->salon','$objeto->edificio','$objeto->email','$objeto->pswrd')";

            mysqli_query($conexion, $insertar) or die("Error al registrar el usuario");
            echo "Registro Agregado Correctamente";

            this->CerrarConexion($conexion);
        }

        public function EliminarUsuarios($){
            $conexion = $this->ConectarBD();
            $eliminar = "DELETE FROM quicksnack WHERE clave = '$nombre'";
            mysqli_query($conexion, $eliminar) or die ("Error al eliminar el usuario");

            echo "Registro Eliminado Correctamente";
            $this->CerrarConexion($conexion);
        }
 }
    class Objeto{}
?>