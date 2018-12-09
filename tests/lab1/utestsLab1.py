import unittest
import coverage
from lab1.main.MySorter import MySorter


class TestSorer(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.cov = coverage.Coverage()
        self.cov.start()

    @classmethod
    def tearDownClass(self):
        self.cov.stop()
        self.cov.save()
        self.cov.html_report()

    def setUp(self):
        self.sorter = MySorter()


    def test_basic_sort(self):

        self.assertEqual(self.sorter.sort([[1, 2, 3],
                                          [4, 5, 6],
                                          [7, 8, 9]]), [[9, 8, 7],
                                                        [6, 1, 2],
                                                        [3, 4, 5]])

    def test_empty_matrix(self):

        self.assertEqual(self.sorter.sort([]), [])


    def test_already_sorted_matrix(self):

        self.assertEqual(self.sorter.sort([[9, 8, 7],
                                          [6, 1, 2],
                                          [3, 4, 5]]), [[9, 8, 7],
                                                        [6, 1, 2],
                                                        [3, 4, 5]])

    def test_square_matrix_input(self):

        self.assertEqual(self.sorter.sort([[1, 2]]), 'Incorrect input')

    def test_integer_elements_in_matrix(self):

        self.assertEqual(self.sorter.sort([[1.7, 2.3],
                                           [3.5, 5.8]]), 'Incorrect input')

    def test_same_elements_in_matrix(self):

        self.assertEqual(self.sorter.sort([[2, 2, 2],
                                           [2, 2, 2],
                                           [2, 2, 2]]), [[2, 2, 2],
                                                         [2, 2, 2],
                                                         [2, 2, 2]])





if __name__ == '__main__':

    unittest.main()