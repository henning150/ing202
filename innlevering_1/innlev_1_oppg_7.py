def beregn_vout(V_in:float, R1:int, R2:int):
    if (R1+R2) == 0:
        return "inf"
    return V_in * (R2/(R1+R2))

print("Vennligst skriv inn inngangsspenningen (V_in): ")
vin = float(input())
print("Vennligst skriv inn motstanden R1 (ohm: ")
r1 = int(input())
print("Vennligst skriv inn motstanden R2 (ohm: ")
r2 = int(input())
print("Utspenningen (V_out) er: ")
print(f"{beregn_vout(vin, r1, r2)} V")


#Output:
# Vennligst skriv inn inngangsspenningen (V_in): 
# 12
# Vennligst skriv inn motstanden R1 (ohm: 
# 200
# Vennligst skriv inn motstanden R2 (ohm: 
# 300
# Utspenningen (V_out) er: 
# 7.199999999999999 V