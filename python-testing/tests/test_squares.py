import pytest
from programs import list_of_squares

def test_fact():
	assert list_of_squares.list_of_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
	assert list_of_squares.list_of_squares(6) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}