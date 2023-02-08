def dot(A,B):
    A , B , res = list(A) , list(B) , 0
    for (x , y) in zip(A,B):
        res += (x * y)
    return res

n = int(input('Enter size of the sets: '))
A , B = set({}) , set({})

print('Enter values for Set 1: ')
for x in range(n):
    A.add(int(input('Enter integer element: ')))

print('\nEnter values for Set 2: ')
for x in range(n):
    B.add(int(input('Enter integer element: ')))

print(f'\nEntered Set 1: {A}')
print(f'Entered Set 2: {B}')

jacSim = len( A.intersection(B) ) / len( A.union(B) )
coSim = dot(A,B) / ( (dot(A,A) ** 0.5) * (dot(B,B) ** 0.5)) 


print(f'a. Jaccard Similarity: {jacSim}')
print(f'b. Cosine Similarity: {coSim}')