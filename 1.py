
import sys

def calc_fd_closure(name, fd_sets, excepted_fd_sets=[]):
    avaiable_fd_sets = list(set(fd_sets).symmetric_difference(set(excepted_fd_sets)))
    func_closure = list(name)
 
    for i in range(0, len(avaiable_fd_sets)):
        for fd_set in avaiable_fd_sets:
            [left, right] = fd_set.split('->')
            if (set(list(left)).issubset(func_closure) or left in func_closure) and (set(list(right)).issubset(func_closure) == False or right not in func_closure):
                func_closure.extend(right.split())
    return ''.join(func_closure)

print('Nhập phụ thuộc hàm. Ví dụ: AB->C,D->E')
fd_sets_raw = input()

# fd_sets_raw = 'AB->CE,CD->E,ABC->EFG' # AB->C,CD->E,AB->E,AB->F,AB->G
# fd_sets_raw = 'AB->C,AC->D,D->EG,G->B,A->D,CG->A' # D->E,D->G,G->B,A->D,A->C,G->A
# fd_sets_raw = 'A->BG,D->EG,GB->HA,D->BA,B->HG' # D->E,D->A,B->G,B->H,B->A
# fd_sets_raw = 'B->CG,DEG->B,A->DC,A->E,A->G' # B->C,B->G,DE->B,A->D,A->E,A->G
# fd_sets_raw = 'E->C,H->E,A->D,AE->H,DG->B,DG->C'

fd_sets = fd_sets_raw.split(',')

# Step 1
step_1_fd_sets = []
for fd_set in fd_sets:
    [left, right] = fd_set.split('->')
    if len(right) > 1:
        for char in right:
            step_1_fd_sets.append(f'{left}->{char}')
    else:
        step_1_fd_sets.append(f'{left}->{right}')

# Step 2
step_2_fd_sets = step_1_fd_sets
for fd_set in step_2_fd_sets:
    [left, right] = fd_set.split('->')
    fd_closure = calc_fd_closure(left, step_2_fd_sets, excepted_fd_sets=[fd_set])
    if set(list(right)).issubset(list(fd_closure)) or right in fd_closure:
        step_2_fd_sets.remove(fd_set)

# Step 3
step_3_fd_sets = list(step_2_fd_sets)
for fd_set in step_2_fd_sets:
    [left, right] = fd_set.split('->')
    redundant_count = 0

    if len(left) == 1:
        continue
    
    is_redundant = False
    for char in left:
        new_left = left.replace(char, '')
        fd_closure = calc_fd_closure(new_left, [f'{new_left}->{right}', *step_3_fd_sets], excepted_fd_sets=[fd_set])
        if char in fd_closure:
            step_3_fd_sets.remove(fd_set)
            step_3_fd_sets.append(f'{new_left}->{right}')
            redundant_count += 1
        
            if redundant_count == len(left) - 1:
                break

print()
print(', '.join(step_3_fd_sets))