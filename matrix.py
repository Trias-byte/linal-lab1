class Matrix:
    def __init__(self,
        matrix_:list = [],
        row:list = [],
        column:list = [], 
        value:list = [], 
        size:tuple = (0, 0)
    ):
        self.row = row
        self.column = column
        self.value = value
        self.size = size
        
        if matrix_ != []:
            self.row = []
            self.column = []
            self.value = []
            self.size = (len(matrix_), len(matrix_[0]))
            for i in range(len(matrix_)):
                self.row.append(0)
                for j in range(len(matrix_[i])):
                    if matrix_[i][j] != 0:
                        self.row[i] += 1
                        self.column.append(j)
                        self.value.append(matrix_[i][j])
        
    def __eq__(self, other):
        if not isinstace(other, (Matrix))
        return self.row == other.row and self.column == other.column and self.value == other.value
    def __len__(self):
        return self.size

    def __str__(self):
        res = f' [{*row}]\n [{*column}]\n [{*value}]'
        return res

    def get_row_value(self, n_row):
        a = sum(self.row[:n_row])
        ans = [
            [self.column[i+a] for i in self.row[n_row]],
            [self.value[i+a] for i in self.row[n_row]]

        ]
        return ans 

    def trace(self) -> int:
        trace = 0
        cnt = -1
        for i in range(len(self.row)):
            for j in range(len(self.row[i])):
                cnt += 1
                if self.column[cnt] == i:
                    trace += self.value[cnt]

        return trace

    def element(self, r: int, c: int):
        cnt = 0
        r -= 1
        c -= 1
        b = sum(self.row[:r])
        for i in range(row[r]):
            if self.column[b+i] == c:
                cnt = i
                return self.value[cnt]
        return 0


def sum_matrix(first: Matrix, second: Matrix) -> "Matrix":
    if len(first) != len(second):
        raise Exception("Разная размерность!")
    cnt_f, cnt_s = 0, 0
    row = []
    col = []
    val = []
    for i in range(len(first.row)):
        a = first.row[i] + first.column[i]
        while True:
            if first.column[cnt_f] > second.column[cnt_s] and cnt_s < second.row[i]:
                col.append(second.column[cnt_s])
                val.append(second.value[cnt_s])
                cnt_s+= 1
            elif first.column[cnt_f] < second.column[cnt_s] and cnt_f < first.row[i]:
                col.append(first.column[cnt_f])
                val.append(first.value[cnt_f])
                cnt_f += 1
            elif first.column[cnt_f] == second.column[cnt_s]:
                col.append(first.column[cnt_f])
                val.append(first.value[cnt_f] + second.value[cnt_s])
                cnt_f += 1
                cnt_s += 1
                a -= 1
            elif cnt_f < first.row[i]:
                if col[-1]!= first.column[cnt_f]:
                    col.append(first.column[cnt_f])
                    cnt_f += 1
                else:
                    cnt_f += 1
                    col.append(first.column[cnt_f])
                    val.append(first.value[cnt_f])
            elif cnt_s < second.row[i]:
                if col[-1]!= second.column[cnt_s]:
                    col.append(second.column[cnt_s])
                    val.append(second.column[cnt_s])
                    cnt_s += 1
                else:
                    cnt_s += 1
                    col.append(second.column[cnt_s])
                    val.append(second.value[cnt_s])
            else:
                break
        row.append(a)
    return Matrix(row = row, column = col, value = val, size = len(first))
    

def multi_matrix_const(matrix: Matrix, const: int = 1) -> "Matrix":
    val = []
    for i in matrix.value:
        val.append(i*const)
    return Matrix(row = matrix.row, column = matrix.column, value = val, size = len(matrix))


def matrix_traspose(mat: Matrix) -> "Matrix":
    colVector = [[] for _ in range(mat.size[1])]
    valVector = [[] for _ in range(mat.size[1])]
    row = []
    col = []
    val = []
    cnt = 0
    for i in range(len(mat.row)):
        for y in range(mat.row[i]):
            cnt += 1
            colVector[mat.column[cnt]].append(i)
            valVector[mat.column[cnt]].append(mat.value[cnt])
    for i in range(len(colVector)):
        row.append(len(colVector[i]))
        col += colVector[i]
        val += colVector[i]
    return Matrix(row = row, column = col, value = val, size = (mat.size[1], mat.size[0]))


def multi_matrix(first: Matrix, second: Matrix) -> "Matrix":
    if len(first) != len(second):
        raise Exception("Разная размерность!")

    sec = matrix_traspose(second)
    row = []
    col = []
    val = []
    
    for i in range(len(first.row)):
        c = []
        v = []
        for y in range(len(sec.row)):
        
            a = 0
            cnt_f = 0, cnt_s = 0
            while cnt_f < len(first.row[i]) and cnt_s < len(sec.row[i]):
                col_f = first.get_row_value(i)[0][cnt_f]
                col_s = sec.get_row_value(y)[0][cnt_s]
                if col_f > col_s:
                    cnt_s += 1
                elif col_f < col_s:
                    cnt_f += 1
                else:
                    a += sec.get_row_value(y)[1][cnt_s] * first.get_row_value(i)[1][cnt_s] 
            if (a != 0):
                c.append(y)
                v.append(a)
        col += c
        val += v
        row.append(len(c))
    return Matrix(row = row, value = val, column = col, size = (first.size[0], second.size[1]) )


def get_det(mat: Matrix) -> int:
    matrix = []
    cnt = -1
    tmp = 0
    d = 0

    for i in range(len(mat.row)):
        a = 0
        matrix.append([])
        for y in range(len(mat.row[i])):
            cnt += 1
            while a < mat.column[cnt]:
                matrix[i].append(0)
                a += 1
            matrix[i].append(mat.value[cnt])

    for k in range(n-1):
         for i in range(k+1, n):
            tmp = -matrix[i][k] / matrix[k][k]
            for j in range(n):
                matrix[i][j] += matrix[k][j] * tmp
    d = 1
    for i in range(n):
        d *= matrix[i][i]
    return  (d, d != 0) 
