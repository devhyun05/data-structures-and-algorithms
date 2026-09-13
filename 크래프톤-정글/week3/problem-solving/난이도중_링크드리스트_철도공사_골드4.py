# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309

class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Linkedlist:
    def __init__(self):
        self.head=None
        self.current=None

    def append_node(self,data):
        if self.head is None:
            self.head = Node(data)
            self.current = self.head
        else:
            new_node = Node(data)
            self.current.next = new_node
            new_node.prev = self.current
            self.current = self.current.next

    def last_to_head(self):
        self.current.next=self.head
        self.head.prev=self.current

    def bn(self,curr_station,new_station):
        current_1 = self.head
        while current_1.data != curr_station:
            current_1 = current_1.next
        current_2 = current_1.next
        print(current_2.data)

        new_node=Node(new_station)
        current_1.next=new_node
        new_node.prev=current_1
        new_node.next=current_2
        current_2.prev=new_node

    def bp(self,curr_station,new_station):
        current_1 = self.head
        while current_1.data != curr_station:
            current_1 = current_1.next
        current_2 = current_1.prev
        print(current_2.data)

        new_node = Node(new_station)
        current_1.prev = new_node
        new_node.next=current_1
        new_node.prev = current_2
        current_2.next=new_node

    def cn(self,curr_station):
        current_1=self.head
        while current_1.data!=curr_station:
            current_1=current_1.next
        current_2=current_1.next
        print(current_2.data)
        current_3=current_2.next
        current_1.next=current_3
        current_3.prev=current_1
        current_2.next=None
        current_2.prev=None

    def cp(self,curr_station):
        current_1=self.head
        while current_1.data!=curr_station:
            current_1=current_1.next
        current_2=current_1.prev
        print(current_2.data)
        current_3=current_2.prev
        current_1.prev=current_3
        current_3.next=current_1
        current_2.next=None
        current_2.prev=None

li = Linkedlist()
a,b = map(int,input().split())
station_num=list(map(int,input().split()))

for i in range(len(station_num)):
    li.append_node(station_num[i])
li.last_to_head()

for _ in range(b):
    command=list(input().split())
    cmd=command[0]
    curr_station=int(command[1])

    if cmd=="BN":
        new_station=int(command[2])
        li.bn(curr_station,new_station)
    elif cmd=="BP":
        new_station=int(command[2])
        li.bp(curr_station,new_station)

    elif cmd=="CN":
        li.cn(curr_station)
    elif cmd=="CP":
        li.cp(curr_station)