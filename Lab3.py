n = int(input("Будь ласка, введіть ціле число (1 < N < 9): "))
line = ""
while n < 1 or n > 9:
    line += "!"
    n = int(input(f"Будь ласка, введіть ціле число (1 < N < 9 {line}): "))

for i in range(1, n + 1):
    print("  " * (n - i), end="")

    for j in range(n, n - i, -1):
        print(j, end=" ")

    print()