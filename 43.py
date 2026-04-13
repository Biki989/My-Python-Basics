class Vector:
    def __init__(self, components):
        self.components = components  # list or tuple of numbers

    # Task 5: Overload + operator (vector addition)
    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for addition.")
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    # Task 5: Overload * operator (dot product)
    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for dot product.")
        return sum(a * b for a, b in zip(self.components, other.components))

    # Task 6: String representation (3D vector format like "7i + 8j + 10k")
    def __str__(self):
        if len(self.components) == 3:
            return f"{self.components[0]}i + {self.components[1]}j + {self.components[2]}k"
        return str(self.components)  # fallback for non-3D

    # Task 7: Override len() to return dimension of vector
    def __len__(self):
        return len(self.components)


# Example usage
v1 = Vector([7, 8, 10])
v2 = Vector([1, 2, 3])

# Addition
v3 = v1 + v2
print("Addition:", v3)  # 8i + 10j + 13k

# Dot product
print("Dot Product:", v1 * v2)  # (7*1 + 8*2 + 10*3) = 53

# Dimension
print("Dimension of v1:", len(v1))