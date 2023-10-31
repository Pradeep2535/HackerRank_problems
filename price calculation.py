'''Task

 Raghu is a shoe shop owner. His shop has  number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  Raghu earned.

Input Format

The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.


Output Format

Print the amount of money earned by .
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=list(map(int,input().split()))
n1=int(input())
s=0
for i in range(n1):
    size,price=map(int,input().split())
    if size in l:
        s+=price
        l.remove(size)
print(s)
