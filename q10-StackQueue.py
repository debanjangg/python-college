class Stack:
    def __init__(self,len):
        self.len = len
        self.top = 0
        self.S = []
    
    def push(self,ele):
        if self.top == self.len:
            print('Stack overflow.')
        else:
            self.S.append(ele)
            self.top += 1
            
    def pop(self):
        if self.top == 0:
            print('Stack underflow.')
        else:
            self.top -= 1
            return self.S.pop()
    
    def display(self):
        if self.top == 0:
            print('Empty Stack.')
        else:
            print(f'Stack: ',end='')
            for x in range(self.top):
                print(self.S[x],end='  ')
            print()
        
class Queue:
    def __init__(self,len):
        self.len = len
        self.front, self.rear = 0, 0
        self.Q = []
    
    def enQ(self,ele):
        if self.rear == self.len:
            print('Queue full.')
        else:
            self.Q.append(ele)
            self.rear += 1
            print(f'{ele} enqueued.')
            
    def deQ(self):
        if self.front == self.rear:
            print('Queue is empty.')
        else:
            self.front += 1
            return self.Q.pop(0)
    
    def display(self):
        if self.front == self.rear:
            print('Empty Queue.')
        else:
            print(f'Queue: ',end='')
            for x in range(0,self.rear - self.front):
                print(self.Q[x],end='  ')
            print()
            
    
ch1 = int(input('Enter: 1. Stack, 2. Queue. Choose: '))
if ch1 == 1:
    l = int(input('Enter length of the Stack: '))
    S = Stack(l)
    while True:
        print('\nMenu:\n\t1. Push element,\n\t2. Pop element,\n\t3. Display,\n\t4. Exit.')
        ch2 = int(input('Enter choice: '))
        if ch2 == 1:
            S.push(int(input('Enter element to push: ')))
        elif ch2 == 2:
            x = S.pop()
            if x:
                print(f'Element popped: {x}')
        elif ch2 == 3:
            S.display()
        elif ch2 == 4:
            print('Bye')
            break
        else:
            print('Wrong Choice. Try again.')
elif ch1 == 2:
    l = int(input('Enter length of the Queue: '))
    Q = Queue(l)
    while True: 
        print('\nMenu:\n\t1. Enqueue element,\n\t2. Dequeue element,\n\t3. Display,\n\t4. Exit.')
        ch2 = int(input('Enter choice: '))
        if ch2 == 1:
            Q.enQ(int(input('Enter element to enqueue: ')))
        elif ch2 == 2:
            x = Q.deQ()
            if x:
                print(f'Element dequeued: {x}')
        elif ch2 == 3:
            Q.display()
        elif ch2 == 4:
            break
        else:
            print('Wrong Choice. Try again.')
else:
    print('Wrong choice')
