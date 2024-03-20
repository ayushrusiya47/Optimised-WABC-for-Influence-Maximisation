import random

def monteCarloSimulation(gIn,gOut,seeds,num_simulations):
    # calculating weights
    weights = {}
    for i in range(len(gOut)):
        for j in gOut[i]:
            weights[(i,j)] = 1/len(gIn[j])
    
    avg=0
    for _ in range(num_simulations):
        # Trimming edges with probability (1-p(i,j)) to reduce time complexity
        gOutCopy = [set() for i in range(len(gOut))]
        for i in range(len(gOut)):
            for j in gOut[i]:
                if random.random() < weights[(i,j)]:
                    gOutCopy[i].add(j)
        activated_temp=seeds
        total_activated=activated_temp
        gain=len(activated_temp)
        while(gain>0):
            new=set()
            for i in activated_temp:
                for j in gOut[i]:
                    if j not in total_activated and random.random() < weights[(i,j)]:
                        new.add(j)
            gain=len(new)
            activated_temp=new
            total_activated=total_activated.union(activated_temp)
        avg+=len(total_activated)
        
    avg=avg/num_simulations
    return avg
