from typing import Callable
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, diff, lambdify

def newton_raphson():

    x = symbols('x')
    func = lambda x: x**3+4*(x**2)-10

    # Calcular la derivada
    deriv = diff(func(x), x)

    # Crear una nueva función lambda para la derivada
    deriv = lambdify(x, deriv)

    # Solicitar otros valores necesarios para Newton-Raphson
    p0 = float(input("Ingrese el valor inicial p0: "))
    # tol = float(input("Ingrese la tolerancia: "))
    # max_iter = int(input("Ingrese el número máximo de iteraciones: "))

    root = aux_newton_raphson(func, deriv, p0)
    graph(func,root,round(root)-1,round(root)+1)


def aux_newton_raphson(
    func: Callable,
    deriv: Callable,
    p0: float | int,
    tol: float | int = 1e-6,
    max_iter: float | int = 100,
) -> float | None:
    """
    Aplica el método de Newton-Raphson para encontrar la raíz de una función "func".

    Args:
        func: (Callable): Función para la cual se busca la raíz.
        deriv: (Callable): Derivada de la función `func`.
        p0: (float | int): Valor inicial para comenzar la búsqueda de la raíz.
        tol: (float | int), optional): Tolerancia para la convergencia. Valor predeterminado es 1e-6.
        max_iter: (float, | int; optional): Número máximo de iteraciones. Valor predeterminado es 1000.

    Returns:
       float | None: Aproximación de la raíz encontrada o None si no se alcanza la convergencia.

    Raises:
        ValueError: Si el número máximo de iteraciones es alcanzado sin convergencia.

    Examples:
        >>> newton_raphson(lambda x: x**2 - 4, lambda x: 2*x, 2)
        2.000000000001818
    """

    i = 1
    while i <= max_iter:
        # compute p
        p = p0 - func(p0) / deriv(p0)
        # Stop conditions according to book Numerical Analysis (p. 68)
        if (
            abs(p - p0) < tol
            or abs(func(p)) < tol
            or (p != 0 and abs((p - p0) / p) < tol)
        ):
            # TODO: imprimir cual fue la tolerancia
            print(f"Procedure was successful, root  is equal to x = {p}, iterations: {i}, tolerance: {tol}, error: {abs(p - p0)}")
            return p
        else:
            p0 = p
            i += 1
    else:
        raise Exception(f"No convergence, N iterations {i}")

def graph(func,root,x_min,x_max):
    xvalues = np.linspace(x_min,x_max,100)
    yvalues = func(xvalues)

    plt.plot(xvalues,yvalues)
    plt.plot(root,func(root),marker=".")
    plt.legend("Newthon raphson method")
    x=symbols("x")
    func_l = str(func(x))
    pol_str = f"Newthon raphson method: given polynomial \n${func_l}$"
    plt.text(x_max-1.8, x_max+5.6, pol_str, fontsize=12, verticalalignment='top',horizontalalignment="left")
    plt.title(f"Newthon raphson method")
    plt.annotate(f"Apr root: ({root}, {func(root)})", (root+0.05,func(root)+0.2))

    #plt.axhline(y=func(root), color='red', linestyle='--')
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.axvline(x=root, color='red', linestyle='--')
    plt.show()

# tests
if __name__ == "__main__":
    newton_raphson()

# Numerical Analysis book: https://faculty.ksu.edu.sa/sites/default/files/numerical_analysis_9th.pdf
# TODO: revisar https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.newton.html
# TODO: Pomer comentarios en ingles, porque si xddddd
# TODO: imprimir la grafica y la raíz calculada con matplotlib https://www.youtube.com/watch?v=T3q0hZjXG3g
# TODO: Si nos queremos complicar la vida, se podría imprmir una tabla del método
"""
Enlaces para el informe:
* https://pythonnumericalmethods.berkeley.edu/notebooks/chapter19.04-Newton-Raphson-Method.html

"""
