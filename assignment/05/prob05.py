from collections import defaultdict

class Node:
    
    
    def __init__(self, word, next = None, weight = 1):
        self.word = word
        self.weight = weight
        self.next = next


# dict의 value들 == Tree 객체가 됨
class Tree:
    
    # title : 연결되는 대상이 되는 노드 (dict의 key로 표현됨)
    # root : Node 객체, title과 연결되어 있는 노드
    def __init__(self, root=None):

        self.root = root
        
    
    # 연관성이 있는 두 단어 A와 B를 연결하는 에지의 가중치는
    # 단어 A의 설명에 B 등장횟수 + 단어 B의 설명에 A 등장횟수    
    def push(self, word):
        tmp = Node(word, self.root)     # root를 자식으로 하는 노드를 만들고
        self.root = tmp     # 자신이 루트가 됨
        
        
    def search(self, target):
        
        p = self.root
        # q = None
        
        while p != None:
            if p.word == target:
                return p    # target을 찾았으므로 바로 반환
            p = p.next
        
        return p        # None 반환
    
                
    def update(self, Node_target):
        Node_target.weight += 1
        
    def traversal(self):
        dict = {}
        p = self.root
        
        while p != None:
            dict[p.word] = p.weight
            p = p.next
        
        return dict
            
        
        

# graph_dict : Tree 객체를 요소로 하는 defaultdict
def make_graph(word, title, graph_dict):
    
    # 연관성이 없었던 경우 1 - 둘 중 하나라도 edge 트리를 가지지 않을 경우
    if not word in graph_dict.keys() or not title in graph_dict.keys():
        
        if not word in graph_dict.keys():
            graph_dict[word] = Tree()
            
        if not title in graph_dict.keys():
            graph_dict[title] = Tree()
        
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
            
                
                
            


with open('./files/dict_simplified.txt', 'r') as f:
    explain_word = defaultdict(str)
    
    # 단어 저장을 이렇게 할 수 있음
    for line in f:
        word, explain = line.split('\t')
        explain_word[word] = explain
    
graph_dict = defaultdict(Tree)


# dict의 dict로

# 사전 내 각 단어와 그에 대한 설명 확인
# value = dict 타입
for title, value in explain_word.items():
    # 설명 내의 단어를 확인
    for word in value.split():
        # word가 사전의 단어들에 속한다면 (title에 속한다면)
        if word in explain_word.keys():
            make_graph(word, title, graph_dict)
                
print(graph_dict['volcano'].traversal())