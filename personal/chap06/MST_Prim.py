class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))
        
import heapq

def prim(graph, start=0):
    visited = set()
    min_heap = []
    mst_weight = 0
    mst_edges = []

    # 시작 노드의 모든 간선을 힙에 추가
    visited.add(start)
    for v, weight in graph[start]:
        heapq.heappush(min_heap, (weight, start, v))

    while min_heap and len(visited) < len(graph):
        weight, u, v = heapq.heappop(min_heap)
        if v in visited:
            continue
        visited.add(v)
        mst_weight += weight
        mst_edges.append((u, v, weight))
        for next_v, next_weight in graph[v]:
            if next_v not in visited:
                heapq.heappush(min_heap, (next_weight, v, next_v))

    return mst_weight, mst_edges

# Prim 알고리즘 실행 예시
mst_weight, mst_edges = prim(graph, start=0)
print("MST weight:", mst_weight)
print("MST edges:", mst_edges)
