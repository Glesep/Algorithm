from collections import defaultdict
from collections import deque
import heapq

class Node:
    
    def __init__(self, word, next = None, weight = 1):
        self.word = word
        self.weight = weight
        self.next = next

# dict의 value들 == Tree 객체가 됨
class Tree:
    
    # title : 연결되는 대상이 되는 노드 (dict의 key로 표현됨)
    # root : Node 객체, title과 연결되어 있는 노드
    def __init__(self, title, root=None):
        self.title = title
        self.root = root
        
    
    # 연관성이 있는 두 단어 A와 B를 연결하는 에지의 가중치는
    # 단어 A의 설명에 B 등장횟수 + 단어 B의 설명에 A 등장횟수    
    def push(self, word):
        tmp = Node(word, self.root)     # root를 자식으로 하는 노드를 만들고
        self.root = tmp                 # 자신이 루트가 됨
        
        
    def search(self, target):
        
        p = self.root
        # q = None
        
        while p != None:
            if p.word == target:
                return p    # target을 찾았으므로 바로 반환
            p = p.next
        
        return p            # None 반환
    
                
    def update(self, Node_target):
        Node_target.weight += 1
        
    def traversal(self):
        result = {}
        p = self.root
        
        while p != None:
            result[p.word] = p.weight
            p = p.next
        
        return result
            
# graph_dict : Tree 객체를 요소로 하는 defaultdict
def make_graph(word, title, graph_dict):
    
    # 연관성이 없었던 경우 1 - 둘 중 하나라도 edge 트리를 가지지 않을 경우
    if not word in graph_dict.keys() or not title in graph_dict.keys():
        
        if not word in graph_dict.keys():
            graph_dict[word] = Tree(word)
            
        if not title in graph_dict.keys():
            graph_dict[title] = Tree(title)
        
        graph_dict[word].push(title)
        graph_dict[title].push(word)
    
    # 둘 다 edge 트리를 가질 경우
    else:
        
        result_1 = graph_dict[title].search(word)
        result_2 = graph_dict[word].search(title)   # 상대 노드도 가져오기

        # 연관성이 존재하는 경우
        if result_1 != None and result_2 != None:

            graph_dict[title].update(result_1)          #각각 가중치 1씩 업데이트
            graph_dict[word].update(result_2)
            
        # 연관성이 없었던 경우 3 - 둘 다 edge 트리를 가질 경우
        else:
            graph_dict[word].push(title)
            graph_dict[title].push(word)
            
                
def answer1(graph_dict):
    # 정점 개수 파악(n)
    vertex = len(graph_dict.keys())
    edge = 0 
    
    # 에지 개수 세기 (2m)
    for tree in graph_dict.values():
        p = tree.root
        
        while p != None:
            edge += 1
            p = p.next
    
    print ('Answer1:', vertex, int(edge/2))
    
def answer2(graph_dict):
    vertex_max = ''
    degree_max = -1
    for vertex, edge_tree in graph_dict.items():
        
        p = edge_tree.root
        degree = 0
        
        while p != None:
            degree += 1
            p = p.next
        
        if degree > degree_max:
            degree_max = degree
            vertex_max = vertex

    print('Answer2:', vertex_max, degree_max)
    
# DFS
# 함수 들어올때 v를 인식하며 들어오므로 component_sum의 초기 값은 1
def DFS(graph_dict, v, visited):
    visited[v] = 1
    component_sum = 1
    
    p = graph_dict[v].root
    
    while p != None:
        if visited[p.word] == 0:
            component_sum += DFS(graph_dict, p.word, visited)
        p = p.next
    
    return component_sum

def answer3(graph_dict):
    # visited 초기화
    visited = {key:0 for key in graph_dict.keys()}
    compo_max = -1
    while 0 in visited.values():
        v = None
        for key, value in visited.items():
            if value == 0:
                v = key
                break
            
        # (python)변경 가능한 객체를 매개변수로 받아와 함수 안에서 작업하면 함수 밖에 존재하는 실체에도 값이 적용됨
        compo_sum = DFS(graph_dict, v, visited)
        if compo_sum > compo_max:
            compo_max = compo_sum
    
    print('Answer3:', compo_max)   

# BFS
def answer4(word, k, graph_dict):
    
    print_total = 0   # 출력된 단어의 개수
    distance = {key : -1 for key in graph_dict.keys()}
    q = deque()
    
    # 시작 노드 초기화
    distance[word] = 0
    q.append(graph_dict[word])
    print(word)
    print_total += 1
    
    while q:        # q가 비어있지 않을 동안 반복
        target = q.popleft()
        
        if distance[target.title] > k:
            break
        
        p = target.root
        
        while p != None:    # 해당 노드에 인접한 노드 확인
            
            if distance[p.word] == -1:
                distance[p.word] = distance[target.title] + 1
                q.append(graph_dict[p.word])
                print(p.word)
                print_total += 1
                
            p = p.next
    
    print(print_total)

# Dijkstra
def answer5(graph, start_node, end_node):
    """
    다익스트라 알고리즘을 사용하여 주어진 그래프에서 최단 경로를 찾습니다.

    :param graph: graph_dict (defaultdict(Tree) 형태)
    :param start_node: 시작 노드 (단어)
    :param end_node: 도착 노드 (단어)
    :return: (최단 경로 리스트, 총 가중치) 또는 경로가 없을 경우 (None, float('inf'))
    """
    # 시작 또는 도착 노드가 그래프에 없는 경우
    if start_node not in graph.keys() or end_node not in graph.keys():
        return None, float('inf')

    # 시작 노드로부터 모든 노드까지의 거리를 저장할 딕셔너리 (초기값: 무한대)
    distances = {node: float('inf') for node in graph.keys()}
    # 시작 노드의 거리는 0으로 초기화
    distances[start_node] = 0
    
    # 경로 복원을 위해 이전 노드를 기록할 딕셔너리
    predecessor = {node: None for node in graph.keys()}

    # 우선순위 큐(최소 힙) 생성 후 시작 노드 추가. (거리, 노드) 튜플 형태
    priority_queue = [(0, start_node)]

    while priority_queue:
        # 현재 가장 거리가 짧은 노드를 큐에서 추출
        current_distance, current_node = heapq.heappop(priority_queue)

        # 이미 처리된 노드(더 짧은 경로가 발견된 노드)라면 건너뛰기
        if current_distance > distances[current_node]:
            continue

        # 목표 노드에 도달했다면, 경로를 재구성하여 반환하고 종료
        if current_node == end_node:
            path = []
            node = end_node
            while node is not None:
                path.append(node)
                node = predecessor[node]
            # 경로를 시작 -> 도착 순으로 뒤집기
            return path[::-1], distances[end_node]

        # 현재 노드와 연결된 이웃 노드들을 확인
        # traversal() 메서드가 {이웃노드: 가중치} 딕셔너리를 반환
        neighbors = graph[current_node].traversal()
        
        neighbors = {key: 1 / value for key, value in neighbors.items() if value != 0}
        
        
        for neighbor, weight in neighbors.items():
            # 현재 노드를 거쳐 이웃 노드로 가는 새로운 거리 계산
            distance = current_distance + weight

            # 새로운 경로가 기존 경로보다 짧은 경우
            if distance < distances[neighbor]:
                # 거리와 이전 노드 정보 업데이트
                distances[neighbor] = distance
                predecessor[neighbor] = current_node
                # 우선순위 큐에 새로운 (거리, 이웃 노드) 추가
                heapq.heappush(priority_queue, (distance, neighbor))

    # 큐가 비었는데 도착 노드에 도달하지 못했다면 경로가 없는 것
    return None, float('inf')   
        
# ================================================================================

with open('./files/dict_simplified.txt', 'r') as f:
    explain_word = defaultdict(str)
    
    # 단어 저장을 이렇게 할 수 있음
    for line in f:
        word, explain = line.split('\t')
        explain_word[word] = explain
    
graph_dict = defaultdict(Tree)


# graph 만들기
for title, value in explain_word.items():
    # 설명 내의 단어를 확인
    for word in value.split():
        # word가 사전의 단어들에 속한다면 (title에 속한다면)
        if word in explain_word.keys():
            make_graph(word, title, graph_dict)

# input_4 = input('Answer4 input(word, k) : ')
# # input_5 = input('Answer5 input : (word_1, word_2)')

# word_input_4, k = input_4.split()



# answer1(graph_dict)
# answer2(graph_dict)
# answer3(graph_dict)
# answer4(word_input_4, int(k), graph_dict)
print(dijkstra(graph_dict, 'parity', 'parcel'))
