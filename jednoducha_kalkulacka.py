prvnicislo = int(input("Zadejte první číslo"))
druhecislo = int(input("Zadejte druhé číslo"))
operace = input("Zadejte druh operace")

if (operace == "*"):
    print("Výsledek je" , prvnicislo * druhecislo)

elif (operace == "/"):
    print("Výsledek je" , prvnicislo / druhecislo)

elif (operace == "-"):
    print("Výsledek je" , prvnicislo - druhecislo)

elif (operace == "+"):
    print("Výsledek je" , prvnicislo + druhecislo)

else: 
    print("Neznámý druh operace...")
