import ABC_Evaluation_Function

# Function to calculate minimum fitness and its seed
def minFitness(fitness):
    min_fitness = min(fitness.values())
    for i in fitness:
        if fitness[i] == min_fitness:
            min_fitness_seed = i
    return (min_fitness,min_fitness_seed)

def ABC_Main(gOut,gIn,d,numOfSeeds):
    # Calculating Ranks
    # TODO: Calculating ranks in a better way to avoid local maximas
    # maybe use fitness function with seed as all vertices
    ranks = [(len(gOut[i]),i) for i in range(len(gOut))]
    ranks.sort()
    ranks = [ranks[i][1] for i in range(len(ranks))]
    
    # Initializing additional parameters
    omega = 0.02 # termination criterion is gain less than 2% 

    # Initializing seeds
    seeds = set(ranks[:numOfSeeds])
    
    fitness = ABC_Evaluation_Function.evalFitness(gOut,d,seeds)
    curr_fitness = sum(fitness.values())

    min_fitness, min_fitness_seed = minFitness(fitness)
    
    while(True):
        scouts = set() # consider taking scouts according to rank
        for i in seeds:
            for j in gOut[i]:
                if j not in seeds:
                    scouts.add(j)
                    
        while(len(scouts) > 0):
            test_scout= scouts.pop()
            seeds.add(test_scout) # consider taking union with all scouts together
            new_fitness = ABC_Evaluation_Function.evalFitness(gOut,d,seeds)
            
            if new_fitness[test_scout]>min_fitness:
                seeds.remove(min_fitness_seed) # consider making a blacklist containing removed seeds
                del new_fitness[min_fitness_seed]
                min_fitness, min_fitness_seed = minFitness(new_fitness)
                continue
            else:
                seeds.remove(test_scout)
        new_fitness = ABC_Evaluation_Function.evalFitness(gOut,d,seeds)
        new_curr_fitness = sum(new_fitness.values())
        
        if new_curr_fitness - curr_fitness < omega*curr_fitness:
            break
        else:
            fitness = new_fitness
            curr_fitness = new_curr_fitness
    
    return (seeds,curr_fitness)