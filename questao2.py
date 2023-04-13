x = int(input())

previous_fib_n = 0
fib_n = 1

while ( fib_n < x):
    temp = fib_n
    fib_n = fib_n + previous_fib_n
    previous_fib_n = temp


if ( x == fib_n):
    print ("O número pertence à sequência de Fibonacci.")
else:
    print ("O número não pertence à sequencia de Fibonacci.")
