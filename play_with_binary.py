# The number starts from 1
# Add 0 at the front and 1 after it.
result_list = ['1']
# Change the number inside range to reach for more numbers
for i in range(20):
    for number in reversed(range(0,len(result_list))):
        if number % 2 == 0:
            result_list.insert(number, '0')
        else:
            result_list.insert(number, '1')
    if result_list[-2] == 1:
        result_list.append('0')
    else:
        result_list.append('1')
    print(''.join(result_list))