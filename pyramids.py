rows = int(input("Enter number of rows: "))

# Upward pyramid
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("* " * i)

# Downward pyramid
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    print("* " * i)
