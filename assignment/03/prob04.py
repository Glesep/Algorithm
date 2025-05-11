class Node:
    def __init__(self, address_dict, parent=None):
        self.address_dict = address_dict      # 한 사람의 address 정보가 dict형태로 저장됨
        self.left = None
        self.right = None
        self.parent = parent  # 부모 노드 참조
        
    def print_info(self):   # 노드의 정보를 출력하는 함수
        """노드가 가지고 있는 address_dict 내 정보를 출력하는 함수
        """
        for key, value in self.address_dict.items():
            if key == 'Name':
                print(self.address_dict['Name'])
            else:
                print(f'\t{key}: {value}')
    
    def to_datastream_(self):
        """address_dict의 value값을 문자열로 직렬화

        Returns:
            datastream: 직렬화된 value값
        """
        values = [value for _, value in self.address_dict.items()]

        datastream = ""
        datastream += '\t'.join(values) + '\n'
        
        return datastream
            
# =========================================================================

class address_BST:
    def __init__(self):
        self.root = None

    def insert(self, node):
        """BST에 새로운 노드를 삽입하는 함수

        Args:
            node (Node): 삽입할 노드 객체
        """
        y = None
        x = self.root
        
        while x != None:
            # x가 NIL 이 될때까지 타고 감 - y를 뒤따라오게함
            y = x
            if node.address_dict['Name'] < x.address_dict['Name']:
                x = x.left
            else:
                x = x.right
        
        # 삽입될 위치는 y의 자식 - 왼쪽인지 오른쪽인지 판별
        node.parent = y
        if node.parent == None:
            self.root = node
        elif node.address_dict['Name'] < node.parent.address_dict['Name']:
            node.parent.left = node
        else:
            node.parent.right = node
    
    def delete_(self, name):
        """BST 내에 이름으로 특정된 노드를 삭제

        Args:
            name (str): 찾고 싶은 노드의 address_dict['Name']에 해당하는 문자열
        """
        # 이름으로 특정된 노드를 찾기
        node_del_forLogic = self.search(self.root, name)
        
        # 해당 이름을 가진 노드가 없을 때 - 함수 종료
        if not node_del_forLogic.address_dict:
            print(f"{name}'s information does not exist.")
            return
        
        
        # leaf 노드 or 자식 노드가 1개일 경우
        if node_del_forLogic.left == None or node_del_forLogic.right == None:
            node_del_forReal = node_del_forLogic
        # 자식 노드가 2개일 경우
        else:
            node_del_forReal = self.tree_successor(node_del_forLogic)
        
        
        # 실제 삭제하는 노드의 왼쪽 자식이 있다 - successor 노드는 아님
        if node_del_forReal.left != None:   # 자식이 0개 아니면 1개 - 오른쪽 자식은 무조건 없음
            x = node_del_forReal.left
        else:
            x = node_del_forReal.right      # 만약 오른쪽 있으면 오른쪽 들어가고 없으면 None
        
        # 실제 삭제되어야 하는 노드를 삭제
        if x != None:       # 삭제될 노드의 부모를 자신의 부모로 삼음 - node_del_forReal를 삭제 
            x.parent = node_del_forReal.parent
        
        # 삭제될 노드의 부모가 없음 - 루트 노드가 삭제됨 - 자식이 루트로
        if node_del_forReal.parent == None:
            self.root = x
        
        # 삭제되는 노드가 루트노드를 제외한 내부 노드일 때
        elif node_del_forReal == node_del_forReal.parent.left:
            node_del_forReal.parent.left = x
        
        else:
            node_del_forReal.parent.right = x
        
        # 자식이 2개일 경우 - 진짜 삭제되는 노드와 논리적으로 삭제되는 노드가 다름
        if node_del_forReal != node_del_forLogic:       # successor 위치를 대신 삭제하는 경우
            
            # 자식 노드 관계는 위에서 다 정리됨. 나머지 데이터만 들고오기
            node_del_forLogic.val = node_del_forReal.val
            node_del_forLogic.parent = node_del_forReal.parent

            del node_del_forReal
            
        print(f"{name} was successfully deleted.")
        
        
    def search(self, x, k):
        """ 찾고 싶은 사람의 존재 유무를 사람의 이름을 매개로 검색하는 함수

        Args:
            x (node): node(일반적으로 root)
            k (str): 사람의 이름
        Returns:
            Node (Node): 존재하면 해당 노드 반환, 존재하지 않으면 빈 노드 반환
        """
        if x == None:
            return Node(None)       # 존재하지 않으면 빈 노드 반환
        elif k == x.address_dict['Name']:
            return x
            
        if k < x.address_dict['Name']:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)
        
    def trace_name(self, x, k):
        """ 이름으로 검색하면서 루트에서 해당 노드까지 찾아가는 동안
            방문하는 모든 노드에 저장된 이름들을 한 줄에 하나씩 출력한다.

        Args:
            x (node): node(일반적으로 root)
            k (str): 사람의 이름
        Returns:
            Node (Node): 존재하면 해당 노드 반환, 존재하지 않으면 빈 노드 반환
        """
        if x == None:
            return Node(None)       # 존재하지 않으면 빈 노드 반환
        elif k == x.address_dict['Name']:
            return x
            
        print(x.address_dict['Name'])
        
        if k < x.address_dict['Name']:
            return self.trace_name(x.left, k)
        else:
            return self.trace_name(x.right, k)
    
    def to_datastream(self, node):
        """BST에 속한 Node의 to_datastream_() 함수를 preorder로 실행

        Args:
            node (Node): 시작할 Node 객체 - 보통 root

        Returns:
            list: 직렬화한 데이터를 모은 리스트
        """
        serialized_data = []
        if node:    # 노드 != NIL
            serialized_data.append(node.to_datastream_())
            serialized_data += self.to_datastream(node.left)
            serialized_data += self.to_datastream(node.right)
        
        return serialized_data
    
    def tree_min(self, x):
        while x.left != None:
            x = x.left
            
        return x
    
    def tree_successor(self, x):
        if x.right != None:
            return self.tree_min(x.right)
        x_parent = x.parent
        
        while x_parent != None and x == x_parent.right:
            x = x_parent
            x_parent = x_parent.parent
        
        return x_parent

    def inorder_traversal(self, node):
        
        if node:    # 노드 != NIL
            self.inorder_traversal(node.left)
            node.print_info()
            self.inorder_traversal(node.right)
        
# =========================================================================

def read(filename):
    """filename에 해당하는 파일 내 데이터를 읽고 BST 형태로 저장

    Args:
        filename (str): file 이름 (확장자까지 입력)
    Returns:
        BST_address  : BST 객체 반환
    """
    with open(f"./files/{filename}", 'r', encoding='utf-8-sig') as f:
        f.readline()        # dummy 제거
        data = f.readlines()

        # 데이터 정리
        for i in range(len(data)):
            data[i] = data[i].strip().split('\t')

        columns = ['Name', 'Company', 'Address', 'Zipcode', 'Phones', 'Email']

        BST_address = address_BST()     # BST 객체 생성

        # 해당 node 생성 후, BST에 저장
        for address_info in data:

            address_dict = {key: value for key, value in zip(columns, address_info)}
            node = Node(address_dict)
            BST_address.insert(node)

        del data        # 필요 없어진 리스트형 데이터 삭제
        
    return BST_address
        
def list(BST_address):
    BST_address.inorder_traversal(BST_address.root)

def find(BST_address, name):
    target = BST_address.search(BST_address.root, name)
    
    if target.address_dict:
        target.print_info()
    else:
        print(f"{name}'s information does not exist.")

def trace(BST_address, name):
    target = BST_address.trace_name(BST_address.root, name)
    
    if target.address_dict:
        print(target.address_dict['Name'])
    else:
        print(f"{name}'s information does not exist.")

def add(BST_address, name):
    """BST_address에 name에 해당하는 address 정보를 저장

    Args:
        BST_address (BST): address 정보가 들어있는 BST 객체
        name (str): 문자열로 표현된 이름

    Returns:
        BST: 저장 과정이 끝난 BST
    """
    target = BST_address.search(BST_address.root, name)
    
    if target.address_dict:
        print(f"{name}'s information exists.")
        return BST_address
    
    else:
        address_info = [name]
        columns = ['Name', 'Company', 'Address', 'Zipcode', 'Phones', 'Email']
        
        for column in columns[1:]:
            address_info.append(input(f'{column}? '))
            
        address_dict = {key: value for key, value in zip(columns, address_info)}
        node = Node(address_dict)
        BST_address.insert(node)
        
        print(f"{name} was successfully added.")
        
        return BST_address

def delete(BST_address, name):
    BST_address.delete_(name)
    
def save(BST_address, filename):
    serialize_data = BST_address.to_datastream(BST_address.root)
    
    with open(f"./files/{filename}", "w", encoding='utf-8-sig') as f:
        f.write('name\tcompany_name\taddress\tzip\tphone\temail\n')
        f.writelines(serialize_data)
        
# =========================================================================
def app():
    while True:
        command = input().split()
        if command[0] == 'read':
            BST_address = read(command[1])
            
        if command[0] == 'list':
            list(BST_address)
        
        elif command[0] == 'find':
            find(BST_address, command[1])
        
        elif command[0] == 'add':
            add(BST_address, command[1])
        
        elif command[0] == 'trace':
            trace(BST_address, command[1])
        
        elif command[0] == 'delete':
            delete(BST_address, command[1])
        
        elif command[0] == 'save':
            save(BST_address, command[1])
        
        elif command[0] == 'exit':
            break

# =========================================================================
if __name__ == "__main__":
    app()