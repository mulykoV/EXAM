import pytest
from Exam import nth_term_arithmetic_progression

def test_nth_term_arithmetic_progression():
    assert nth_term_arithmetic_progression(5, 2, 1) == 5
    assert nth_term_arithmetic_progression(5, 2, 2) == 7
    assert nth_term_arithmetic_progression(5, 2, 3) == 9
