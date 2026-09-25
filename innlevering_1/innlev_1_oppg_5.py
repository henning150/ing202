list = []
num = -1
while num != 0:
    print("Skriv inn et positivt tall (eller 0 når du er ferdig):")
    num = int(input())
    if num!=0:
        list.append(num)
print()
print("Hvilket tall vil du dele tallene over på?") 
delPa = int(input())


delelig = []
ikkeDelelig = []

for i in list:
    if i % delPa == 0:

        delelig.append(str(i))
    else:
        ikkeDelelig.append(str(i))

print()
print(f"Delelig på {delPa}:")
print(f"[{", ".join(delelig)}]")
print(f"Ikke delelig på {delPa}:")
print(f"[{", ".join(ikkeDelelig)}]")


#Output:
# Skriv inn et positivt tall (eller 0 når du er ferdig):
# 9
# Skriv inn et positivt tall (eller 0 når du er ferdig):
# 8
# Skriv inn et positivt tall (eller 0 når du er ferdig):
# 27
# Skriv inn et positivt tall (eller 0 når du er ferdig):
# 28
# Skriv inn et positivt tall (eller 0 når du er ferdig):
# 0

# Hvilket tall vil du dele tallene over på?
# 3

# Delelig på 3:
# [9, 27]
# Ikke delelig på 3:
# [8, 28]