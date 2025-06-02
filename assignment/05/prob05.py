from collections import defaultdict


# 인접리스트 구현을 위한 edge 클래스 정의
class edge:
    
    def __init__(self, weight, node=None):
        self.weight = weight
        self.node = node
        

        
        
    
    


with open('./files/dict_simplified.txt', 'r') as f:
    explain_word = defaultdict(str)
    
    # 단어 저장을 이렇게 할 수 있음
    for line in f:
        word, explain = line.split('\t')
        explain_word[word] = explain
    
graph = defaultdict(edge)

for key, value in explain_word:
    for word in value.split():
        