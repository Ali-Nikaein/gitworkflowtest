import unittest
from avgGrade import calculate_average_grade

class TestCalculateAverageGrade(unittest.TestCase):

    def test_average_grade_A(self):
        scores = [95, 92, 88, 98, 100]
        self.assertEqual(calculate_average_grade(scores), "A")

    def test_average_grade_B(self):
        scores = [85, 88, 92, 82, 87]
        self.assertEqual(calculate_average_grade(scores), "B")

    def test_average_grade_C(self):
        scores = [72, 78, 68, 75, 80]
        self.assertEqual(calculate_average_grade(scores), "C")

    def test_average_grade_D(self):
        scores = [62, 55, 67, 58, 60]
        self.assertEqual(calculate_average_grade(scores), "D")

    def test_average_grade_F(self):
        scores = [40, 30, 20, 10, 5]
        self.assertEqual(calculate_average_grade(scores), "F")

if __name__ == "__main__":
    unittest.main()
