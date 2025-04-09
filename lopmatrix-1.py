class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.data = [[0 for _ in range(m)] for _ in range(n)]
    
    def input_matrix(self):
        for i in range(self.n):
            self.data[i] = list(map(int, input().split()))
    
    def transpose(self):
        transposed = Matrix(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                transposed.data[i][j] = self.data[j][i]
        return transposed
    
    def multiply(self, other):
        if self.m != other.n:
            raise ValueError("Cannot multiply matrices: dimensions do not match")
        result = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                result.data[i][j] = 0
                for k in range(self.m):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result
    
    def print_matrix(self):
        for i in range(self.n):
            print(" ".join(map(str, self.data[i])))

def main():
    num_tests = int(input())
    for _ in range(num_tests):
        n, m = map(int, input().split())
        matrix_a = Matrix(n, m)
        matrix_a.input_matrix()
        matrix_a_transpose = matrix_a.transpose()
        result_matrix = matrix_a.multiply(matrix_a_transpose)
        result_matrix.print_matrix()

if __name__ == "__main__":
    main()