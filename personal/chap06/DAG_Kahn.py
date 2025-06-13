# DAG에서 indegree == 0인 노드가 없을 수 없다.
# why? - indegree == 0인 노드가 없다면 사이클이 존재하므로 DAG 정의에 위배

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
        # 진입 차수 리스트를 0으로 초기화
        self.indegree = [0] * self.V

    def add_edge(self, u, v):
        """
        방향성 간선(u -> v)을 그래프에 추가합니다.
        
        Args:
            u (int): 시작 정점 (출발 노드)
            v (int): 도착 정점 (도착 노드)
        """
        # u의 인접 리스트에 v를 추가
        self.graph[u].append(v)
        # v의 진입 차수를 1 증가
        self.indegree[v] += 1

    def topological_sort(self):
        """
        칸(Kahn's) 알고리즘을 사용하여 위상 정렬을 수행합니다.
        그래프에 사이클이 존재하면 빈 리스트를 반환합니다.
        
        Returns:
            list: 위상 정렬된 순서를 담은 리스트. 사이클이 있으면 빈 리스트 반환.
        """
        # 1. 진입 차수가 0인 모든 정점을 큐에 추가
        queue = collections.deque([i for i in range(self.V) if self.indegree[i] == 0])
        
        topological_order = []  # 위상 정렬 결과를 저장할 리스트
        
        # 2. 큐가 빌 때까지 반복
        while queue:
            # 큐에서 진입 차수가 0인 정점 u를 꺼냄
            u = queue.popleft()
            topological_order.append(u)
            
            # u와 인접한 모든 정점 v의 진입 차수를 1 감소
            for v in self.graph[u]:
                self.indegree[v] -= 1
                # 만약 v의 진입 차수가 0이 되면 큐에 추가
                if self.indegree[v] == 0:
                    queue.append(v)
        
        # 3. 사이클 탐지
        # 위상 정렬 결과 리스트의 길이가 전체 정점 수와 같다면 사이클이 없는 것
        if len(topological_order) == self.V:
            return topological_order
        else:
            # 다르다면, 사이클이 존재하여 모든 정점을 방문하지 못한 것
            print("오류: 그래프에 사이클이 존재합니다.")
            return []

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

    result1 = g1.topological_sort()
    if result1:
        print(f"위상 정렬 결과: {result1}") # 예시 출력: [4, 5, 0, 2, 3, 1]

    print("\n" + "="*30 + "\n")

    # 예제 2: 사이클이 있는 그래프
    print("--- 예제 2: 사이클이 있는 경우 ---")
    g2 = DAG(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.add_edge(3, 1) # 1 -> 2 -> 3 -> 1 사이클 발생

    result2 = g2.topological_sort()
    if not result2:
        print("사이클이 감지되어 위상 정렬을 수행할 수 없습니다.")

        

        

