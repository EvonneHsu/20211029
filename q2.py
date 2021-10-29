def is_prime(n):
    for i in range(2,n):
        if n % i== 0:
            return False
    return Ture
n=int(input('Input a number: '))
for i in range(2,n+1):
    i is_prime =is_prime(i)
    if i is_prime:
        print(i)
