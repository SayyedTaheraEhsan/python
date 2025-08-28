# Program to demonstrate logical operators in Python

# Take input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Logical AND
print("\n--- Logical AND ---")
print(a > 0 and b > 0)   # True only if both are positive
print(a < 0 and b < 0)   # True only if both are negative

# Logical OR
print("\n--- Logical OR ---")
print(a > 0 or b > 0)    # True if at least one is positive
print(a < 0 or b < 0)    # True if at least one is negative

# Logical NOT
print("\n--- Logical NOT ---")
print(not (a > b))       # True if a is NOT greater than b
print(not (a == b))      # True if a is NOT equal to b
