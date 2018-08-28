## FILE HANDLING
# Question 1
f = open('abcd.txt','r')
l = f.readlines()
for i in l:
    print(i)
f.close()

# Question 2
from collections import Counter
with open('abcd.txt','r') as f:
    a = Counter(f.read().split())
    print(a)

# Question 3
with open('abcd.txt','r') as f:
    with open('new.txt','w') as g:
        for l in f:
            g.write(l)

# Question 4
with open('abcd.txt') as f:
    with open('new.txt') as g:
        for l1,l2 in zip(f,g):
            print(l1+l2)

# Question 5
file = open("ab.txt")
column = []
for line in file:
    column.append(int(line))
column.sort()
print(column)
file.close()
