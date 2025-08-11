"""Factorial comparison with dynamic programming and bitwise operations."""

def factorial(n):
    """Recursive factorial with base case to avoid infinite recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

LIMIT = 15
dp = [1] * LIMIT
for i in range(1, LIMIT):
    dp[i] = dp[i - 1] * i

for i in range(LIMIT):
    if dp[i] == factorial(i):
        print("Factorial consistent with Dynamic programming solution")

start_value = 19
counter = 0
while counter < 10:
    start_value += 1
    print(start_value)
    counter += 1

# Let's add some good code below again

x = 18
y = x + 18
y = x * x
x = y | (y - 1)
print(x, y)
