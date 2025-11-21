from solution import find_cheapest_price

def test_simple_path():
    assert find_cheapest_price(
        3,
        [
            [0, 1, 100],
            [1, 2, 100]
        ],
        0, 2, 1
    ) == 200

def test_direct_path_cheapest():
    assert find_cheapest_price(
        3,
        [
            [0, 1, 500],
            [0, 2, 100]
        ],
        0, 2, 0
    ) == 100

def test_exceeds_stops_returns_minus_one():
    assert find_cheapest_price(
        3,
        [
            [0, 1, 100],
            [1, 2, 100]
        ],
        0, 2, 0
    ) == -1
