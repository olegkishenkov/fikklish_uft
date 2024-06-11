from multiprocessing import Pool, Array
import logging
from datetime import datetime
logger = logging.getLogger(__name__)


def make_set(i):
    labels[i] = i
    ranks[i] = 0

def find_set(i):
    if labels[i] != i:
        labels[i] = find_set(labels[i])
    return labels[i]

def union(i, j):
    logger.info(f'union {i} {j} {find_set(i)} {find_set(j)}')
    if ranks[i] < ranks[j]:
        labels[find_set(i)] = find_set(j)
    elif ranks[i] > ranks[j]:
        labels[find_set(j)] = find_set(i)
    else:
        labels[find_set(max(i, j))] = find_set(min(i, j))
        logger.info(f'union  {list(labels)} {id(labels)}')
        ranks[min(i, j)] += 1

def process_internal(start, end):
    logger.info(f'process internal {start} {end}')
    for i in range(start, end):
        for j in edges[i]:
            if j < i and start <= j < end and find_set(i) != find_set(j):
                logger.info(f'process internal  {i} {j} {find_set(i)} {find_set(j)}')
                union(i, j)


def process_external():
    for i in range(n):
        for j in edges[i]:
            if j < i and i // part_size != j // part_size and find_set(i) != find_set(j):
                logger.info(f'process external {i} {j} {find_set(i)} {find_set(j)}')
                union(i, j)


# labels: list[int]
lables: Array
ranks: list[int]
processes_n: int = 4
n: int
part_size: int
edges: list[list[int]]


def connected_components(edges_: list[list[int]]):
    global edges, labels, ranks, n, part_size
    edges = edges_
    n = len(edges)
    # labels = [None] * n
    labels = Array('i', [-1] * n)
    ranks = [None] * n
    part_size = n // processes_n

    for i in range(n):
        make_set(i)

    with Pool(processes_n) as p:
        p.starmap(
            process_internal,
            [(part_size * i, part_size * (i + 1)) for i in range(processes_n-1)] + [(part_size * (processes_n - 1), n)],
        )

    logger.info(f'{list(labels)}, {id(labels)}')
    process_external()

    return list(labels)
