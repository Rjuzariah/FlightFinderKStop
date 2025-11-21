from utils import find_cheapest_price

def test_simple_path():
    sample_data = {
        "n":3,
        "flights":[
            [0, 1, 100],
            [1, 2, 100]
        ],
        "src":0, 
        "dst":2, 
        "k":1
    }
    assert find_cheapest_price(**sample_data) == 200

def test_direct_path_cheapest():
    sample_data = {
        "n":3,
        "flights":[
            [0, 1, 500],
            [0, 2, 100]
        ],
        "src":0, 
        "dst":2, 
        "k":0
    }
    assert find_cheapest_price(**sample_data) == 100    

def test_no_possible_path():
    sample_data = {
        "n":4,
        "flights":[
            [0, 1, 100],
            [1, 2, 100]
        ],
        "src":0, 
        "dst":3, 
        "k":2
    }
    assert find_cheapest_price(**sample_data) == -1

def test_within_stops_but_more_expensive():
    sample_data = {
        "n":4,
        "flights":[
            [0, 1, 100],
            [1, 2, 100],
            [0, 2, 500]
        ],
        "src":0, 
        "dst":2, 
        "k":1
    }
    assert find_cheapest_price(**sample_data) == 200

def test_zero_stops_no_direct_flight():
    sample_data = {
        "n":3,
        "flights":[
            [0, 1, 100],
            [1, 2, 100]
        ],
        "src":0, 
        "dst":2, 
        "k":0
    }
    assert find_cheapest_price(**sample_data) == -1

def test_multiple_paths():
    sample_data = {
        "n":5,
        "flights":[
            [0, 1, 100],
            [1, 2, 100],
            [0, 2, 300],
            [2, 3, 100],
            [1, 3, 600],
            [3, 4, 100]
        ],
        "src":0, 
        "dst":4, 
        "k":3
    }
    assert find_cheapest_price(**sample_data) == 400

def test_no_flights():
    sample_data = {
        "n":3,
        "flights":[],
        "src":0, 
        "dst":2, 
        "k":1
    }
    assert find_cheapest_price(**sample_data) == -1

def test_3_stops_but_cheapest():
    sample_data = {
        "n": 7,
        "flights": [
            [0,1,300],
            [0,2,200],
            [1,3,100],
            [1,4,400],
            [2,1,200],
            [2,3,300],
            [2,5,500],
            [2,6,600],
            [3,4,100],
            [3,6,200],
            [4,6,100],
            [5,6,200]
        ],
        "src": 0,
        "dst": 6,
        "k": 3
    }
    assert find_cheapest_price(**sample_data) == 600
