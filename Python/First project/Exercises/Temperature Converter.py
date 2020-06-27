print("to convert Celsius to Fahrenheit enter a")
print("to convert Fahrenheit to Celsius enter b")
user_input = input()
if user_input == "a":
    if isinstance(user_input, str):
        temperature = input("Enter the temperature")
        result = ((float(temperature)*9/5)+32)
        print(result)
elif user_input == "b":
    if isinstance(user_input, str):
        temperature = input('Enter the temperature')
        result = ((float(temperature)-32)*5/9)
        print(result)

#---------------------
print("to convert Celsius to Fahrenheit enter a")
print("to convert Fahrenheit to Celsius enter b")
user_input = input()
if user_input == "a":
    if isinstance(user_input, str):
        temperature = input("Enter the temperature")
        result = ((float(temperature)*9/5)+32)
        print(result)
elif user_input == "b":
    if isinstance(user_input, str):
        temperature = input('Enter the temperature')
        result = ((float(temperature)-32)*5/9)
        print(result)

#----------------------
print("to convert Celsius to Fahrenheit enter a")
print("to convert Fahrenheit to Celsius enter b")
print("to convert Celsius to Kelvin enter c")
user_input = input()
if user_input == "a":
    temperature = float(input("Enter the base temperature: "))
    result = (temperature*9/5)+32
elif user_input == "b":
    temperature = float(input("Enter the base temperature: "))
    result = (temperature-32)*5/9
elif user_input == "c":
    temperature = float(input("Enter the base temperature: "))
    result = (temperature+273)
print(result)

#Emerson Mellado:spiral_calendar_pad:  9 minutes ago
#One more solution with functions:
print("to convert Celsius to Fahrenheit enter a")
print("to convert Fahrenheit to Celsius enter b")
print("to convert Celsius to Kelvin enter c")
user_input = input()


def celsius_to_fahrenheit(temp):
    return (temp*9/5)+32


def fahrenheit_to_celsius(t):
    return (t-32)*5/9


def celsius_to_kelvin(x):
    return x+273


if user_input == "a":
    temperature = float(input("Enter the base temperature: "))
    result = celsius_to_fahrenheit(temperature)
elif user_input == "b":
    temperature = float(input("Enter the base temperature: "))
    result = fahrenheit_to_celsius(temperature)
elif user_input == "c":
    temperature = float(input("Enter the base temperature: "))
    result = celsius_to_kelvin(temperature)
print(result)