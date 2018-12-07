'''
18. Дана квадратная целочисленная несортированная матрица.
Отсортировать в ней по убыванию только те элементы, которые являются большими,
чем среднее арифметическое всех элементов матрицы,
а оставшиеся элементы отсортировать по возрастанию.
'''
from __future__ import division
import operator
import numpy as np

class MySorter: # pragma: no cover

    # find mean in input matrix
    def calc_matrix_mean(self, matrix):
        matrix_sum = 0
        matrix_elements = 0

        for row in matrix:
            matrix_sum += sum(row)
            matrix_elements += len(row)

        mean = matrix_sum/matrix_elements

        return mean

    # find element under or above mean
    def find_subarray_of_elements(self, matrix, mean, relate):
        elements = []

        for row in matrix:
            for element in row:
                if relate(element, mean) is True:
                    elements.append(element)

        return elements

    # sort element by increasing or decreasing
    def bubble_sort(self, array, relate):

        for n in range(1, len(array)):
            for j in range(len(array)-n):
                if relate(array[j], array[j+1]) is True:
                    array[j], array[j+1] = array[j+1], array[j]

        return array

    # input array performs into square matrix
    def split_list(self, alist):
        length = len(alist)
        wanted_parts = int(np.sqrt(length))

        return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts]
                for i in range(wanted_parts)]

    # check if matrix suit's for sorting
    def check_matrix(self, matrix):
        number_of_elements = 0
        for row in matrix:
            for element in row:
                number_of_elements += 1
                if isinstance(element, int) is not True:
                    return False

        if float(np.sqrt(number_of_elements)) != float(len(matrix)):
            return False
        else:
            return True

    # main function with all steps of sorting array
    def sort(self, matrix):
        if len(matrix) == 0:
            return matrix
        elif self.check_matrix(matrix) is False:
            return 'Incorrect input'
        else:
            mean = self.calc_matrix_mean(matrix)

            great_elements = self.find_subarray_of_elements(matrix, mean, operator.gt)
            small_elements = self.find_subarray_of_elements(matrix, mean, operator.le)

            sorted_great_elements = self.bubble_sort(great_elements, operator.lt)
            sorted_small_elements = self.bubble_sort(small_elements, operator.gt)

            result_matrix = self.split_list(sorted_great_elements+sorted_small_elements)

            return result_matrix