n = int(input("Enter number of terms: "))
a, b = 0, 1
print("Fibonacci Sequence:")
for i in range(n):
    print(a, end=", ")
    a, b = b, a + b