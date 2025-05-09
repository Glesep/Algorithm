# flag를 둬서 BST인지 확인
def isBST_postorder(node_val, level=1):
    """
    Args:
        node_val (list): node의 value값이 postorder로 표현된 list
        level (int, optional): 현재 tree의 level. root 노드의 level = 1

    Returns:
        level (int): BST의 postorder가 아니라면 -1, 맞다면 BST의 height
    """
    is_small = True          # 값이 root node의 val보다 큰지 작은지 나타내는 flag
    split_index = None       # 서브트리로 나눠질 index
    
    if len(node_val) == 1:      # leaf node일 때
        return level
    
    elif not node_val:          # 이전 단계에서 root_val이 그 외 node_val보다 전부 작았을 때 (split_index = 0)
        return level-1
    
    root_val = node_val[-1]
    
    for i in range(0, len(node_val)):   # root node와 그 외 노드를 하나씩 검사
        if is_small:
            if node_val[i] > root_val:  # root_val보다 처음으로 큰 값일 때
                split_index = i
                is_small = False
        
        else:
            if node_val[i] < root_val:  # root_val보다 큰 값이 있어야 할 서브트리에 작은 값이 있을 때 -> BST 불가
                return -1
    
    
    if split_index == None: # root_val이 다른 값 전부보다 클 때
        split_index = -1
        
    # recursion
    left_height = isBST_postorder(node_val[:split_index], level+1)
    right_height = isBST_postorder(node_val[split_index:-1], level+1)
    
    # BST가 불가한 곳이 나왔다면
    if left_height == -1 or right_height == -1:
        return -1
    else:
        return max(left_height, right_height)

N = int(input())
node_val = [*map(int, input().split())]
print(isBST_postorder(node_val))