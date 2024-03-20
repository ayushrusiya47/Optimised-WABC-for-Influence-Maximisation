import time
import matplotlib.pyplot as plt
from tqdm import tqdm

from WABC_Main import WABC_Main
from ABC_Main import ABC_Main
from monte_carlo_simulation import monteCarloSimulation

# Initializing in-neighbour graph
gOut = []
with open("random_graph_input2000.txt") as f:
    for line in f:
        gOut.append([int(x) for x in line.split()])
        
# Initializing out-neighbour graph
gIn = [[] for i in range(len(gOut))]
for i in range(len(gOut)):
    for j in gOut[i]:
        gIn[j].append(i)

# Parameter sensitive analysis        
theta_test_values=[i/100 for i in range(1,51)]
evaluated_spread=[]
estimated_spread=[]
time_taken=[]
for theta in tqdm(theta_test_values,desc="Loading…"):
    start=time.time()
    seeds, fitness = WABC_Main(gOut,gIn,theta,10)
    end=time.time()
    time_taken.append(end-start)
    evaluated_spread.append(fitness)
    estimated_spread.append(monteCarloSimulation(gIn,gOut,seeds,10000))
    
error_rel=[abs(evaluated_spread[i]-estimated_spread[i])/estimated_spread[i] for i in range(50)]

max_time=max(time_taken)
time_rel=[i/max_time for i in time_taken]

max_spread=max(estimated_spread)
coverage_rel=[(1-i/max_spread) for i in estimated_spread]

score_function=[error_rel[i]+time_rel[i]+coverage_rel[i] for i in range(50)]

plt.plot(theta_test_values,error_rel,label="error_rel")
plt.plot(theta_test_values,time_rel,label="time_rel")
plt.plot(theta_test_values,coverage_rel,label="coverage_rel")
plt.plot(theta_test_values,score_function,label="score_fun")

plt.xlabel("theta")
plt.ylabel("value")
plt.legend()

plt.show()

optimal_theta=theta_test_values[score_function.index(min(score_function))]
print("optimal theta is",optimal_theta)

WABC_time_taken=[]
WABC_evaluated_spread=[]   
WABC_estimated_spread=[]
WABC_relative_error=[]
ABC_time_taken=[]
ABC_evaluated_spread=[]   
ABC_estimated_spread=[]
ABC_relative_error=[]


for num_of_seeds in tqdm(range(5,26,5),desc="Loading…"):
    WABC_start=time.time()
    seeds, fitness = WABC_Main(gOut,gIn,optimal_theta,num_of_seeds)
    WABC_end=time.time()
    WABC_time_taken.append(WABC_end-WABC_start)
    WABC_evaluated_spread.append(fitness)
    WABC_estimated_spread.append(monteCarloSimulation(gIn,gOut,seeds,10000))
    WABC_relative_error.append(abs(fitness-WABC_estimated_spread[-1])/WABC_estimated_spread[-1])
    
    ABC_start=time.time()
    seeds, fitness = ABC_Main(gOut,gIn,1,num_of_seeds)
    ABC_end=time.time()
    ABC_time_taken.append(ABC_end-ABC_start)
    ABC_evaluated_spread.append(fitness)
    ABC_estimated_spread.append(monteCarloSimulation(gIn,gOut,seeds,10000))
    ABC_relative_error.append(abs(fitness-ABC_estimated_spread[-1])/ABC_estimated_spread[-1])
    
plt.plot(range(5,26,5),WABC_time_taken,label="WABC_time_taken")
plt.plot(range(5,26,5),ABC_time_taken,label="ABC_time_taken")
plt.xlabel("num_of_seeds")
plt.ylabel("time_taken")
plt.legend()
plt.show()

plt.plot(range(5,26,5),WABC_evaluated_spread,label="WABC_evaluated_spread")
plt.plot(range(5,26,5),ABC_evaluated_spread,label="ABC_evaluated_spread")
plt.xlabel("num_of_seeds")
plt.ylabel("evaluated_spread")
plt.legend()
plt.show()

plt.plot(range(5,26,5),WABC_relative_error,label="WABC_relative_error")
plt.plot(range(5,26,5),ABC_relative_error,label="ABC_relative_error")
plt.xlabel("num_of_seeds")
plt.ylabel("relative_error")
plt.legend()
plt.show()
