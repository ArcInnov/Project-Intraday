# Takes user input of  adn 

from datetime import date
from nsepy import get_history

scriptSymbol = input("Insert the symbol of script: ")

a= int(input("Enter start date in YYYY"))
b= int(input("Enter start date in MM"))
c= int(input("Enter start date in DD"))


# endDate = input("Enter end date in YYYY-MM-DD format")
print(a,b,c)

script = get_history(symbol=scriptSymbol,
                   start=date(a,b,c),
                   end=date(2015,1,10))
print(script)