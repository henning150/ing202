import math


vann = 1000.0
tid = 0
while vann>1.0:
    q=0.94*math.pow(vann, 0.167)
    vann -= q
    tid += 1
    print(f"{tid} : {vann}")

#402