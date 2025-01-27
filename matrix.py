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
            cnt = 0
            for i in range(len(matrix_)):
                self.row.append(cnt)
                for j in range(len(matrix_[i])):
                    if matrix_[i][j] != 0:
                        cnt += 1
                        self.column.append(j)
                        self.value.append(matrix_[i][j])
            self.row.append(cnt)
                
        
    def __eq__(self, other):
        if not isinstace(other, (Matrix)):
            return self.row == other.row and self.column == other.column and self.value == other.value
    
    def __len__(self):
        return self.size

    def __str__(self):
        res = f' [{self.row}]\n [{self.column}]\n [{self.value}]'
        return res

    def get_row_value(self, n_row):
        ans = [
            [self.column[self.row[n_row]:self.row[n_row + 1]]],
            [self.value[self.row[n_row]:self.row[n_row + 1]]]

        ]
        return ans 

    def trace(self) -> int:
        trace = 0
        cnt = -1
        for i in range(self.size[0]):
            for j in range(self.row[i], self.row[i+1]):
                if i == self.column[j]:
                    trace += self.value[j]
        return trace

    def element(self, r: int, c: int):
        a = sum([i for i in range(self.row[r], self.row[r+1]) if self.column[i] == c ])
        return 0 if c not in self.column[self.row[r]:self.row[r+1]] else self.value[a]

def multi_matrix_const(matrix: Matrix, const: int = 1) -> "Matrix":
    val = []
    for i in matrix.value:
        val.append(i*const)
    return Matrix(row = matrix.row, column = matrix.column, value = val, size = len(matrix))

def sum_matrix(first: Matrix, second: Matrix) -> "Matrix":
    if first.size != second.size:
        raise ValueError("Matrices have different dimensions!")

    row = [0]
    column = []
    value = []

    for i in range(first.size[0]):
        f_start, f_end = first.row[i], first.row[i + 1]
        s_start, s_end = second.row[i], second.row[i + 1]

        f_ptr, s_ptr = f_start, s_start

        while f_ptr < f_end or s_ptr < s_end:
            if s_ptr >= s_end or (f_ptr < f_end and first.column[f_ptr] < second.column[s_ptr]):
                column.append(first.column[f_ptr])
                value.append(first.value[f_ptr])
                f_ptr += 1
            elif f_ptr >= f_end or (s_ptr < s_end and second.column[s_ptr] < first.column[f_ptr]):
                column.append(second.column[s_ptr])
                value.append(second.value[s_ptr])
                s_ptr += 1
            else:  # Equal columns
                sum_value = first.value[f_ptr] + second.value[s_ptr]
                if sum_value != 0:
                    column.append(first.column[f_ptr])
                    value.append(sum_value)
                f_ptr += 1
                s_ptr += 1

        row.append(len(column))

    return Matrix(row=row, column=column, value=value, size=first.size)


def transpose_matrix(mat: Matrix) -> "Matrix":
    row_count, col_count = mat.size
    t_row = [0] * (col_count + 1)
    t_col = [0] * len(mat.column)
    t_val = [0] * len(mat.value)

    for c in mat.column:
        t_row[c + 1] += 1

    for i in range(1, len(t_row)):
        t_row[i] += t_row[i - 1]

    temp = t_row[:-1]

    for r in range(row_count):
        for i in range(mat.row[r], mat.row[r + 1]):
            c = mat.column[i]
            pos = temp[c]
            t_col[pos] = r
            t_val[pos] = mat.value[i]
            temp[c] += 1

    return Matrix(row=t_row, column=t_col, value=t_val, size=(col_count, row_count))

    
def multiply_matrices(a: Matrix, b: Matrix) -> "Matrix":
    if a.size[1] != b.size[0]:
        raise ValueError("Matrix dimensions do not allow multiplication!")

    b_t = transpose_matrix(b)

    row = [0]
    column = []
    value = []

    for i in range(a.size[0]):
        row_start, row_end = a.row[i], a.row[i + 1]
        col_idx = []
        col_val = []

        for j in range(row_start, row_end):
            col_a = a.column[j]
            val_a = a.value[j]

            col_start, col_end = b_t.row[col_a], b_t.row[col_a + 1]

            for k in range(col_start, col_end):
                col_b = b_t.column[k]
                val_b = b_t.value[k]

                if col_b not in col_idx:
                    col_idx.append(col_b)
                    col_val.append(val_a * val_b)
                else:
                    idx = col_idx.index(col_b)
                    col_val[idx] += val_a * val_b

        sorted_indices = sorted(range(len(col_idx)), key=lambda x: col_idx[x])
        for idx in sorted_indices:
            column.append(col_idx[idx])
            value.append(col_val[idx])

        row.append(len(column))

    return Matrix(row=row, column=column, value=value, size=(a.size[0], b.size[1]))




def get_det(mat: Matrix) -> int:
    if mat.size[0] != mat.size[1]:
        raise ValueError("Matrix is not square!")

    n = mat.size[0]
    det = 1
    temp_row = mat.row[:]
    temp_col = mat.column[:]
    temp_val = mat.value[:]

    for i in range(n):
        pivot = -1
        for j in range(temp_row[i], temp_row[i + 1]):
            if temp_col[j] == i:
                pivot = j
                break

        if pivot == -1 or temp_val[pivot] == 0:
            return 0

        det *= temp_val[pivot]
        temp_val[pivot] = 1

        for j in range(temp_row[i], temp_row[i + 1]):
            temp_val[j] /= det

        for k in range(i + 1, n):
            factor = 0
            for j in range(temp_row[k], temp_row[k + 1]):
                if temp_col[j] == i:
                    factor = temp_val[j]
                    temp_val[j] = 0
                    break

            if factor != 0:
                for j in range(temp_row[i], temp_row[i + 1]):
                    for l in range(temp_row[k], temp_row[k + 1]):
                        if temp_col[l] == temp_col[j]:
                            temp_val[l] -= factor * temp_val[j]

    return int(det)
