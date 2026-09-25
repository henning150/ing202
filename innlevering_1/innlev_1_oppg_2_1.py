print("Skriv tall:")
num = int(input());
if num==0:
    print(f"{num} er ikke oddetall eller partall");
elif (num % 2)>0:
    print(f"{num} er oddetall");
else:
    print(f"{num} er partall");

#Output:
# Skriv tall:
# 13
# 13 er oddetall

# Skriv tall:
# 20
# 20 er partall