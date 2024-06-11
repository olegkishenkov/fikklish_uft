from multiprocessing import Pool

def make_set(i):
    global labels, ranks
    labels[i] = i
    ranks[i] = 0

def find_set(i):
    if labels[i] != i:
        labels[i] = find_set(labels[i])
    return labels[i]

def union(i, j):
    if ranks[i] < ranks[j]:
        labels[find_set(i)] = find_set(j)
    elif ranks[i] > ranks[j]:
        labels[find_set(j)] = find_set(i)
    else:
        labels[find_set(max(i, j))] = find_set(min(i, j))
        ranks[min(i, j)] += 1

def process_internal(start, end):
    for i in range(start, end):
        for j in range(len(edges[i])):
            if j < i and start <= j < end and find_set(i) != find_set(j):
                union(i, j)

def process_external():
    global edges
    for i in range(n):
        for j in range(len(edges[i])):
            if j < i and i // part_size != j // part_size and find_set(i) != find_set(j):
                union(i, j)


labels: list[int]
ranks: list[int]
processes_n: int = 4
n: int
part_size: int
edges: list[list[int]]



def connected_components(edges_: list[list[int]]):
    global labels, ranks, processes_n, n, part_size, edges
    edges = edges_
    n = len(edges)
    labels = [None] * n
    ranks = [None] * n
    part_size = n // processes_n + 1

    for i in range(n):
        make_set(i)

    with Pool(processes_n) as p:
        p.starmap(
            process_internal,
            ((part_size * i, min(part_size * (i + 1), n)) for i in range(processes_n)),
        )

    process_external()

    return labels
