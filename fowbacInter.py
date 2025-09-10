def forward_difference_table(x, y):
    n = len(y)
    table = [y.copy()]
    for i in range(1, n):
        diff = []
        for j in range(n - i):
            diff.append(table[i-1][j+1] - table[i-1][j])
        table.append(diff)
    return table

def print_difference_table(x, table, name="Forward Difference Table"):
    print(f"\n{name}:")
    n = len(x)
    for i in range(n):
        print(f"x={x[i]:<5} ", end="")
        for j in range(len(table)):
            if i < len(table[j]):
                print(f"{table[j][i]:<10}", end=" ")
        print()

def newton_forward(x, y, value):
    n = len(x)
    table = forward_difference_table(x, y)
    h = x[1] - x[0]
    p = (value - x[0]) / h

    result = y[0]
    fact = 1
    p_term = 1
    formula_str = f"y = {y[0]}"
    for i in range(1, n):
        fact *= i
        p_term *= (p - (i-1))
        term = (p_term / fact) * table[i][0]
        result += term
        formula_str += f" + ({p_term:.4f}/{fact})*{table[i][0]}"
    return result, formula_str

def newton_backward(x, y, value):
    n = len(x)
    table = forward_difference_table(x, y)
    h = x[1] - x[0]
    p = (value - x[-1]) / h

    result = y[-1]
    fact = 1
    p_term = 1
    formula_str = f"y = {y[-1]}"
    for i in range(1, n):
        fact *= i
        p_term *= (p + (i-1))
        term = (p_term / fact) * table[i][-1]
        result += term
        formula_str += f" + ({p_term:.4f}/{fact})*{table[i][-1]}"
    return result, formula_str

# ------------------ MAIN PROGRAM ------------------

# Ask number of elements
n = int(input("Enter number of data points (n): "))

# Input values
x = []
y = []
print("Enter x values:")
for i in range(n):
    x.append(float(input(f"x[{i}] = ")))

print("Enter y values:")
for i in range(n):
    y.append(float(input(f"y[{i}] = ")))

# Build table
table = forward_difference_table(x, y)
print_difference_table(x, table)

# Interpolation point
value = float(input("\nEnter the value of x to interpolate: "))

# Results
f_result, f_formula = newton_forward(x, y, value)
b_result, b_formula = newton_backward(x, y, value)

print(f"\nNewton Forward Interpolation Formula at x={value}:")
print(f_formula)
print(f"Result = {f_result}")

print(f"\nNewton Backward Interpolation Formula at x={value}:")
print(b_formula)
print(f"Result = {b_result}")
