# Skapa en ordlista
person = {
    "namn": "Youness",
    "ålder": 44,
    "yrke": "IT Konsult"
}

# Åtkomst till värden
print("-Namn:", person["namn"])
print("-Ålder:", person["ålder"])
print("-Yrke:", person["yrke"])
print("-------------")
# Iterera över nycklar och värden
for nyckel, värde in person.items():
    print(nyckel + ":", värde)
