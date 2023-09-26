# Skapa och skriv till en fil i samma mapp
with open("min.txt", "w") as fil:
    fil.write("Detta är en exempelfil.\nExtra text 3.")

# Läsa från en fil
with open("min.txt", "r") as fil:
    innehåll = fil.read()
    print("Filinnehåll:", innehåll)

 
