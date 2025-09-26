import math

s_0 = int(input("Введіть ціле число: "))
v_0 = int(input("Введіть ціле число: "))
t = int(input("Введіть ціле число: "))
g = int(input("Введіть ціле число: "))


s = s_0 + (v_0 * t) + ((g * (t ** 2)) / 2) # перша формула
print(f"Результат: {s}")

a = int(input("Введіть ціле число: "))
p = int(input("Введіть ціле число: "))
m_1 = int(input("Введіть ціле число: "))
m_2 = int(input("Введіть ціле число: "))

G = 4 * (math.pi ** 2) * (a ** 3 / ((p ** 2) * (m_1 + m_2)))
print(f"Результат: {G}")


PV = int(input("Введіть ціле число: "))
INT = int(input("Введіть ціле число: "))
YRS = int(input("Введіть ціле число: "))

FV = PV * (1 + ((INT / 100) ** YRS))
print(f"Результат: {FV}")


a_four = int(input("Введіть ціле число: "))
b_four = int(input("Введіть ціле число: "))
y_four = int(input("Введіть ціле число: "))

c = math.sqrt((a_four ** 2) + (b_four ** 2) - (2 * a_four * b_four * math.cos(y_four)))
print(f"Результат: {c}")
