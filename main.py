import math


def delta(a, b, c):
    result = (b*b) - (4*a*c)
    return result


def bhaskara(a, b, c):
    deltaResult = delta(a, b, c)
    if deltaResult < 0:
        return "Delta Negativo"
    triforce = math.sqrt(deltaResult)
    firstX = (-b + triforce) / (2*a)
    secondX = (-b - triforce) / (2*a)
    return f"x1={round(firstX, 2)}, x2={round(secondX, 2)}"


print(bhaskara(7, 3, 4))
print(bhaskara(1, 5, 2))
print(bhaskara(3, 10, 2))
