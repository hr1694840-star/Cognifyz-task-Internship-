# Celsius to Fahrenheit and Fahrenheit to Celsius
print("Temperature Converter")

# Ask temperature from user
temperature = float(input("Enter temperature value: "))

# Enter C for Celsius and F for Fahrenheit
unit = input("Enter unit (C for Celsius / F for Fahrenheit): ")

if unit == "C" or unit == "c":
    result = (temperature * 9/5) + 32
    print("Temperature in Fahrenheit is:", result)

elif unit == "F" or unit == "f":
    result = (temperature - 32) * 5/9
    print("Temperature in Celsius is:", result)

else:
    print("Sorry! You entered wrong unit.")