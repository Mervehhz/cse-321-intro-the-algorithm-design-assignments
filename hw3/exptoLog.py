def pow(a, n):
    if n == 0:
        return 1
    half = pow(a, n//2)
    if n % 2 == 0:
        return half * half
    else:
        return a * half * half