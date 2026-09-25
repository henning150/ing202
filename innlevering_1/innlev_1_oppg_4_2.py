x = ""
numOrd = 0
numTegn = 0
while (True):
    if len(x)>25:
        print(f"setningen er : {x}.")
        print(f"Setningen består av {numOrd} ord og {numTegn} bokstaver")
        break
    print(f"{numOrd+1}. ord?")
    neste = input()
    if numOrd == 0:
        x = neste
        numTegn = len(neste)
    else:
        x += " " + neste
        numTegn += len(neste)
    numOrd += 1


#Output:
# 1. ord?
# hei   
# 2. ord?
# på
# 3. ord?
# deg
# 4. ord?
# din 
# 5. ord?
# gamle 
# 6. ord?
# sjokolade
# setningen er : hei på deg din gamle sjokolade.
# Setningen består av 6 ord og 25 bokstaver