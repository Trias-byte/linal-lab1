import unittest
from matrix import Matrix, sum_matrix, multi_matrix_const, transpose_matrix, multiply_matrices, get_det


class MatrixTestCase(unittest.TestCase):
    def setUp(self):
        data = [
            [1, 0, 0, 0], 
            [0, 1, 0, 0], 
            [0, 0, 1, 0], 
            [0, 0, 0, 1]
        ]
        self.ex = Matrix(matrix_=data)

    def test_init_row(self):
        self.assertEqual(self.ex.row, [0, 1, 2, 3, 4])

    def test_init_column(self):
        self.assertEqual(self.ex.column, [0, 1, 2, 3])

    def test_init_value(self):
        self.assertEqual(self.ex.value, [1, 1, 1, 1])

    def test_matrix_len(self):
        self.assertEqual(self.ex.size, (4, 4))

    def test_matrix_str(self):
        expected = " [0, 1, 2, 3, 4]\n [0, 1, 2, 3]\n [1, 1, 1, 1]"
        self.assertEqual(str(self.ex), expected)

    def test_trace(self):
        self.assertEqual(self.ex.trace(), 4)

    def test_get_null_element(self):
        self.assertEqual(self.ex.element(1, 2), 0)

    def test_get_element(self):
        self.assertEqual(self.ex.element(1, 1), 1)


class OperationMatrixTestCase(unittest.TestCase):
    def setUp(self):
        data1 = [
            [1, 0], 
            [0, 0],
            [1, 1],
        ]

        data2 = [
            [0, 1], 
            [1, 1], 
            [0, 0]
        ]

        data3 = [
            [1, 1],
            [1, 1],
            [1, 1]
        ]

        data4 = [
            [1, 0, 1], 
            [0, 2, 1]
        ]

        data5 = [
            [2, 0], 
            [0, 0], 
            [2, 2]
        ]

        data6 = [
            [1, 0, 1], 
            [0, 0, 0], 
            [1, 2, 2]
        ]

        data7 = [
            [1, 1, 1], 
            [1, 1, 1]
        ]

        self.first = Matrix(matrix_=data1)
        self.second = Matrix(matrix_=data2)
        self.third = Matrix(matrix_=data3)
        self.fourth = Matrix(matrix_=data4)
        self.fifth = Matrix(matrix_=data5)
        self.sixth = Matrix(matrix_=data6)
        self.seventh = Matrix(matrix_=data7)

    def test_sum_matrix(self):
        result = sum_matrix(self.first, self.second)
        self.assertEqual(result.row, self.third.row)
        self.assertEqual(result.column, self.third.column)
        self.assertEqual(result.value, self.third.value)

    def test_const(self):
        self.assertEqual(multi_matrix_const(self.first, 2), self.fith)

    def test_multiply_matrices(self):
        result = multiply_matrices(self.first, self.fourth)
        self.assertEqual(result.row, self.sixth.row)
        self.assertEqual(result.column, self.sixth.column)
        self.assertEqual(result.value, self.sixth.value)

    def test_transpose_matrix(self):
        result = transpose_matrix(self.seventh)
        self.assertEqual(result.row, [0, 2, 4, 6])
        self.assertEqual(result.column, [0, 1, 0, 1, 0, 1])
        self.assertEqual(result.value, [1, 1, 1, 1, 1, 1])


class MatrixDetTestCase(unittest.TestCase):
    def setUp(self):
        data = [
            [1, 2, 0],
            [0, 0, 3],
            [1, 1, 0]
        ]
        self.matrix = Matrix(matrix_=data)

    def test_det(self):
        self.assertEqual(get_det(self.matrix), 3)


if __name__ == "__main__":
    unittest.main()
