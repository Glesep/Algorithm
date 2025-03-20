N = int(input())    # 정수의 개수
integer = [*map(int, input().split())]

# 현 위치의 숫자만큼 움직일 수 있음
# 0으로 빠지냐 안빠지냐만 생각하자
def IsPossible(index=0):
    
    if index == N-1:    # 맨 마지막 인덱스에 도착했을 때 - 성공
        return True
    elif integer[index] == 0:   # 맨 마지막 인덱스가 아닌데 0을 만남 - 실패
        return False
    
    else:
        move_count = integer[index]
       
        for i in range(move_count):      # 갈 수 있는 곳을 전부 탐색
            dist = i+1
            if IsPossible(index+dist):   # 이후의 경우가 가능하다면
                return True
        return False    # 다 탐색했는데 안 된다면 False
    
if IsPossible():
    print("Yes")
else:
    print("No")
        
        

