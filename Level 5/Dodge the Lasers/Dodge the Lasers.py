from decimal import *


def solution(s):
    getcontext().prec = 101
    sqrt2 = Decimal(2).sqrt()
    sqrt2m1 = sqrt2 - 1
    googol = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    sqrti = int(sqrt2m1 * googol)
    param = int(s)

    def convert(nprime, lenprime, lenroot):
        nprime = int(str(nprime)[:lenprime - lenroot])
        return nprime

    def calculate(n):
        if n == 0:
            return 0
        else:
            nprime = int(sqrti * n)
            if len(str(nprime)) > len(str(sqrti)):
                lenprime = len(str(nprime))
                lenroot = len(str(sqrti))
                nprime = convert(nprime, lenprime, lenroot)
            else:
                nprime = 0
        return (n * nprime) + n * (n + 1) / 2 - nprime * (nprime + 1) / 2 - calculate(nprime)

    answer = calculate(param)
    return str(answer)
