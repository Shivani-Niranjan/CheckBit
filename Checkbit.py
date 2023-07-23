'''
You are given two integers A and B.
Return 1 if B-th bit in A is set
Return 0 if B-th bit in A is unset

Input
A = 4
B = 1

Output
0

Input
A = 5
B = 2

Output
1
'''
number = int(input())
checkbit = int(input())

if (number == (number | (1 << checkbit))):
    print (1)
else:
    print (0)