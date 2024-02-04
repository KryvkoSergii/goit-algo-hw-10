import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def function(x):
    return x**2 + 3*x

def check_calc(func, a, b):
    result, error = spi.quad(func, a, b)
    return result, error

def monte_carlo_integral(n_samples, lower_bound, upper_bound):
    total = 0

    for _ in range(n_samples):
        x = np.random.uniform(lower_bound, upper_bound)
        total += function(x)

    average = total / n_samples
    integral_approximation = average * (upper_bound - lower_bound)

    return integral_approximation

# Задання інтервалу для обчислення інтегралу
lower_bound, upper_bound = 0, 5

# Кількість випробувань (збільште для точнішого результату)
n_samples = 10000

# Оцінка інтегралу методом Монте-Карло
integral_approximation = monte_carlo_integral(n_samples, lower_bound, upper_bound)

print(f"Monte Carlo Integral Approximation: {integral_approximation}")

test_area = check_calc(function, lower_bound, upper_bound)

print(f"Test Area: {test_area}")