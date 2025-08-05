# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):  # Only go up to square root of the number
        if number % i == 0:
            return False
    return True

# Input from user
num = int(input("Enter a number: "))

# Check and display result
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
