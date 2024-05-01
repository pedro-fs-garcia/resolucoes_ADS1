import math

x = math.pi*0.5


def cos(x, k):
    soma = 0
    a, b = 1, 1
    for i in range(1, 2*k+1):
        soma += a/b
        a *= (-1)*x*x
        b = b*(2*i-1)*(2*i)
    return soma
print(cos(math.pi/3, 15))
print(math.cos(math.pi/2))
print("---")


def sen(x, k):
    sen = 0
    a, b = x, 1
    for i in range(2*k):
        sen = sen + (a/b)
        a = a*x**2*(-1)
        b *= (2*i + 2)*(2*i +3)
    return sen
print(f"seno(x) = {sen(math.pi, 10)}")
print(math.sin(math.pi))
print("---")


def e_to_the_X(x, k):
    e = 1
    a, b = x, 1
    for i in range(1, k):
        e += a/b
        a = a*x
        b = b*(i+1)
    return e
print(e_to_the_X(2, 20))
print(math.exp(2))
print("---")

def one_over (x, k):
    s = 1
    a = x
    for i in range(1, k):
        s += a
        a *= x
    return s
print(one_over(0.5, 10))
print("---")

def ln_1_plus_x(x):
    ln = 0
    a, b = x, 1
    for i in range(100):
        ln += a/b
        a = a*(-x)
        b += 1
    return ln
print(ln_1_plus_x(0.6))
print(math.log1p(0.6))
print("---")

def arctan(x):
    tan = 0
    a, b = x, 1
    for i in range (20):
        tan += a/b
        a *= (-1)*(x**2)
        b += 2
    return tan
print(arctan(0.5))
print(math.atan(0.5))
print("---")

