import pytest

from scrabble import derive_score

test_data = [
    ('cabbage', 14),
    ('xylophone', 24),
    ('kazoo', 18),
    ]

@pytest.mark.parametrize("word, expected_score", test_data)
def test_scrabble_scoring(word, expected_score):
    result = derive_score(word)
    assert result == expected_score