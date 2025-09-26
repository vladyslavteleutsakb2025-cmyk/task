import math
a = int(input("Введіть ціле число: "))
b = int(input("Введіть ціле число: "))
c = int(input("Введіть ціле число: "))

#ax^2 + bx + c = 0

d = b ** 2 - 4 * a * c

d_sqrt = math.sqrt(d)

x_one = ((b * (-1)) + d_sqrt) / (a * 2)
x_two = ((b * (-1)) - d_sqrt) / (a * 2)

print(f"Перший корінь:{x_one:.2f}\nДругий корінь:{x_two:.2f}")


