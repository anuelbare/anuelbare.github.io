def currency_converter():
    usd_to_eur = 0.85  # Example conversion rate

    print("Currency Converter: USD to EUR")
    usd_amount = float(input("Enter the amount in USD: "))
    eur_amount = usd_amount * usd_to_eur

    print(f"{usd_amount} USD is {eur_amount:.2f} EUR")

currency_converter()
