from collections import Counter
from math import factorial, gcd
from fractions import Fraction


def cycidx(n):
    lisn = [Counter(nlis) for nlis in accel_asc(n)]
    return [(coeff(term.items()), term) for term in lisn]


def accel_asc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]


def combine(cyca, cycb):
    comb = 0
    for i in cyca:
        for j in cycb:
            comb += gcd(i, j) * cyca[i] * cycb[j]
    return comb


def coeff(term):
    val = 1
    for x, y in term:
        val *= factorial(y) * x ** y
    return Fraction(1, val)


def solution(w, h, s):
    total = 0
    ccols = cycidx(w)
    crows = cycidx(h)
    for ccoeff, ccycle in ccols:
        for rcoeff, rcycle in crows:
            multiplier = ccoeff * rcoeff
            cycles = combine(ccycle, rcycle)
            count = 1
            count *= s ** cycles
            total += multiplier * count
    return str(total)
