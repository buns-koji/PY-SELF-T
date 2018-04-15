class Hexagon():
    def __init__(self,l1,l2,l3,l4,l5,l6):
        self.len1 = l1
        self.len2 = l2
        self.len3 = l3
        self.len4 = l4
        self.len5 = l5
        self.len6 = l6

    def perimeter(self):
        return self.len1 + self.len2 + self.len3 + self.len4 + self.len5 + self.len6

hexagon = Hexagon(3,3,3,3,3,3)
print(hexagon.perimeter())
