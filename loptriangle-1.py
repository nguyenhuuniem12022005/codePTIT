from decimal import Decimal
from math import sqrt

class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def distance(self, other):
        dis = sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))
        return dis

class Triangle:
    def __init__(self, p1, p2, p3) :
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def is_valid(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)
  
        return (a + b > c) and (a + c > b) and (b + c > a)

    def perimeter(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)
        return a + b + c

if __name__ == '__main__':
    import sys


    data = sys.stdin.read().split()
    t = int(data[0]) 
    coords = list(map(Decimal, data[1:])) 

    idx = 0  

    for _ in range(t):
   
        p1 = Point(coords[idx], coords[idx + 1])
        p2 = Point(coords[idx + 2], coords[idx + 3])
        p3 = Point(coords[idx + 4], coords[idx + 5])
        idx += 6 

        triangle = Triangle(p1, p2, p3)

        if triangle.is_valid():
            peri = triangle.perimeter()
            print(f'{peri:.3f}')
        else:
            print('INVALID')
