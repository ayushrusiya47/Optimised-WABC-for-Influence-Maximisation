import random

# number of nodes
n=2000

num_influencers = 50
num_populer_users = 250
num_average_users = n-num_influencers-num_populer_users

# edges according to influence level, can change percentage of users for each class
num_influencers_edges = [random.randint(int(0.03*n), int(0.08*n)) for i in range(num_influencers)]
num_populer_users_edges = [random.randint(int(0.01*n), int(0.03*n)) for i in range(num_populer_users)]
num_average_users_edges = [random.randint(1, int(0.01*n)) for i in range(num_average_users)]

combined_edges = num_influencers_edges + num_populer_users_edges + num_average_users_edges

# number of edges
m = sum(num_influencers_edges) + sum(num_populer_users_edges) + sum(num_average_users_edges)

graph = []

# adding all edges
for i in range(n):
    other_users=set(range(n))
    other_users.remove(i)
    graph.append(list(random.sample(sorted(other_users), combined_edges[i])))
    
# storing the graph in an input file
with open('random_graph_input2000.txt', 'w') as f:
    # f.write(str(n) + ' ' + str(m) + '\n')
    for i in range(n):
        for j in range(len(graph[i])):
            f.write(str(graph[i][j]) + ' ')
        f.write('\n')
    f.close()