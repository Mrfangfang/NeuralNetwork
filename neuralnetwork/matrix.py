'''
David Fuller

Matrix class: Template for a Matrix object.

2018-4-13
'''

import random


class Matrix:
    def __init__(self, row_count, column_count):
        '''
        Matrix's init method.

        Sets up a Matrix object.

        Args:
            row_count (int): Number of rows in a matrix.
            column_count (int): Number of columns in a matrix.
        '''
        
        self.row_count = row_count
        self.column_count = column_count
        self.data = []

        for i in range(self.row_count):
            self.data.append([])
            for j in range(self.column_count):
                self.data[i].append(j * 0)

    def randomize(self):
        '''
        Randomize the elements of the matrix between -1 and 1.
        '''
        
        for i in range(self.row_count):
            for j in range(self.column_count):
                self.data[i][j] = random.random() * 2 - 1

    @staticmethod
    def map(matrix, function):
        '''
        Static method maps a given method to all elements of a matrix.

        Args:
            matrix (Matrix): Matrix to map method to.
            function (method): Method to be mapped.

        Returns:
            Matrix: Resulting matrix after mapping the method.
        '''
        
        result = Matrix(matrix.row_count, matrix.column_count)
        for i in range(matrix.row_count):
            for j in range(matrix.column_count):
                value = matrix.data[i][j]
                result.data[i][j] = function(value)
        return result

    def copy(self):
        '''
        Makes a copy of itself.

        Returns:
            Matrix: A copy of a Matrix.
        '''
        
        matrix = Matrix(self.row_count, self.column_count)
        for i in range(self.row_count):
            for j in range(self.column_count):
                matrix.data[i][j] = self.data[i][j]
        return matrix

    @staticmethod
    def from_array(input_array):
        '''
        Static method creates a matrix from an array.

        Args:
            input_array (array): array of integers.

        Returns:
            Matrix: Matrix created from the integers.
        '''

        length = len(input_array)
        new_matrix = Matrix(length, 1)
        for i in range(length):
            new_matrix.data[i][0] = input_array[i]
        return new_matrix

    def to_array(self):
        '''
        Creates an array from a matrix.

        Returns:
            array: 1 dimensional array created from a matrix.
        '''
        
        array = []
        for i in range(self.row_count):
            for j in range(self.column_count):
                array.append(self.data[i][j])
        return array

    @staticmethod
    def transpose(matrix):
        '''
        Static method transposes a given matrix.

        Args:
            matrix (Matrix): Matrix to transpose.

        Returns:
            Matrix: Transposed matrix.
        '''
        
        result = Matrix(matrix.column_count, matrix.row_count)
        for i in range(matrix.row_count):
            for j in range(matrix.column_count):
                result.data[j][i] = matrix.data[i][j]
        return result

    def add(self, n):
        '''
        Adds n to itself.

        Args:
           n (Matrix): Addend as a matrix or
           n (int): Addend as an integer.
        '''
        
        if isinstance(n, Matrix):
            if self.row_count != n.row_count or \
                    self.column_count != n.column_count:
                print('Cannot add. Different matrix sizes.')
            else:
                for i in range(self.row_count):
                    for j in range(self.column_count):
                        self.data[i][j] = self.data[i][j] + n.data[i][j]
        else:
            for i in range(self.row_count):
                for j in range(self.column_count):
                    self.data[i][j] = self.data[i][j] + n

    @staticmethod
    def subtract(a, b):
        '''
        Static method subtracts matrix b from matrix a.

        Args:
            a (Matrix): Minuend matrix.
            b (Matrix): Subtrahend matrix.

        Returns:
            Matrix: Resulting matrix from subtraction.
        '''
        
        if a.row_count != b.row_count or a.column_count != b.column_count:
            print('Cannot subtract. Different matrix sizes.')
        else:
            result = Matrix(a.row_count, a.column_count)
            for i in range(a.row_count):
                for j in range(a.column_count):
                    result.data[i][j] = a.data[i][j] - b.data[i][j]
            return result                    

    def multiply(self, n):
        '''
        Multiplies itself by n.

        Args:
            n (Matrix): Multiplier as a Matrix or
            n (int): Multiplier as an integer.
        '''
        
        if isinstance(n, Matrix):
            if self.row_count != n.row_count or \
                    self.column_count != n.column_count:
                print('Cannot multiply. Different matrix sizes.')
            else:
                for i in range(self.row_count):
                    for j in range(self.column_count):
                        self.data[i][j] = self.data[i][j] * n.data[i][j]
        else:
            for i in range(self.row_count):
                for j in range(self.column_count):
                    self.data[i][j] = self.data[i][j] * n

    @staticmethod
    def static_multiply(a, b):
        '''
        Static method multiplies matrix a and matrix b.

        Args:
           a (Matrix): Multiplicand matrix.
           b (Matrix): Multiplier matrix.

        Returns:
           Matrix: Resulting matrix of the multiplication.
        '''
        
        if a.column_count != b.row_count:
            print('Cannot multiply. Column count of' +
                  ' a must match row count of b.')
            return None

        result = Matrix(a.row_count, b.column_count)
        for i in range(result.row_count):
            for j in range(result.column_count):
                summation = 0
                for k in range(a.column_count):
                    summation = summation + a.data[i][k] * b.data[k][j]
                result.data[i][j] = summation
        return result

    def __str__(self):
        '''
        String representation of Matrix object.

        Returns:
           str: Matrix as a string.
        '''

        output = ''
        for i in range(self.row_count):
            for j in range(self.column_count):
                output += '{:<5}'.format(str(self.data[i][j])) + ' '
            output = output.rstrip(' ')
            output += '\n'
        return output.rstrip('\n')
