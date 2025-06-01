# GA05 - 4번 해답

from collections import defaultdict

# 윈도우의 총 개수 : n-k-0+1
# 윈도우 이동 횟수 : n-k번
# 초기 윈도우 초기화 : O(k)
# 윈도우 이동 후 빠지는 문자와 새로 들어오는 문자의 빈도수를 각각 O(1)에 처리 가능
# 윈도우 이동은 총 n-k번 이루어지므로 시간복잡도 : O(n-k)
def count_distinct(X, k):
    freq = defaultdict(int)     # 명시적으로 key에 대한 값을 적지 않은 채로 사용 시, 초기값은 0(int)으로 자동 적용
    distinct = 0
    result = []

    # 초기 윈도우 : 인덱스 0 ~ K-1
    for i in range(k):
        if freq[X[i]] == 0:
            distinct += 1
        freq[X[i]] += 1
    result.append(distinct)

    # 슬라이딩 윈도우
    
    for i in range(k, len(X)):  # 마지막 윈도우 : 인덱스 n-k ~ n-1
        # 왼쪽 문자 제거
        left = X[i - k]     # 리스트에서 윈도우의 왼쪽에 해당하는 문자 들고옴
        freq[left] -= 1     # 윈도우에서 삭제
        if freq[left] == 0:
            distinct -= 1

        # 오른쪽 문자 추가
        right = X[i]
        if freq[right] == 0:    # 리스트에서 윈도우의 오른쪽에 추가될 문자를 들고옴
            distinct += 1       # 윈도우에 추가
        freq[right] += 1

        result.append(distinct)

    return result


result = count_distinct([1, 2, 1, 3, 4, 2, 3], 4)
print(result)