# weight conversion

unit = input("Is the temp in Celcius or Farenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 2)
    print(f"The temperature in Farenheit is: {temp}F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 2)
    print(f"The temperature in Celcius is: {temp}C")
else:
    print(f"{unit} an invalid unit of temperature!")