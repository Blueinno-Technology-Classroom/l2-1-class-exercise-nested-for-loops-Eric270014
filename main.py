##################################################
'''
Q1: 
for row in range(7):
    for col in range(row):
        print(col, end=' ')
    print('', end=newLine)
'''

# TODO: Write your code here

##################################################
'''
Q2:

for row in range(1, 7, 1):
    for col in range(1, row+1):
        print(col, end=' ')
    print()

'''

# TODO: Write your code here

##################################################
'''
Q3:
for row in range(9, 0, -1):
    for col in range(5):
        print(row, end= '')


'''


# TODO: Write your code here

##################################################
'''
Q4:
for row in range(9, 0, -1):
    print(str(row)*row, end='')

'''




# TODO: Write your code here

##################################################
'''
Q5:
print()
print('Q5')

maximum = 10
for i in range(1, 10, 2):
    dashes = f'-' * int(maximum/2)
    nums = f'{i}' * i
    print(dashes + nums)
    maximum -= 2

'''



# TODO: Write your code here

##################################################
'''
Q6:

print()
print('Q6')
for i in range(1, 5):

# 1. loop of empty spaces (for (5 - i) times)
    for j in range(5 - i, 0, -1):
        print(' ', end='')

#2. loop of ascendning numbers 
    for j in range (1, i+1):
        print(j, end='')
#3. loop of decending numbers
    for j in range(i - 1, 0, -1):
        print(j, end='')
    print()
'''

# TODO: Write your code here

##################################################
