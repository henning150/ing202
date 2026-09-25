#del 1
def delelig(n, m):
    result:float = n/m;
    return result==1

#del 2
def sist(num):
    numStr = str(num);
    return numStr[len(numStr)-1];

#del 3
def log(num):
    if (num>=10):
        return 1+log(num/10);
    else:
        return 0;


print("delelig (10, 5):")
print(delelig(10, 5))
print("delelig (9, 5):")
print(delelig(9, 5))

print("sist (12345):")
print(sist(12345))

print("log (365)")
print(log(365))

print("log (0)")
print(log(0))


#Output:
# delelig (10, 5):
# False
# delelig (9, 5):
# False
# sist (12345):
# 5
# log (365)
# 2
# log (0)
# 0