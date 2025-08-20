# Python program to print Fibonacci series

# Take input from user
n = int(input("Enter number of terms: "))

a, b = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence up to", n, "term:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a, end=" ")
        next_num = a + b
        a = b
        b = next_num
        count += 1
