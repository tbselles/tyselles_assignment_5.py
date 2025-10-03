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

