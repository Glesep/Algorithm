# 파이썬에서 매개변수에 빈 리스트를 초깃값으로 넣을 경우 - 매개변수로 다시 넣어주지 않아도 함수를 호출할 때마다 같은 리스트 객체를 참조함

# flag를 둬서 BST인지 확인
def post_to_pre(node_val):
    """
    Args:
        node_val (list): node의 value값이 postorder로 표현된 list

    Returns:
        preorder (list): postorder로 표현된 BST의 preorder 표현
    """
    
    preorder = []
        
    split_index = None       # 서브트리로 나눠질 index
    
    if not node_val:          # 이전 단계에서 root_val이 그 외 node_val보다 전부 작았을 때 (split_index = 0)
        return preorder
    
    # 현 트리의 root node를 추가
    root_val = node_val[-1]
    preorder.append(root_val)

    if len(node_val) == 1:      # leaf node일 때
        return preorder
    

    for i in range(0, len(node_val)):   # root node와 그 외 노드를 하나씩 검사
        if node_val[i] > root_val:  # root_val보다 처음으로 큰 값일 때
            split_index = i
            break
    
    if split_index == None: # root_val이 다른 값 전부보다 클 때
        split_index = -1
        
    # recursion
    pre_left = post_to_pre(node_val[:split_index])
    pre_right = post_to_pre(node_val[split_index:-1])
    
    # root, left, right 순으로 결합 (preorder)후 이전 단계로 return
    return preorder + pre_left + pre_right

N = int(input())
node_val = [*map(int, input().split())]
print(*post_to_pre(node_val))