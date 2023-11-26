#!/usr/bin/python
"""
This will print the product of two matrices to output
>>>lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]])
[[13, 16]]
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Returns the new matrix after operation
    Parameters: m_a and m_b, the matrices
    """
    m_c = np.dot(m_a, m_b)
    return m_c
