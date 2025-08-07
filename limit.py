from sympy import symbols, tan, limit

# Define the variable
x = symbols('x')

# Define the expression
expr = (tan(5*x) - 5*x) / x**3

# Calculate the limit as x approaches 0
lim = limit(expr, x, 0)

# Print the result
print("The limit is:", lim)
