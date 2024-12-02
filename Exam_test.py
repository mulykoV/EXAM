import unittest
from Exam import nth_term_arithmetic_progression

def nth_term_arithmetic_progression(a, d, n): 
    return a + (n - 1) * d

class TestArithmeticProgression(unittest.TestCase): 
    def test_first_term(self): 
        self.assertEqual(nth_term_arithmetic_progression(5, 2, 1), 5)

    def test_second_term(self): 
        self.assertEqual(nth_term_arithmetic_progression(5, 2, 2), 7)

    def test_fifth_term(self): 
        self.assertEqual(nth_term_arithmetic_progression(5, 2, 5), 13)

    def test_tenth_term(self): 
        self.assertEqual(nth_term_arithmetic_progression(5, 2, 10), 23)

if __name__ == '__main__': 
    unittest.main()