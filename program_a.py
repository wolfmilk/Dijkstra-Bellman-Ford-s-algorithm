from collections import defaultdict
from heapq import *
def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))
    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf")

if __name__ == "__main__":
    edges = [
        ("A", "B", 22),
        ("A", "C", 9),
        ("A", "D", 12),
        ("B", "C", 35),
        ("B", "F", 36),
        ("B", "H", 34),
        ("C", "F", 42),
        ("C", "E", 65),
        ("C", "D", 4),
        ("D", "E", 33),
        ("D", "I", 30),
        ("E", "F", 18),
        ("E", "G", 23),
        ("F", "H", 24),
        ("F", "G", 39),
        ("G", "H", 25),
        ("G", "I", 21),
        ("H", "I", 19)
    ]

    print ("the shortest path between nodes A and I for the giving graph is: ",dijkstra(edges, "A", "I"))
    import timeit
    print("The timeit for this program is: ",timeit.timeit("dijkstra", globals=globals(), number=5))
    
