from fractions import Fraction
from math import gcd
import copy


def simplify(x, y):
    g = gcd(x, y)
    return Fraction(int(x / g), int(y / g))


def lcm(x, y):
    return int(x * y / gcd(x, y))


def transform(st_mat):
    sum_list = list(map(sum, st_mat))
    bool_index = list(map(lambda x: x == 0, sum_list))
    mat_index = set([i for i, x in enumerate(bool_index) if x])
    tem_mat = []
    for i in range(len(st_mat)):
        tem_mat.append(list(map(lambda x: Fraction(0, 1) if (sum_list[i] == 0) else simplify(x, sum_list[i]),
                                st_mat[i])))
    transform_mat = []
    zeros_mat = []
    for i in range(len(tem_mat)):
        if i not in mat_index:
            transform_mat.append(tem_mat[i])
        else:
            zeros_mat.append(tem_mat[i])
    transform_mat.extend(zeros_mat)
    t_mat = []
    for i in range(len(transform_mat)):
        t_mat.append([])
        extend_mat = []
        for j in range(len(transform_mat)):
            if j not in mat_index:
                t_mat[i].append(transform_mat[i][j])
            else:
                extend_mat.append(transform_mat[i][j])
        t_mat[i].extend(extend_mat)
    return [t_mat, len(zeros_mat)]


def mat_copy(matrix):
    copied = copy.deepcopy(matrix)
    copied = [[Fraction(y, 1) for y in x] for x in copied]
    return copied


def gauss_elim(m, values):
    matrix = mat_copy(m)
    for i in range(len(matrix)):
        index = -1
        for j in range(i, len(matrix)):
            if matrix[j][i].numerator != 0:
                index = j
                break
        matrix[i], matrix[index] = matrix[index], matrix[j]
        values[i], values[index] = values[index], values[i]
        for j in range(i + 1, len(matrix)):
            if matrix[j][i].numerator == 0:
                continue
            ratio = -matrix[j][i] / matrix[i][i]
            for k in range(i, len(matrix)):
                matrix[j][k] += ratio * matrix[i][k]
            values[j] += ratio * values[i]
    solved = [0 for i in range(len(matrix))]
    for i in range(len(matrix)):
        index = len(matrix) - 1 - i
        end = len(matrix) - 1
        while end > index:
            values[index] -= matrix[index][end] * solved[end]
            end -= 1
        solved[index] = values[index] / matrix[index][index]
    return solved


def transpose(matrix):
    # python 3 only
    return [*zip(*matrix)]


def inverse(matrix):
    inversed = []
    transposed = transpose(matrix)
    for i in range(len(transposed)):
        values = [Fraction(int(i == j), 1) for j in range(len(matrix))]
        inversed.append(gauss_elim(transposed, values))
    return inversed


def mat_multiply(mat1, mat2):
    return [[sum(Fraction((x * y), 1) for x, y in zip(m1_r, m2_c)) for m2_c in zip(*mat2)] for m1_r in mat1]


def split_q_r(st_mat, size_r):
    size_q = len(st_mat) - size_r
    q_mat = []
    r_mat = []
    for i in range(size_q):
        q_mat.append([int(i == j) - st_mat[i][j] for j in range(size_q)])
        r_mat.append(st_mat[i][size_q:])
    return [q_mat, r_mat]


def solution(init):
    probabilities = transform(init)
    if probabilities[1] == len(init):
        return [1, 1]
    q_mat, r_mat = split_q_r(*probabilities)
    q_inverse = inverse(q_mat)
    probabilities = mat_multiply(q_inverse, r_mat)
    row = probabilities[0]
    m_factor = 1
    for fract in row:
        m_factor = lcm(m_factor, fract.denominator)
    probabilities = list(map(lambda x: int(x.numerator * m_factor / x.denominator), row))
    probabilities.append(m_factor)
    return probabilities
