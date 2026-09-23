class Matrix:
    def __init__(self, grid):
        self.grid = grid
        self.row = len(grid)
        self.col = len(grid[0]) if self.row > 0 else 0

    def show(self):
        for row in self.grid:
            print(" ".join(f"{val:>4}" for val in row))
        print()

    def add(self, other):
        if self.row != other.row or self.col != other.col:
            raise ValueError("Matrices must have the same dimensions to add.")
        
        result = [
            [self.grid[i][j] + other.grid[i][j] for j in range(self.col)]
            for i in range(self.row)
        ]
        return Matrix(result)

    def subtract(self, other):
        if self.row != other.row or self.col != other.col:
            raise ValueError("Matrices must have the same dimensions to subtract.")
        
        result = [
            [self.grid[i][j] - other.grid[i][j] for j in range(self.col)]
            for i in range(self.row)
        ]
        return Matrix(result)

    def multiplication(self, other):
        if self.col != other.row:
            raise ValueError(
                f"Cannot multiply: columns of first matrix ({self.col}) "
                f"must match rows of second matrix ({other.row})."
            )
        
        result = [
            [
                sum(self.grid[i][k] * other.grid[k][j] for k in range(self.col))
                for j in range(other.col)
            ]
            for i in range(self.row)
        ]
        return Matrix(result)


def main():
    m1 = Matrix([
        [1, 2, 3],
        [4, 5, 6]
    ])

    m2 = Matrix([
        [7, 8, 9],
        [1, 2, 3]
    ])

    m3 = Matrix([
        [1, 2],
        [3, 4],
        [5, 6]
    ])

    print("Matrix 1:")
    m1.show()

    print("Matrix 2:")
    m2.show()

    print("Addition (m1 + m2):")
    m1.add(m2).show()

    print("Subtraction (m1 - m2):")
    m1.subtract(m2).show()

    print("Multiplication (m1 x m3):")
    m1.multiplication(m3).show()


if __name__ == "__main__":
    main()