zakupy = {"piekarnia": ["chleb", "bułki", "pączek"],
        "warzywniak": ["marchew", "seler", "rukola"]}
for sklep, rzeczy in zakupy.items():
    rzeczy_capitalized=[rzecz.capitalize() for rzecz in rzeczy]
    print(f"Idę do {sklep.capitalize()} i kupuję tam: {rzeczy_capitalized}")
zakupy_piekarnia = zakupy["piekarnia"]
zakupy_warzywniak = zakupy["warzywniak"]
suma = len(zakupy_piekarnia)+len(zakupy_warzywniak)
print(f"W sumie kupuję {suma} produktów")
print("kurs jest trochę chaotyczny")
