import pytest

from scrabble import *

test_data = [('cabbage', 14)]

@pytest.mark.parametrize("word, expected_score", test_data)
def test_scrabble_scoring(word, expected_score):
    result = derive_score(word)
    assert result == expected_score