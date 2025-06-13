import collections

class DAG:
    """
    칸 알고리즘 구현을 위한 DAG(방향성 비순환 그래프) 자료구조 클래스.
    
    속성:
    - V (int): 그래프의 정점(vertex) 개수
    - graph (defaultdict): 인접 리스트 방식으로 그래프를 저장 (u -> [v1, v2, ...])
    - indegree (list): 각 정점의 진입 차수를 저장하는 리스트
    """
    
    def __init__(self, vertices):
        """
        그래프를 초기화합니다.
        
        Args:
            vertices (int): 그래프에 포함될 정점의 총 개수 (보통 0부터 V-1까지).
        """
        self.V = vertices
        # 인접 리스트: 키가 존재하지 않을 경우 빈 리스트를 기본값으로 생성
        self.graph = collections.defaultdict(list)
        
        # 방문 여부를 기록하는 visited
        self.visited = collections.defaultdict(int)

    def add_edge(self, u, v):
        """
        방향성 간선(u -> v)을 그래프에 추가합니다.
        
        Args:
            u (int): 시작 정점 (출발 노드)
            v (int): 도착 정점 (도착 노드)
        """
        # u의 인접 리스트에 v를 추가
        self.graph[u].append(v)
    
    def topological_sort2(self):
        
        # 위상 정렬의 결과가 될 deque
        topological_order = collections.deque()
        
        # for node in self.graph.keys():    # 이렇게 사용하면 graph(defaultdict())의 크기가 바뀌는 순간 오류
        for node in self.graph.copy().keys():
            if self.visited[node] == 0:
                self.DFS_TS(node, topological_order)
        
        return topological_order
                
    def DFS_TS(self, node, topological_order):
        self.visited[node] = 1
        
        for adj_node in self.graph[node]:
            if self.visited[adj_node] == 0:
                self.DFS_TS(adj_node, topological_order)
        
        topological_order.appendleft(node)
        
    # --- 예제 사용법 ---
if __name__ == "__main__":
    # 예제 1: 일반적인 DAG
    print("--- 예제 1: 사이클이 없는 경우 ---")
    g1 = DAG(6)
    g1.add_edge(5, 2)
    g1.add_edge(5, 0)
    g1.add_edge(4, 0)
    g1.add_edge(4, 1)
    g1.add_edge(2, 3)
    g1.add_edge(3, 1)

    # 그래프 구조:
    # 5 -> 2 -> 3
    # |         |
    # v         v
    # 0 <- 4 -> 1

    result1 = g1.topological_sort2()
    if result1:
        print(f"위상 정렬 결과: {result1}") # 예시 출력: [4, 5, 0, 2, 3, 1]

    print("\n" + "="*30 + "\n")