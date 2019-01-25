base = (" ", "- ", "- e ", " e ")
a, first_dial, cur_elem_to_base = input(), False, ''
for elem_ind in range(len(a)):
    if a[elem_ind] <= '9' and a[elem_ind] >= '0':
        if not first_dial:
            cur_elem_to_base += ' '
            first_dial = True
    else:
        cur_elem_to_base += a[elem_ind]
        first_dial = False

if cur_elem_to_base in base:
    '''Это число'''
