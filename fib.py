def fibonacci(x,y):
    while True:
        yield x
        x, y = y, x + y

# Accepting  input
n = int(input("Input the number of Fibonacci numbers you want to generate? "))
x=int(input("Enter first number "))
y=int(input("Enter second number "))

print("Number of first ",n,"Fibonacci numbers: ")

fib = fibonacci(x,y)
for _ in range(n):
    print(next(fib),end=" ")
