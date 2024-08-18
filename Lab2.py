line = ""

for i in range(1, 21, 1):
    if i % 3 == 0:
        line += "«"
    else:
        line += "*"

print(line)