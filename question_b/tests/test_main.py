import pytest
from question_b.main import compare_versions


@pytest.mark.parametrize(
    "v1, v2, expected",
    [
        ("1.2", "1.1", 1),
        ("1.1", "1.2", -1),
        ("1.2.3", "1.2.3", 0),
        ("1.2", "1.2.3", -1),
        ("1.2.3", "1.2", 1),
    ]
)
def test_compare_versions(v1, v2, expected):
    assert compare_versions(v1, v2) == expected
