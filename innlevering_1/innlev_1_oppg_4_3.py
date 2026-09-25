tekst = "Dette er en liten tekst. Den inneholder en liten test. Ikke værst."
l = tekst.split(".")
l.pop() #removing last item after last .
for s in l:
    print(f"{s.lstrip()}.")

# Dette er en liten tekst.
# Den inneholder en liten test.
# Ikke værst.