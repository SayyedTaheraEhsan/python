# 1. Print numbers from 1 to 5
print("1. Numbers from 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print("\n")

# 2. Sum of numbers in a list
print("2. Sum of list numbers:")
numbers = [2, 4, 6, 8, 10]
total = 0
for n in numbers:
    total += n
print("Sum =", total)
print()

# 3. Factorial of a number
print("3. Factorial of 5:")
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial =", fact)
print()

# 4. Print characters of a string
print("4. Characters in a string:")
text = "HELLO"
for ch in text:
    print(ch, end=" ")
print("\n")

# 5. Nested for loop (Multiplication table)
print("5. Multiplication table (1 to 3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", i*j)
    print("-----")
