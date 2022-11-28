from datetime import date
from nsepy import get_history

scriptSymbol = input("Insert the symbol of script: ")

a= int(input("Enter start date in YYYY: "))
b= int(input("Enter start date in MM: "))
c= int(input("Enter start date in DD: "))

x= int(input("Enter end date in YYYY: "))
y= int(input("Enter end date in MM: "))
z= int(input("Enter end date in DD: "))


script = get_history(symbol=scriptSymbol,
                   start=date(a,b,c),
                   end=date(x,y,z))
print(script)