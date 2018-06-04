"""Write a Decorator named after5 that will ignore the decorated function in the first 5 times it is called. Example Usage:
@after5
def doit(): print("Yo!")
# ignore the first 5 calls
doit()
doit()
doit()
doit()
doit()

# so only print yo once
doit()


please make a similar one, but that acceps times to skip as param (@after(<times_to_skip>))

=========================

Calculation in the following fib function may take a long time. Implement a Decorator that remembers old calculations so the function won't calculate a fib value more than once. Program Code:
@memoize
def fib(n):
    print("fib({})".format(n))
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

Expected Output:
fib(10)
fib(9)
fib(8)
fib(7)
fib(6)
fib(5)
fib(4)
fib(3)
fib(2)
fib(1)
55

=======================

Write a decorator called accepts that checks if a function was called with correct argument types. Usage example:
# make sure function can only be called with a float and an int
@accepts(float, int)
def pow(base, exp):
  pass

# raise AssertionError
pow('x', 10)

========================

Write a decorator called returns that checks that a function returns expected argument type. Usage example:
@returns(str)
def same(word)
  return word

# works:
same('hello')

# raise AssertionError:
same(10)

=========================

Write a decorator named logger. It should log function calls and execution
time (for example: function f was called w/ params <a, b> and  took <time> to execute). Decorator may accept argument file - file to write logs to. If no param was provided - simply print logs to console.
Decorator should be implemented as a class.
"""
