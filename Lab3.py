n = 5
for i in range(1, n + 1):
    line = ""
    for j in range(n - i + 1, n + 1):
        line += str(j)
    print(line)