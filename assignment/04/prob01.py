# 더이상 suffix가 존재하지 않거나 (즉 [end]에 도달하거나) 혹은 생성할 랜덤 텍스트의 길이의 최대값에 도달하면 종료한다.
# 가짜 텍스트의 최대 길이는 100단어로 하라.
import random





def make_random_text(first, second, result='', length=0):
    
    tuple_target = (first, second)
    
    # [end]가 suffix인 경우
    if dict_Markov[tuple_target][0] == '[end]':
        return result
    
    if len(dict_Markov[tuple_target]) > 1:  # value list 내 요소가 2개 이상인 경우
        index = [idx for idx in range(len(dict_Markov[tuple_target]))]
        
        target_word = ''
        while index:
            random_index = index.pop(random.choice(index))
            
            if len(result + ' ' + dict_Markov[tuple_target][random_index]) > 100:
                continue
            else:
                target_word = dict_Markov[tuple_target][random_index]
                break
            
        if target_word == '':   # 랜덤 텍스트의 길이가 100이 넘는 경우
            return result
      
    else:       # value list 내 요소가 2개 이상인 경우
        target_word = dict_Markov[tuple_target][0]
        
    return make_random_text(second, target_word, result+' '+target_word, len(result+' '+target_word))
                

# ========================================================================================================================
if __name__ == "__main__":

    dict_Markov = dict()
    # 데이터 전처리
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
        words.append('[end]')

    first = ''
    second = ''

    for word in words:

        if first == '':
            first = word
        elif second == '':
            second = word

        else:

            # key 생성
            tuple_words = (first, second)

            if tuple_words in dict_Markov.keys():   # 이미 존재하는 key일 경우
                if word not in dict_Markov[tuple_words]:    # word value가 없는 경우만 삽입
                    dict_Markov[tuple_words].append(word)

            else:
                # key에 대한 리스트에 word를 추가해 넣음
                dict_Markov[tuple_words] = [word]

            # 앞으로 하나씩 밀기
            # if words
            first = second
            second = word

    print(dict_Markov.keys())
    input_str = input()
    
    input_first, input_second = input_str.split()

    
    # print(words)
    # print(('did.', '[end]') in dict_Markov.keys())
    result = make_random_text(input_first, input_second)       
    
    print(result)
    

