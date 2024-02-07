import time

total = 0
def sum(num):
    if num == 1:
        return 1
    else:
        return num + sum(num-1)

print(sum(5))

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
    
print(factorial(4))

#FUNCTION Factorial(Num: INTEGER) RETURNS INTEGER
#   IF Num = 1 THEN
#       RETURN 1
#   ELSE
#       RETURN Num * Factorial(Num-1)
#   ENDIF
#ENDFUNCTION

def compound_interest(principal, interest, years):
    if years == 0:
        return principal
    else:
        return (1 + interest) * compound_interest(principal, interest, years - 1) 
    
print(compound_interest(10, 0.03, 3))

def collatz(num):
    if num == 1:
        return 0
    if (num % 2) == 0:
        return 1 + collatz(num//2)
    else:
        return 1 + collatz(num//3)

print(collatz(13))
    
def fib(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
st = time.time()
print(fib(4))

et = time.time()

print(et-st)