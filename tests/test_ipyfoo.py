from ipyfoo import Counter


def test_counter():
    counter = Counter()
    counter.value = 10
    assert counter._esm
    assert counter.value == 10
