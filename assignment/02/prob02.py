# 객체 정의
class person:
    
    def __init__(self, name, company, address, zipcode, phones, email):
        self.name = name
        self.company = company
        self.address = address
        self.zipcode = zipcode
        self.phones = phones
        self.email = email
    
    def print_info(self):
        print(self.name)
        print(f'    Company: {self.company}')
        print(f'    Zipcode: {self.zipcode}')
        print(f'    Phones: {self.phones}')
        print(f'    Email: {self.email}')
    
        
# read
def read_func(file):
    """파일명을 받아 파일 내에 있는 정보들을 사람별로 저장하는 함수입니다.

    Args:
        file (str): 파일명

    Returns:
        list: 정보들이 저장되어있는 객체들을 저장한 list
    """
    with open(f'./files/{file}') as f:
                person_list = [i.strip().split('|') for i in f.readlines()]

    people = [person(name.strip(), address.strip(), company.strip(), zipcode.strip(), phones.strip(), email.strip()) 
                for name, company, address, zipcode, phones, email in person_list]
    
    return people
    
# sort
def sort_func(list_people, key):
    """list_people 내 객체들을 객체의 멤버인 key를 기준으로 정렬하는 함수입니다.

    Args:
        list_people (list): 사람의 정보가 들어있는 객체가 저장된 리스트
        key (str): 정렬 기준이 될 객체의 멤버

    Returns:
        list: key 기준으로 정렬된 list
    """
    list_people.sort(key=attrgetter(f'{key}'))
    
    return list_people
    
    
# print
def print_func(list_people):
    """list_people 내에 있는 모든 객체의 print_info() 함수를 실행시키는 함수입니다.

    Args:
        list_people (list): person 객체가 들어있는 list
    """
    for p in list_people:
        p.print_info()

# main
from operator import attrgetter     # python 표준 라이브러리
 
def app():
    
    while True:
        user_input = input().split()
        
        if user_input[0] == 'read':
            file = user_input[1]
            people = read_func(file)

        if user_input[0] == 'sort':
            user_input[1] = user_input[1][1:]
            people = sort_func(people, user_input[1])
        
        if user_input[0] == 'print':
            print_func(people)

        if user_input[0] == 'exit':
            print('bye')
            break

app()