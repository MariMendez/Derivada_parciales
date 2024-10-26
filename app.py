from flask import Flask, render_template, request
import math

app = Flask(__name__)


def calcular_gradiente(x, y):
    denominador = 3 * x * y + 2 * x ** 2 - y
    derivada_x = (3 * y + 4 * x) / denominador
    derivada_y = (3 * x - 1) / denominador
    return derivada_x, derivada_y


def producto_punto(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))

# Función para calcular la dirección constante
def direccion_constante(gradiente):
    return (-gradiente[1], gradiente[0])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    # Obtener los valores de x e y desde el formulario
    x = float(request.form['x'])
    y = float(request.form['y'])
    
    # Calcular el gradiente en el punto (1,2)
    grad_x, grad_y = calcular_gradiente(x, y)
    
    # Apartado a: Dirección de mayor aumento de temperatura
    direccion_mayor_aumento = (grad_x, grad_y)
    
    # Apartado b: Calcular el producto punto para la dirección equivocada (1, -1/2)
    direccion_equivocada = (1, -0.5)
    cambio_temp = producto_punto(direccion_mayor_aumento, direccion_equivocada)
    
    # Apartado c: Dirección de temperatura constante
    direccion_constante_temp = direccion_constante((grad_x, grad_y))

    return render_template('resultado.html', 
                           gradiente_x=grad_x, gradiente_y=grad_y, 
                           cambio_temp=cambio_temp, 
                           direccion_constante_x=direccion_constante_temp[0], 
                           direccion_constante_y=direccion_constante_temp[1])

if __name__ == '__main__':
    app.run(debug=True)
