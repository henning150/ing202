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
