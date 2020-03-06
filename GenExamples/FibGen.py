def fibonacci():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current


fib = fibonacci()

# for i in fib:
#     print(i)

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))


