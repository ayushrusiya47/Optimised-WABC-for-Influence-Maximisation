from collections import deque

def evalFitness(g,d,seeds):
    fitness = {x: 0 for x in seeds}
    dOutNbr={x:[] for x in seeds}
    
    #storing frequencies to optimize queries  
    nbrFreq={}
    
    for seed in seeds:
        # performing bfs on each seed to get the d-out neibhours
        visited = [False for i in range(len(g))]
        q=deque()
        q.append((seed,0))
        visited[seed]=True
        while(len(q)>0):
            curr=q.popleft()
            if curr[1]==d:
                continue
            for i in g[curr[0]]:
                if not visited[i]:
                    visited[i]=True
                    q.append((i,curr[1]+1))
        
        for i in range(len(visited)):
            if visited[i]:
                dOutNbr[seed].append(i)
                if i not in nbrFreq:
                    nbrFreq[i]=[seed]
                else:
                    nbrFreq[i].append(seed)
                
    for seed in seeds:
        for nbr in dOutNbr[seed]:
            if seed==min(nbrFreq[nbr]):
                fitness[seed]+=1
    
    return fitness