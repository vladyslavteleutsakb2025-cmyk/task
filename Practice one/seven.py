#Числа - цілі від 1 до 1000
# наприклад маємо 3 і 6, якщо відняти одне від одного
a = int(input("Введіть ціле число: "))
b = int(input("Введіть ціле число: "))

# c = a - b > 0
# print(c, a)
#
# c = b - a > 0
# print(c, b)

resl = (b, a)[a > b]
print(resl)

print(max(a, b))