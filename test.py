heltal = int(input("Fyll i ett heltal: "))
print(heltal)
andra_heltal = int(input("Fyll i ett till heltal: "))
print(heltal + andra_heltal)

pris_jacka = 2000
#rea_procent = 75.0

rea_procent = float(input("Skriv in procentsats: "))

rea = pris_jacka * rea_procent / 100
slut_pris = pris_jacka - rea
print(slut_pris)
