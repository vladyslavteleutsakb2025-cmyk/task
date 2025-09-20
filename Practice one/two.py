import math

a = int(input("Введіть ціле число: "))
b = int(input("Введіть друге ціле число: "))

sum_n = a + b
print(f"Сума: {sum_n}")

d = a - b
print(f"Різниця: {d}")

m = a * b
print(f"Добуток: {m}")

x_sum = (a + b) / 2
print(f"Середнє арифметичне значення: {x_sum}")

g = math.sqrt(m)
print(f"Середнє геометричне значення (корінь з добутку): {g}")

distance = abs(a - b)
print(f"Відстань (абсолютне значення різниці): {distance}")

max_number = max(a, b)
print(f"Максимум: {max_number}")

min_number = min(a, b)
print(f"Мінімум: {min_number}")

sum_square = (a ** 2) + (b ** 2)
print(f"Суму квадратів: {sum_square}")

square_sum = (a + b) ** 2
print(f"Квадрат суми: {square_sum}")

degree = a ** b
print(f"а в степені b: {degree}")