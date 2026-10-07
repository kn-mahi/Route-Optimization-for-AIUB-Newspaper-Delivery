import math
import random
import time
import heapq

graph = {
    'Main Gate': {'Sports Gallery': 10, 'Annex 1': 21},
    'Sports Gallery': {'Main Gate': 10, 'D Building': 26, 'Annex 8': 25},
    'D Building': {'Sports Gallery': 26, 'Annex 8': 3, 'C Building': 13},
    'Annex 8': {'Sports Gallery': 25, 'D Building': 3, 'Annex 9': 10, 'C Building': 16},
    'Annex 9': {'Annex 8': 10, 'C Building': 15},
    'C Building': {'D Building': 13, 'Annex 8': 16, 'Annex 9': 15, 'Annex 2, 3 & 4': 12, 'Annex 5 & 6': 8},
    'Annex 1': {'Main Gate': 21, 'Annex 2, 3 & 4': 8},
    'Annex 2, 3 & 4': {'Annex 1': 8, 'Annex 5 & 6': 10, 'C Building': 12},
    'Annex 5 & 6': {'Annex 2, 3 & 4': 10, 'C Building': 8},
}

START = 'Main Gate'
TARGETS = [n for n in graph if n != START]
random.seed(42)

# Dijkstra (internal use only for cost calculation)
def dijkstra(source):
    dist = {node: math.inf for node in graph}
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in graph[u].items():
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

dist_map = {node: dijkstra(node) for node in graph}

def order_cost(order):
    total, cur = 0, START
    for nxt in order:
        total += dist_map[cur][nxt]
        cur = nxt
    return total

def random_order():
    arr = TARGETS[:]
    random.shuffle(arr)
    return arr

def hill_climbing(max_restarts=40):
    t0 = time.perf_counter()
    best, best_cost = None, math.inf
    for _ in range(max_restarts):
        current = random_order()
        current_cost = order_cost(current)
        improved = True
        while improved:
            improved = False
            for i in range(len(current)):
                for j in range(i + 1, len(current)):
                    nbr = current[:]
                    nbr[i], nbr[j] = nbr[j], nbr[i]
                    c = order_cost(nbr)
                    if c < current_cost:
                        current, current_cost = nbr, c
                        improved = True
        if current_cost < best_cost:
            best, best_cost = current[:], current_cost
    return best, best_cost, (time.perf_counter() - t0) * 1000

def simulated_annealing(initial_temp=200.0, cooling=0.995, min_temp=1e-3, max_steps=25000):
    t0 = time.perf_counter()
    current = random_order()
    current_cost = order_cost(current)
    best, best_cost = current[:], current_cost
    temp, steps = initial_temp, 0
    while temp > min_temp and steps < max_steps:
        i, j = random.sample(range(len(current)), 2)
        nbr = current[:]
        nbr[i], nbr[j] = nbr[j], nbr[i]
        cand_cost = order_cost(nbr)
        delta = cand_cost - current_cost
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current, current_cost = nbr, cand_cost
            if current_cost < best_cost:
                best, best_cost = current[:], current_cost
        temp *= cooling
        steps += 1
    return best, best_cost, (time.perf_counter() - t0) * 1000

def beam_search(width=4):
    t0 = time.perf_counter()
    beam = [([], START, 0)]
    for _ in range(len(TARGETS)):
        candidates = []
        for partial, last, cost_so_far in beam:
            for nxt in [n for n in TARGETS if n not in partial]:
                candidates.append((partial + [nxt], nxt, cost_so_far + dist_map[last][nxt]))
        candidates.sort(key=lambda x: x[2])
        beam = candidates[:width]
    best_partial, _, best_cost = min(beam, key=lambda x: x[2])
    return best_partial, best_cost, (time.perf_counter() - t0) * 1000

if __name__ == "__main__":
    hc_order, hc_cost, hc_time = hill_climbing()
    sa_order, sa_cost, sa_time = simulated_annealing()
    bs_order, bs_cost, bs_time = beam_search(width=4)

    results = [
        ("Hill Climbing",         hc_order, hc_cost, hc_time),
        ("Simulated Annealing",   sa_order, sa_cost, sa_time),
        ("Beam Search (width=4)", bs_order, bs_cost, bs_time),
    ]

    for name, order, cost, runtime in results:
        route = [START] + order
        print(f"[{name}]")
        print(f"  Route : {' -> '.join(route)}")
        print(f"  Cost  : {cost}  |  Time: {runtime:.3f} ms")
        print()

    best = min(results, key=lambda x: (x[2], x[3]))
    print("-" * 50)
    print(f"Best Algorithm : {best[0]}")
    print(f"Best Cost      : {best[2]}")
    print(f"Best Time      : {best[3]:.3f} ms")