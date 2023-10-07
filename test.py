def check( gas, cost, k):
        i, tank = k, 0
        tank +=  gas[i] - cost[i]
        while True:
            if i == (len(gas) - 1): i = 0
            else: i += 1
            if i == k: 
                return 1
            if tank < gas[i]:
                return -1 
            tank +=  gas[i] - cost[i]

def canCompleteCircuit(gas, cost) -> int:
    for i in range(len(gas)):
        if gas[i] > cost[i]:
            if check(gas,cost,i) == 1: return i
    return -1

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

print(canCompleteCircuit(gas, cost))