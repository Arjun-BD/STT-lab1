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

VALUE = 19
COUNTER = 0
while COUNTER < 10:
    VALUE += 1
    print(VALUE)
    COUNTER += 1

# Let's add some good code below again

X = 18
Y = X + 18
Y = X * X
X = Y | (Y - 1)
print(X, Y)
