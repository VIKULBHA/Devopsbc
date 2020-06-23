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