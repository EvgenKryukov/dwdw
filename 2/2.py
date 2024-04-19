(Часть 1)
x = 1  # Замените значение x на то, которое вы хотите проверить

if -2 <= x <= 3:
    print("Точка x принадлежит интервалу [-2;3]")
else:
    print("Точка x не принадлежит интервалу [-2;3]")

№2
x = -5  # Замените значение x на то, которое вы хотите проверить

if (-10 <= x <= -2) or (4 <= x <= 8):
    print(f"Точка x = {x} принадлежит интервалу [-10;-2]U[4;8]")
else:
    print(f"Точка x = {x} не принадлежит интервалу [-10;-2]U[4;8]")

(Часть 2)
import math

def solve_quadratic_equation(t):
    a = t - 5
    b = -3*t
    c = 2*(t-3)
    
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant))/(2*a)
        x2 = (-b - math.sqrt(discriminant))/(2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x,
    else:
        return "нет корней"

# Интервал перебора чисел
for t in range(-10, 11):
    roots = solve_quadratic_equation(t)
    print(f"При t = {t}, корни уравнения:", roots)


