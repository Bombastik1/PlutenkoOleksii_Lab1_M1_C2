1a = float(input("Введіть значення а (1 ≤ а ≤ 100): "))
while (a > 100 or a < 1):
    a = float(input("Будь ласка, введіть значення a в діапазоні від 1 до 100: "))

b = float(input("Введіть значення b (1 ≤ b ≤ 100): "))
while (b > 100 or b < 1):
    b = float(input("Будь ласка, введіть значення b в діапазоні від 1 до 100: "))

if (a > b):
    x = 2 * a + b
elif (a < b):
    x = (a - 5) / b
else:
    x = -2

print(x)
