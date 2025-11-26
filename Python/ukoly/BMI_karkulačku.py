
# Vstup od uživatele
#vaha = float(input("Zadej svoji váhu (v kg): "))
#vyska = float(input("Zadej svoji výšku (v metrech): "))

def bmi_kalkulacka(vaha, vyska):
    # Vypocet BMI (v kg na m^2)
    bmi = vaha / (vyska ** 2)
    
    # Určujeme kategorii podle hodnoty BMI
    if bmi < 18.5:
        kategorie = "Podváha"
    elif 18.5 <= bmi < 24.9:
        kategorie = "Normální váha"
    elif 25 <= bmi < 29.9:
        kategorie = "Nadváha"
    else:
        kategorie = "Otylost"
    
    return bmi, kategorie

# Příklad použití
vaha = 70  # v kg
vyska = 1.75  # v metrech

bmi, kategorie = bmi_kalkulacka(vaha, vyska)
print(f"Vaše BMI je {bmi:.2f} a spadáte do kategorie: {kategorie}")
