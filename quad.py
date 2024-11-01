def QuadraticFormula(a, b, c):
    d = (b**2) - (4 * a * c)
    x1 = (-b + d**0.5) / (2 * a)
    x2 = (-b - d**0.5) / (2 * a)
    return x1, x2


def QFSister(a, b, c):
    u = (b**2 / (4 * a**2) - c / a) ** 0.5
    x1 = -b / (2 * a) + u
    x2 = -b / (2 * a) - u
    return x1, x2


def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    x1, x2 = QuadraticFormula(a, b, c)
    r1, r2 = QFSister(a, b, c)
    print(x1, x2)
    print(r1, r2)


main()
