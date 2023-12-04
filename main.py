from forex_python.converter import CurrencyRates
import sys
liste_devises = ['USD', 'EUR', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF', 'ISK', 'NOK', 'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'INR', 'KRW', 'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB', 'ZAR']
print("Devises accessibles:", liste_devises)


historique_operations = []
     


while True:

    convertisseur = CurrencyRates()

    montant = float(input("Combien souhaitez-vous echanger: "))
    devise = input("Quelle est la devise de votre montant: ")
    change = input("Quelle devise souhaitez-vous obtenir: ")

    if devise not in liste_devises or change not in liste_devises:
        print("Devises non disponibles.")
        sys.exit()

    echange = convertisseur.get_rate(devise, change)
    obtention = montant * echange
    obtention = round(obtention, 2)
    new_obtention = f"{montant} {devise} = {obtention} {change}"

    print("Vous obtiendrez", obtention, change)

    affichage = input("Voulez-vous archiver votre conversion? (OUI/NON/EFF): ")

    if affichage == "OUI":
        historique_operations.append(new_obtention)
        print("Conversion archivé.")
    elif affichage == "NON":
        pass
    elif affichage == "EFF":
        historique_operations.clear()
        print("Historique effacée.")
    else:
        print("Veuillez entrer OUI/NON/EFF.")           
    continuer = input("Voulez-vous continuer? (OUI/NON): ")
    if continuer != "OUI":
        print("Bonne journée")
        break
    
print("Archives conversion", historique_operations)
