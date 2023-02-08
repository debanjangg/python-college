U = set(range(1,50))
A = set(range(1,20))
B = set(ele for ele in range(4,50,4))

print(f'Set U: {U}')
print(f'Set A: {A}')
print(f'Set B: {B}')

A_comp = U.difference(A)
B_comp = U.difference(B)

print(f'\ni. A\': {A_comp}')
print(f'ii. B\': {B_comp}')
print(f'iii. A intersection B: {A.intersection(B)}')
print(f'iv. A Symmetric Difference B: {A.symmetric_difference(B)}')
print(f'v. A\' Symmetric Difference B\': {A_comp.symmetric_difference(B_comp)}')
print(f'vi. A-B: {A.difference(B)}')
print(f'vii. B-A: {B.difference(A)}')

print(f'viii. Demorgans laws:')
print('\tLaw 1. The complement of the union of two sets is the intersection of their complements.')
LHS = U.difference(A.union(B))
RHS = A_comp.intersection(B_comp)
print(f'\tLHS: {LHS},\n\tRHS: {RHS}')
if(LHS == RHS):
    print('\tDemorgan\'s Law 1 verified.')
else:
    print('\tDemorgan\'s Law 1 not verified.')

print('\n\tLaw 2. The complement of the intersection of two sets is the union of their complements.')
LHS = U.difference(A.intersection(B))
RHS = A_comp.union(B_comp)
print(f'\tLHS: {RHS},\n\tRHS: {RHS}')
if(LHS == RHS):
    print('\tDemorgan\'s Law 1 verified.')
else:
    print('\tDemorgan\'s Law 1 not verified.')

if(U.intersection(A) == A):
    print(f'ix. A is a proper subset of U')
else:
    print(f'ix. A is a proper subset of U')