def fib(limit):
    cursor = 0
    num1 = 0
    num2 = 1
    while cursor < limit:
        yield num1
        num1, num2 = num2, num1 + num2
        cursor += 1


F = fib(10)
for i in F:
    print(i)
