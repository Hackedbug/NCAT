#This is a currency converter program converting USD to different currencies
rate_from_USD = { # dictionary containing exchange rates from different currencies to USD
    'USD': 1.0,
    'EUR': 0.85,
    'JPY': 110.0,
    'GBP': 0.75,
    'AUD': 1.35,
    'CAD': 1.25,
    'CHF': 0.92,
    'CNY': 6.5,
    'INR': 73.0,
    'NGN': 1600.0,
}

amount = float(input("Enter the amount to be converted: ")) # the quantity of USD to be converted to other currencies
from_currency = input("Enter the currency you're converting from: ").upper() #the currency to be converted
to_currency = input("Enter the currency you're converting to: ").upper() #the currency to convert to

if to_currency and from_currency in rate_from_USD: #if statement to check if both values are among the dictionaries before executing
    if to_currency == "EUR":
        print (amount / rate_from_USD.get(to_currency))
    elif to_currency == 'JPY':
        print (amount * rate_from_USD.get(to_currency))
    elif to_currency == 'GBP':
        print (amount / rate_from_USD.get(to_currency))
    elif to_currency == 'AUD':
        print (amount * rate_from_USD.get(to_currency))
    elif to_currency == 'CAD':
        print (amount * rate_from_USD.get(to_currency))
    elif to_currency == 'CHF':
        print (amount / rate_from_USD.get(to_currency))
    elif to_currency == 'CNY':
        print (amount * rate_from_USD.get(to_currency))
    elif to_currency == 'INR':
        print (amount * rate_from_USD.get(to_currency))
    else:
        print (amount * rate_from_USD.get(to_currency))
else: #the statement if the to currency is not among the dictionary
    print(to_currency + " is not a valid currency in the world.")