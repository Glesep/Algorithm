from collections import defaultdict

with open('./files/dict_simplified.txt', 'r') as f:
    explain_word = defaultdict(str)
    
    # 단어 저장을 이렇게 할 수 있음
    for line in f:
        word, explain = line.split('\t')
        explain_word[word] = explain
    
graph = defaultdict(dict)

# 연관성이 있는 두 단어 A와 B를 연결하는 에지의 가중치는
# 단어 A의 설명에 B 등장횟수 + 단어 B의 설명에 A 등장횟수
# dict의 dict로

# 사전 내 각 단어와 그에 대한 설명 확인
# value = dict 타입
for key, value in explain_word.items():
    # 설명 내의 단어를 확인
    for word in value.split():
        # word가 사전의 단어에 속한다면 (key에 속한다면)
        if word in explain_word.keys():
            # 그래프에 존재하지 않는다면(word) 추가
            if not key in graph[word].keys():
                graph[word][key] = 1
                graph[key][word] = 1
            # 그래프에 존재한다면 weight 1 증가
            else:
                graph[word][key] += 1
                graph[key][word] += 1
                
print(graph['frostfish'])