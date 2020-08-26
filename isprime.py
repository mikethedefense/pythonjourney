# Write a function that returns if an integer is prime

def is_prime(n):
    if n == 1:
        return False
    for d in range(2,n):
        if n % d == 0:
            return False
        else:
            return True

print(is_prime(4)) # Test other numbers
