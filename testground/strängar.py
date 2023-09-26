#Konkatenera stränga
förnamn = "Elsa"
efternamn = "Godman"
fullnamn = förnamn + " "+ efternamn
print("Fullnamnet är: " + fullnamn)

# Indexera bokstav
print("Första bokstav i förnamnet är: " + förnamn[0]+ " och sista är: "+ förnamn[-1])

# Trimma strängar
text = "   Detta  är en  text  !"
trimmad_text = text.split()
print("Trimmade texten är: ", trimmad_text)

# Ta bort mellanslag i början och slutet
text = "    Detta är en text.    "
trimmad_text = text.strip() 
print("Trimmad text:", trimmad_text)