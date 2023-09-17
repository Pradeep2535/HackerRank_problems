'''
You are given a string .
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.

'''


from itertools import permutations
s,n=map(str,input().split())
s=sorted(list(s))
l=list(permutations(s,int(n)))
for i in l:
    print(''.join(i))
