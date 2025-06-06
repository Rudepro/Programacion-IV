from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html', nombre='Estudiante', apellido='Pythonista')

if __name__ == '__main__':
    app.run(debug=True)
