import json
import heapq
from collections import defaultdict

def find_cheapest_price(n, flights, src, dst, k):
    graph = defaultdict(list)
    for s, d, p in flights:
        graph[s].append((d, p))

    heap = [(0, src, 0)]  # (cost, city, stops)
    visited = {}

    while heap:
        #pop the smallest cost node
        cost, city, stops  = heapq.heappop(heap)

        # If reach destination within stops
        if city == dst:
            return cost

        # If stops exceed limit, skip
        if stops > k:
            continue

        # If visited city with fewer stops before, skip
        if city in visited and visited[city] <= stops:
            continue
        
        # Add city to track visited cities with stops
        visited[city] = stops

        # Explore all neighboring cities (next possible flights)
        for dest, price in graph[city]:
            new_cost = cost + price
            heapq.heappush(heap, (new_cost, dest, stops + 1))
  
    return -1


def load_data():
    try:
        with open("flight.json", "r") as f:
            return json.load(f)
    except:
        print("⚠️ flight.json not found. Please ensure the file exists.")
        exit(1)
