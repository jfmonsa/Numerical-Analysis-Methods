import numpy as np
from sympy import *
import matplotlib.pyplot as plt
x = Symbol("x")

def lagrange_pol(points):
    n = len(points)
    pol = 0
    for i in range(n):
        num=1
        denom=1
        for j in range(n):
            if j != i:
                num *= (x - points[j][0])
                denom *= (points[i][0] - points[j][0])
        l_term = num / denom
        pol += l_term * points[i][1]
    return pol


def lagrange_method_main(points):
    arr_x = [point[0] for point in points]
    arr_y = [point[1] for point in points]

    #gen values
    pol = lagrange_pol(points)
    expand_pol = pol.expand()
    pol_lambda = lambdify(x,expand_pol)
    
    number_points = 100
    min_x = min(arr_x)
    max_x = max(arr_x)

    #generando array de puntos para graficar
    arr_px = np.linspace(min_x, max_x, number_points)
    arr_py = pol_lambda(arr_px)

    #graph
    plt.subplots(figsize=(15, 8))
    plt.plot(arr_x, arr_y, "o", label="Points")
    plt.plot(arr_px, arr_py, label="Polynomial")
    plt.legend("Langrange Interpolation Method")
    plt.grid(1)
    plt.xlabel("x")
    plt.ylabel("y")
    pol_str = f"Lagrange Polynomial:\n${latex(expand_pol)}$ given the points {points}"
    plt.text(max_x-2.3, max_x+5.5, pol_str, fontsize=12, verticalalignment='top',horizontalalignment="left")
    plt.title(f"Langrange Interpolation Method")
    plt.show()

if __name__ == "__main__":
    # Ejemplo de uso
    #ejemplo del polinomio de la suma de los numeros naturales S(n)=n(n+1)/2

    points = [(1, 1), (2, 3), (3, 6),(4,10)]
    lagrange_method_main(points)