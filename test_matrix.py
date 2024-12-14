import unittest
from matrix import Matrix


class MatrixTestCase(unittest.TestCase):
    def setUp(self):
        data = [
            [1, 0, 0, 0], 
            [0, 1, 0, 0], 
            [0, 0, 1, 0], 
            [0, 0, 0, 1]
        ]
        self.ex = Matrix(data)


    def test_init_row(self):
        self.assertEqual(self.ex.row, [1, 1, 1, 1])


    def test_init_column(self):
        self.assertEqual(self.ex.column, [0, 1, 2, 3])


    def test_init_value(self):
        self.assertEqual(self.ex.value, [1, 1, 1, 1])

    def test_matrix_len(self):
        self.assertEqual(len(self.ex), (4, 4))

    def test_matrix_str(self):
        a = "[1, 1, 1, 1]\n [0, 1, 2, 3]\n [1, 1, 1, 1]"
        self.assertEqual(str(self.ex), a)

    def test_trace(self):
        self.assertEqual(self.ex.trace(), 4)

    def test_get_null_element(self):
        self.assertEqual(self.ex.test_get_element(1, 2), 0)
    
    def test_get_element(self):
        self.assertEqual(self.ex.test_get_element(1, 1))


class operationMatrixTestCase(unittest.TestCase):
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

        self.first = Matrix(data = data1)
        self.second = Matrix(data = data2)
        self.third = Matrix(data = data3)
        self.fouth = Matrix(data = data4)
        self.fith = Matrix(data = data5)
        self.six = Matrix(data = data6)
        self.seven = Matrix(data = data7)

    def test_normal_matrix(self):
        self.assertEqual(sum_matrix(self.first, self.second), self.third)

    def test_const(self):
        self.assertEqual(multi_matrix_const(self.first, 2), self.fith)

    def test_matrix_matrix(self):
        self.assertEqual(multi_matrix(self.first, self.fouth), self.six)
    
    def test_transpose_matrix(self):
        self.assertEqual(matrix_transpose(self.seven), self.trird)


class MatrixDetTestCase(unittest.TestCase) :
    def setUp(self):
        data = [
            [1, 2, 0],
            [0, 0, 3],
            [1, 1, 0]
        ]
        self.data = Matrix(data = data)
    
    def test_det(self):
        self.assertEqual(get_det(self.data), (3, True))


if __name__ == "__main__":
    unittest.main()
