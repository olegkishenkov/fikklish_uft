from disjoint_sets import connected_components


def test_two_connected_vertices():
    assert connected_components([[1], [0]]) == [0, 0]


def test_two_and_one_vertices():
    connected_components([[1], [0], []]) == [0, 0, 2]

def test_triangle():
    connected_components([[1, 2], [0, 2], [0, 1]]) == [0, 0, 0]

def test_triangle_unsorted():
    connected_components([[1, 2], [2, 0], [0, 1]]) == [0, 0, 0]