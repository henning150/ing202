import math
def calc(n):
    return (-1) * math.pow(10, 6) + math.pow(10,4)*n - (math.pow(n, 4)/math.pow(10,10))

best = -9999999999
bestIndex = -1
for i in range(60000):
    profit = calc(i)
    if best<profit:
        bestIndex = i
        best = profit

print(best)
#best : 218301330.349824
print(bestIndex)
#bestindex : 29240