from typing import Callable
from simpy import Symbol, diff, lambdify, sympify  # symbols


def newton_raphson():
    func = input("Ingrese la función en términos de 'x': ")

    # Convertir la entrada del usuario a una expresión simbólica
    x = Symbol("x")
    funcion = sympify(func)

    # Calcular la derivada
    derivada = diff(funcion, x)

    # Convertir la expresión simbólica a una función lambda
    func = lambdify(x, funcion, "numpy")
    deriv = lambdify(x, derivada, "numpy")

    # Solicitar otros valores necesarios para Newton-Raphson
    p0 = float(input("Ingrese el valor inicial p0: "))
    # tol = float(input("Ingrese la tolerancia: "))
    # max_iter = int(input("Ingrese el número máximo de iteraciones: "))

    root = aux_newton_raphson(func, deriv, p0)


def aux_newton_raphson(
    func: Callable,
    deriv: Callable,
    p0: float | int,
    tol: float | int = 1e-6,
    max_iter: float | int = 1000,
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
        if p == 0 or abs(p - p0) < tol:
            print(f"Procedure was succesful root  is equal to x = {p}")
            return p
        else:
            i += 1
            p0 = p
    else:
        raise Exception(f"No convergence, N iterations {i}")


# tests
if __name__ == "__main__":
    newton_raphson()
