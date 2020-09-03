# Author: Augustus Perseghin
# Collaborator: ZiHao Xu
# Collaborator: Chenyin Zhang
# The purpose of this program is to recieve a temperature (with unit) # and convert it into the other unit type (Fehrenheit or Celsius)
tempIn = float(input("Enter temperature: "))
tempInType = input("Enter unit in F/f or C/c: ")
tempOut = 0
if tempInType == 'c' or tempInType == 'C':
  tempOut = tempIn * 9/5 + 32
  print(f"{tempIn}° in Celsius is equivalent to {tempOut}° Fahrenheit.")
elif tempInType == 'f' or tempInType == 'F':
  tempOut = (tempIn - 32) * 5/9
  print(f"{tempIn}° in Fahrenheit is equivalent to {tempOut}° Celsius.")
else:
  print(f"Invalid unit({tempInType}).")



  
