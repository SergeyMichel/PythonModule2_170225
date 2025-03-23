# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.
import math
def distance(x1, y1, x2, y2):
    # TODO: тело, которое вы реализовали на практической работе
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) # вычисляет расстояние между двумя точками


def min_lgth(xa, ya, xb, yb, xc, yc): # вычисляет длины всех трех отрезков 
    ab = distance(xa, ya, xb, yb)
    bc = distance(xb, yb, xc, yc)
    ac = distance(xa, ya, xc, yc)

    if ab <= bc and ab <= ac:
        return "AB" # возвращаем название самого короткого отрезка
    elif bc <= ab and bc <= ac: 
        return "BC" # возвращаем название самого короткого отрезка
    else:
        return "AC"  # возвращаем название самого короткого отрезка

xa, ya = 2, 6
xb, yb = 4, 3
xc, yc = 8, 4


# TODO: your code here
print("Самый короткий отрезок:", min_lgth(xa, ya, xb, yb, xc, yc)) # Выводим название отрезка, например “АС”.
