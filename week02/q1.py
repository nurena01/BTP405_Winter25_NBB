
# Write a Python function called getFibonacciNumbers(n) that generates a 
# list of all Fibonacci numbers less than or equal to n. Fibonacci numbers are defined
# as: • F_0 = 0 • F_1 = 1 • F_n = F_{n-1} + F_{n-2} for n \geq 2

# For example:
# getFibonacciNumbers(10)
# Output: [0, 1, 1, 2, 3, 5, 8]

# ANSWER:

def getFibonacciNumbers(n): # -> n = 10, it is the parameter number, the argum
    if n < 0: #if n is less then 0 then return 0
        return[] #return 0
    
    fib_num = [0,1]
    
    while True:
        next_fib = fib_num[-1] + fib_num[-2]
        if next_fib > n:
            break
        fib_num.append(next_fib)
    return fib_num if n >= 1 else [0]

print(getFibonacciNumbers(10))
