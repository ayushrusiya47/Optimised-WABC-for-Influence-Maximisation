import heapq as hq

def evalFitness(g,weights,seed,theta):
    fitness = {x: 0 for x in seed}
    maxProb = {}
    maxProbHeap = []
    for i in seed:
        hq.heappush(maxProbHeap, (1,i,i))
    while(len(maxProbHeap) > 0):
        (prob, node, seed) = hq.heappop(maxProbHeap)
        if prob<theta:
            continue
        if node not in maxProb:
            maxProb[node] = (seed,prob)
            for j in g[node]:
                hq.heappush(maxProbHeap, (prob*weights[(node, j)],j,seed))
        else:
            if prob>maxProb[node][1]:
                maxProb[node] = (seed,prob)
                for j in g[node]:
                    hq.heappush(maxProbHeap, (prob*weights[(node, j)],j,seed))
                        
    for i in maxProb:
        fitness[maxProb[i][0]] += 1
    return fitness