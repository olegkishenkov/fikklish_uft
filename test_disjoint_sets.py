import logging
from disjoint_sets import connected_components

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='disjoint_sets.log',
    level=logging.INFO,
    force=True,
    format='%(asctime)s - %(module)s - %(levelname)s - %(message)s',
    filemode='w'
)


def test_two_connected_vertices():
    assert connected_components([[1], [0]]) == [0, 0]

def test_two_and_one_vertices():
    assert connected_components([[1], [0], []]) == [0, 0, 2]

def test_triangle():
    assert connected_components([[1, 2], [0, 2], [0, 1]]) == [0, 0, 0]

def test_triangle_unsorted():
    assert connected_components([[1, 2], [2, 0], [0, 1]]) == [0, 0, 0]

def test_four_triangles():
    assert connected_components(
        [[1, 2], [0, 2], [0, 1], [4, 5], [3, 5], [3, 5], [7, 8], [6, 8], [6, 7]]
    ) == [0, 0, 0, 3, 3, 3, 6, 6, 6]