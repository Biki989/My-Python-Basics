class Vector:
    def __init__(self, components):
        self.components = components

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension for addition")
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension for dot product")
        return sum(a * b for a, b in zip(self.components, other.components))

    def __str__(self):
        return f"Vector({self.components})"


# Example usage:
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

sum_result = v1 + v2       # Vector addition
dot_result = v1 * v2       # Dot product

print("Sum:", sum_result)      # Vector([5, 7, 9])
print("Dot Product:", dot_result)  # 32
