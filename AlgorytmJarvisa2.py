import math
import AlgorytmJarvisa

def orientation(p1, p2, p3):
    x1, y1, x2, y2, x3, y3 = p1.x, p1.y, p2.x, p2.y, p3.x, p3.y
    d = (y3 - y2) * (x2 - x1) - (y2 - y1) * (x3 - x2)
    if d > 0:
        return 1
    elif d < 0:
        return -1
    else:
        return 0


def dist(p1, p2):
    x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y
    return math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)


def gift_wrapping(points):
    alg = AlgorytmJarvisa.AlgorytmJarvisa()
    min , max =alg.max_min(points)
    on_hull = min
    hull = []
    while True:
        hull.append(on_hull)
        next_point = points[0]
        for point in points:
            o = orientation(on_hull, next_point, point)
            if next_point == on_hull or o == 1 or (o == 0 and dist(on_hull, point) > dist(on_hull, next_point)):
                next_point = point
        on_hull = next_point
        if on_hull == hull[0]:
            break
    return hull