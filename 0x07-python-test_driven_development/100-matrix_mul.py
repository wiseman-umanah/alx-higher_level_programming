#!/usr/bin/python3

"""
Function to calculate the product of 2 matrices(no module)
>>>matrix_mul([[1, 2]], [[3, 4], [5, 6]])
[[13, 16]]
"""


def matrix_mul(m_a, m_b):
    """
    Returns the new matrix after operation
    Parameters: m_a and m_b, the matrices
    ErrorHandle: TypeError, ValueError
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if [] == m_a:
        raise ValueError("m_a can't be empty")
    if [] == m_b:
        raise ValueError("m_b can't be empty")
    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
        if len(i) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for i in m_b:
        if not isinstance(i, list):
            raise TypeError("m_b must be a list of lists")
        if len(i) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    e1 = "should contain only integers or floats"
    new_matrix = []
    m1 = 0
    m2 = 0
    for i in range(len(m_a)):
        temp = []
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_b)):
                m1 = m_a[i][k]
                m2 = m_b[k][j]
                if not isinstance(m1, int) and not isinstance(m1, float):
                    raise TypeError(f"m_a {e1}")
                if not isinstance(m2, int) and not isinstance(m2, float):
                    raise TypeError(f"m_b {e1}")
                sum = sum + m1 * m2
            temp.append(sum)
        new_matrix.append(temp)
    return new_matrix
