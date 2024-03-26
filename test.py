##задание1
import math
def circle(radius):
    return math.pi * radius**2
def triangle(a,b,c):
    n = [a, b, c]
    n.sort()
    if ((n[0] ** 2) + (n[1] ** 2) == n[2] ** 2):
        print("Данный треугольник является прямоугльным")
    p = (a + b + c)/2.0
    area = (p*(p-a)*(p-b)*(p-c))
    return math.sqrt(area)
def main():
    choice = 0
    while choice != 3:
        print("Найти площадь:\n1\tКруга\n2\tТреугольника\n3\tВыход")
        choice = int(input("Выберите вариант\n"))
        if choice == 1:
            m = float(input("Введите радиус\n"))
            print(circle(m))
        elif choice == 2:
            k1 = float(input("Введите длины 1-ой стороны\n"))
            k2 = float(input("Введите длины 2-ой стороны\n"))
            k3 = float(input("Введите длины 3-ой стороны\n"))
            print(triangle(k1,k2,k3))
main()
