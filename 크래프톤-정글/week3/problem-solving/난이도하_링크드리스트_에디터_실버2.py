# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406
import sys 
input = sys.stdin.readline 

class Node: 
    def __init__(self, data, prev=None, next=None):
        self.data = data 
        self.prev = prev 
        self.next = next

class LinkedList: 
    def __init__(self):
        self.head = None 
        self.current = None 

    # 리스트 맨 뒤에 노드를 추가하는 함수
    def append(self, data):
        # 리스트가 비어 있을때
        if self.head is None:      
            self.head = Node(data)
            self.current = self.head 
            return
 
        # 리스트가 비어 있지 않다면 현재 마지막 노드 뒤에 새 노드 추가 
        new_node = Node(data)
        self.current.next = new_node
        new_node.prev = self.current 
        self.current = self.current.next 

    # 현재 커서 왼쪽 위치에 문자 삽입 
    def cursor_append(self, data):    
        # current가 존재할때만 삽입 가능  
        if self.current is not None: 
            # current가 head라는 뜻은
            # 커서가 맨 앞에 있다는 뜻이므로 head 앞에 삽입
            if self.current == self.head:       
                new_node = Node(data)
                new_node.next = self.current 
                self.current.prev = new_node        
                self.head = new_node 
            else:
                # current 앞에 새 노드를 끼워 넣는 과정
                prev_node = self.current.prev       
                new_node = Node(data)
                new_node.prev = prev_node 
                new_node.next = self.current 
                prev_node.next = new_node
                self.current.prev = new_node 
        

    # 커서를 왼쪽으로 한 칸 이동
    def move_left(self): 
        if self.current is not None and self.current is not self.head:    
            self.current = self.current.prev        
      
    # 커서를 오른쪽으로 한 칸 이동 
    def move_right(self):
        if self.current is not None and self.current.next is not None: 
            self.current = self.current.next 

    # 연결 리스트의 모든 문자들을 리스트 형태로 반환  
    def print_nodes_as_list(self):
        res = []
        if self.head is not None: 
            curr = self.head 

            while curr: 
                if curr.data != "":
                    res.append(curr.data)                
                curr = curr.next 
      
        return res 
    
    # 커서 왼쪽 문자 삭제
    def delete_cursor_left(self):
        # current가 존재하고, current가 head가 아닐 때만
        # 즉 current 왼쪽에 실제 삭제할 노드가 있을 때만 수행
        if self.current is not None and self.current is not self.head: 
            prev_node = self.current.prev 

            if prev_node.prev:
                # 노드가 3개 이상일 때
                # prev_node의 이전 노드와 current를 직접 연결
                prev_prev_node = prev_node.prev 
                prev_prev_node.next = self.current 
                self.current.prev = prev_prev_node
            else:
                # 노드가 2개일 때
                # 삭제 대상(prev_node)이 head이므로
                # current를 새로운 head로 변경
                self.head = self.current 
                self.current.prev = None

li = LinkedList()
input_data = input().rstrip()

for c in input_data: 
    li.append(c)
li.append("")

m = int(input())

for _ in range(m):
    commands = input().split()
    command = commands[0]

    if command == "P":   
        li.cursor_append(commands[1])
    elif command == "L":     
        li.move_left()
    elif command == "D":
        li.move_right()
    elif command == "B":
        li.delete_cursor_left()



print("".join(li.print_nodes_as_list()))

