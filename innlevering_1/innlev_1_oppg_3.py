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
 
print(log(0))