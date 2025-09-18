import heapq

def min_cost_cables(lengths):
    heapq.heapify(lengths)
    total_cost = 0

    while len(lengths) > 1:
        # беремо два найкоротші
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)
        cost = first + second
        total_cost += cost
        # додаємо назад
        heapq.heappush(lengths, cost)

    return total_cost

cables = [4, 3, 2, 6, 5, 1, 8]
print(min_cost_cables(cables))  
