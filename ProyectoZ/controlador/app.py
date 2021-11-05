from flask import Flask,render_template
app = Flask(__name__, template_folder='../vista',static_folder='../static')

@app.route('/')
def main():
    return render_template('Login.html')

@app.route('/index')
def maini():
    return render_template('comunes/index.html')

@app.route('/envio')
def cin():
    return render_template('Pedidos/envio.html')

@app.route('/indexx')
def pedidos():
    return render_template('Pedidos/indexx.html')

@app.route('/Carrito')
def Carrito():
    return render_template('/Carrito/Carrito.html')

@app.route('/Categorias')
def Categoria():
    return render_template('Categoria/Categorias.html')

@app.route('/ConsulCategoria')
def Consulta():
    return render_template('Categoria/ConsultarCategoria.html')

@app.route('/EditarCategoria')
def Editarr():
    return render_template('Categoria/EditarCategoria.html')

@app.route('/RegistroCuenta')
def registtro():
    return render_template('/RegistroUsuario/RegistroCuenta.html')

@app.route('/EditarC')
def editarcuenta():
    return render_template('/RegistroUsuario/EditarCuenta.html')

@app.route('/Usuarios')
def user():
    return render_template('/Usuarios/usuarios.html')
if __name__ == '__main__':
    app.run(debug=True)

