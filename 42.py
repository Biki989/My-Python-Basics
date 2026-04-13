class Vector:
    def __init__(self, components):
        if len(components) != 3:
            raise ValueError("Vector must be of dimension 3")
        self.components = components

    def __add__(self, other):
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, other):
        return sum(a * b for a, b in zip(self.components, other.components))

    def __str__(self):
        x, y, z = self.components
        return f"{x}i + {y}j + {z}k"


# Example usage:
v1 = Vector([7, 8, 10])
v2 = Vector([1, 2, 3])

sum_result = v1 + v2
dot_result = v1 * v2

print("Sum:", sum_result)        # 8i + 10j + 13k
print("Dot Product:", dot_result)  # 68