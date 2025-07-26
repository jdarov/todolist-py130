class Triangle:

    def __init__(self, x, y, z):
        self.sides = sorted([x, y, z])
        if not self._validate_triangle():
            raise ValueError

    @property
    def kind(self):
        if (len(set(self.sides)) == 1):
            return "equilateral"
        if (len(set(self.sides)) == 2):
            return "isosceles"
        return "scalene"
    
    def _validate_triangle(self):
        return (
            all(side > 0 for side in self.sides)
            and self.sides[0] + self.sides[1] > self.sides[2]
        )
