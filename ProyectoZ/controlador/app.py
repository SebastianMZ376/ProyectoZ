from flask import Flask,render_template
app = Flask(__name__, template_folder='../vista',static_folder='../static')

@app.route('/')
def main():
    return render_template('comunes/index.html')

@app.route('/Usuarios')
def user():
    return render_template('/Usuarios/usuarios.html')
if __name__ == '__main__':
    app.run(debug=True)

