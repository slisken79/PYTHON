# Skapa och skriv till en fil
with open("./exempelfil.txt", "w") as fil:
    fil.write("Detta är en exempelfil.\nExtra text 2.")

# Läsa från en fil
with open("./exempelfil.txt", "r") as fil:
    innehåll = fil.read()
    print("Filinnehåll:", innehåll)
 
