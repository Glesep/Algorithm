# 더이상 suffix가 존재하지 않거나 (즉 [end]에 도달하거나) 혹은 생성할 랜덤 텍스트의 길이의 최대값에 도달하면 종료한다.
# 가짜 텍스트의 최대 길이는 100단어로 하라.

dict_Markov = dict()

with open('./files/HarryPotter.txt', 'r') as f:
    harry = f.readlines()
    
    # 데이터 정리
    for i in range(len(harry)):
        harry[i] = harry[i].strip().split('\t')
    harry = [line for sublist in harry for line in sublist if line != '']
    
    script = ''
    for line in harry:
        script += line + ' '
        
    words = script.split()

print(words)

