import math
class Phanso:
    def __init__(self,tu,mau):
        self.tu=tu
        self.mau=mau
        self.toigian()
    def toigian(self):
        ucln=math.gcd(self.tu,self.mau)
        self.tu //=ucln
        self.mau //=ucln
    def __str__(self):
        return f"{self.tu}/{self.mau}"
tu,mau=map(int,input().split())
a=Phanso(tu,mau)
print(a)
    