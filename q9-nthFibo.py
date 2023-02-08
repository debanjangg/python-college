def fibo(n):
    if n <= 1:
        return D[n]
    D[n-1] = fibo(n-1)
    D[n-2] = fibo(n-2)
    D['count'] += 2
    return D[n-1] + D[n-2]

D = {0: 0, 1: 1, 'count': 0}
n = int(input('Enter n: '))
print(f'\nTerm {n} of Fibonacci Sequence: {fibo(n)}')
print(f'Number of recursive calls being made: {D["count"]}')