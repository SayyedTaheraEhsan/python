# Square with only one empty cell inside

n = int(input("Enter size of square: "))

# Position of the empty space (row, col)
empty_row = n // 2   # middle row
empty_col = n // 2   # middle column

for i in range(n):
    for j in range(n):
        if i == empty_row and j == empty_col:
            print(" ", end=" ")  # leave only one space
        else:
            print("*", end=" ")
    print()
