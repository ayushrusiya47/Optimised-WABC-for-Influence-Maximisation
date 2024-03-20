import WABC_Main
import time
import matplotlib.pyplot as plt

# Initializing in-neighbour graph
gOut = []
with open("random_graph_input75000.txt") as f:
    for line in f:
        gOut.append([int(x) for x in line.split()])
        
# Initializing out-neighbour graph
gIn = [[] for i in range(len(gOut))]
for i in range(len(gOut)):
    for j in gOut[i]:
        gIn[j].append(i)
print("saved")
        
time_taken=[]
for seed in range(5,26,5):
    start=time.time()
    seeds, fitness = WABC_Main.WABC_Main(gOut,gIn,0.0009,seed)
    end=time.time()
    print(seeds,fitness,end-start)
    time_taken.append(end-start)

plt.plot(range(5,26,5),time_taken)
plt.xlabel("number of seeds")
plt.ylabel("time taken")
plt.show()
