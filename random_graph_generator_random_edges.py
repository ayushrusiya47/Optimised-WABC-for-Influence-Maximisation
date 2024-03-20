import random

# number of nodes
n=75000
m=2000000

g=[set() for i in range(n)]
count=0
while count<m:
    i=random.randint(0,n-1)
    j=random.randint(0,n-1)
    if i!=j and j not in g[i]:
        g[i].add(j)
        count+=1

with open('random_graph_input75000.txt', 'w') as f:
    for i in range(n):
        for j in g[i]:
            f.write(str(j) + ' ')
        f.write('\n')
    f.close()
