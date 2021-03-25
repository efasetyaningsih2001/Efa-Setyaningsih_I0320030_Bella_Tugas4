p = 4
q = 11

#bitwise OR
r =p|q
print('\n--------------OR--------------')
print('nilai: ', p, ', Binary: ', format(p, '08b'))
print('nilai: ', q, ', Binary: ', format(q, '08b'))
print('-----------------------------(|)')
print('nilai: ', r, ', Binary: ', format(r, '08b'))

#bitwise right shift
r = p >> q
print('\n---------RIGHT SHIFT-----------')
print('nilai: ', p, ', Binary: ', format(p, '08b'))
print('nilai: ', q, ', Binary: ', format(q, '08b'))
print('-----------------------------(>>)')
print('nilai: ', r, ', Binary: ', format(r, '08b'))

#bitwise XOR
r = p ^ q
print('\n--------------XOR-------------')
print('nilai: ', p, ', Binary: ', format(p, '08b'))
print('nilai: ', q, ', Binary: ', format(q, '08b'))
print('------------------------------(^)')
print('nilai: ', r, ', Binary: ', format(r, '08b'))

#bitwise NOT
r = ~p
print('\n--------------NOT-------------')
print('nilai: ', p, ', Binary: ', format(p, '08b'))
print('nilai: ', q, ', Binary: ', format(q, '08b'))
print('-----------------------------(~)')
print('nilai: ', r, ', Binary: ', format(r, '08b'))

#bitwise AND
r = p & q
print('\n--------------AND-------------')
print('nilai: ', p, ', Binary: ', format(p, '08b'))
print('nilai: ', q, ', Binary: ', format(q, '08b'))
print('------------------------------(&)')
print('nilai: ', r, ', Binary: ', format(r, '08b'))
