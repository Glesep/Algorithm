# 10개의 0으로 초기화
count_list = [0] * 10     # counting 하는 숫자는 1~9 범위

def counting_sort(target_list, count_range):
    """ target_list 내에 있는 숫자의 범위를 알 때 사용할 수 있는 counting sort를 구현한 함수입니다.

    Args:
        target_list (list): 정렬의 대상이 될 list
        count_range (int): 숫자의 범위를 알려주는 정수. ex) [0,10) -> 10

    Returns:
        _type_: _description_
    """
    sorted_list = [0] * len(target_list)    # 정답이 저장될 list - target_list 개수만큼 뚫기
    count_list = [0] * count_range          # 각 수는 count_range개의 범위에 있음

    
    for j in range(len(target_list)):       # target_list에 존재하는 정수의 개수를 저장함
        count_list[target_list[j]] += 1
    
    for i in range(1, count_range):         # count_list에 저장되어있는 정수의 개수의 누적합을 왼쪽에서 오른쪽으로 구함
        count_list[i] = count_list[i]+count_list[i-1]
    
    for j in range(len(target_list)-1, -1, -1):     # counting sort
        sorted_list[count_list[target_list[j]]-1] = target_list[j]
        count_list[target_list[j]] -= 1
        
    return sorted_list

# ====================================================================

def counting_sort_forRadix(target_list, count_range, d_index):
    """ target_list 내에 있는 숫자의 범위를 알 때 사용할 수 있는 counting sort를 구현한 함수입니다.
        - radix sort에 이용되는 개량판
    Args:
        target_list (list): 정렬의 대상이 될 list
        count_range (int): 숫자의 범위를 알려주는 정수. ex) [0,10) -> 10
        d_index (int): target_list 내 숫자의 어느 자릿수로 counting_sort를 할껀지를 정하는 매개변수
        ex) 3자리 - 천, 백, 일 = 0, 1, 2

    Returns:
        list: counting sort 된 결과물
    """
    # count_list 초기화 해결
    sorted_list = [0] * len(target_list)    # 정답이 저장될 list
    count_list = [0] * count_range
    
    
    for j in range(len(target_list)):       # target_list에 존재하는 정수의 개수를 저장함
        count_list[int(target_list[j][d_index])] += 1
    
    for i in range(1, count_range):         # count_list에 저장되어있는 정수의 개수의 누적합을 왼쪽에서 오른쪽으로 구함
        count_list[i] = count_list[i]+count_list[i-1]
    
    for j in range(len(target_list)-1, -1, -1):     # counting sort - 해당 자릿수(d_index)를 기준으로 전체 수를 옮김
        sorted_list[count_list[int(target_list[j][d_index])]-1] = target_list[j]
        count_list[int(target_list[j][d_index])] -= 1
        
    return sorted_list


def radix_sort(target_list, d):
    """counting sort를 d번 수행 - 이거는 숫자의 자릿수로 구현됨

    Args:
        target_list (list): radix sort를 적용할 리스트
        d (int): 숫자 자릿수 범위 - ex) 천의 자릿수까지 있으면 3

    Returns:
        list: 결과물
    """
    target_list = list(map(str, target_list))
    
    for d_index in range(d-1, -1, -1):  # 0, 1, 2
        target_list = counting_sort_forRadix(target_list, 10, d_index)
    
    target_list = list(map(int, target_list))
    
    return target_list



# ====================================================================


target = [329, 457, 657, 839, 436, 720, 355]

result = radix_sort(target, 3)

print(result)