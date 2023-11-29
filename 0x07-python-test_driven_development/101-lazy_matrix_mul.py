#!/usr/bin/python
"""
This will print the product of two matrices to output
>>>lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]])
[[13, 16]]
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices

    Args: 
    	m_a (list): matrix a
        m_b (list): matrix b
    Returns:
    	the new matrix after operation
    """
    m_c = np.dot(m_a, m_b)
    return m_c
