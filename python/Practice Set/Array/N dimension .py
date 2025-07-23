class Vector:
    def __init__(self, components):
        self.components = components

    def __add__(self, other):
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, other):
        dot_product = sum(a * b for a, b in zip(self.components, other.components))
        return dot_product
