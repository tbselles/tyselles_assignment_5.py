# === Challenge 1: Collatz Conjecture ===
print("=== Challenge 1: Collatz Conjecture ===")
start = int(input("Enter starting number: "))

# Generate the Collatz sequence until reaching 1
print("Sequence:", end=" ")
steps = 0
n = start
while n != 1:
    print(n, end=" ")
    if n % 2 == 0:     # even: divide by 2
        n //= 2
    else:              # odd: multiply by 3 and add 1
        n = 3*n + 1
    steps += 1
print(1)
print(f"Steps: {steps}")
# === Challenge 2: Prime Number Checker ===
print("=== Challenge 2: Prime Number Checker ===")
num = int(input("Enter a number: "))

# Check divisibility from 2 up to num-1
print(f"Testing divisors from 2 to {num-1}...")
is_prime = True
for divisor in range(2, num):
    if num % divisor == 0:  # found a divisor → not prime
        print(f"{num} is not prime (divisible by {divisor})")
        is_prime = False
        break
if is_prime:
    print(f"{num} is prime!")

