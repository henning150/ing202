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