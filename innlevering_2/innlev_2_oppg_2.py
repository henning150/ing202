
#1
def telefonnummer(tekst:str):
    tekst = tekst.replace("-", "")
    tekst = tekst.replace(" ", "")
    tekst = tekst.replace("+47", "")
    if tekst.startswith("0047"):
        tekst = tekst[4:]
    return int(tekst)

print(telefonnummer("0047-124 53233 214"))

#2
smaord = ["og", "eller", "med", "hos", "på", "i"]
def sentence_case(tekst:str):
    tekst = tekst.lower().capitalize()
    return tekst

def title_case(tekst:str):
    tekst = tekst.lower()
    result = []
    words = tekst.split(" ")
    for w in words:
        if not smaord.__contains__(w):
            result.append(w.capitalize())
        else:
            result.append(w)

    return " ".join(result)

print(title_case("hei på deg"))