# # This function will count the body mass
# def bodyMassIndex(weight,height):
#     bmi=(weight*703)/(height*height)
#     print(f'User BMI = {bmi:.2f}')
#     if bmi < 18.5:
#         printBmi=(f'User with weight {weight} pound and height {height} inches is underweight')
#     elif bmi <=24.9:
#         printBmi=(f'User with weight {weight} pound and {height} height has normal weight')
#     elif bmi <=29.9:
#         printBmi=(f'User with weight {weight} pound and {height} height is overerweight')
#     else:
#         printBmi=(f'User with weight {weight} pound
#         and {height} height is considered in obese category')
#     return printBmi
# # get data from user
# invalidInput=True
# while invalidInput:
#     try:
#         user_weight=float(input("Please enter your Weight in Pounds "))
#         user_height = float(input("Please enter your Height in Inches "))
#     except:
#         print("Please enter your data in right format")
#         continue
#     # call function bodyMassIndex if data from user is in correct format
#     if isinstance(user_weight,float) & isinstance(user_height,float):
#         print(bodyMassIndex(user_weight,user_height))
#         invalidInput=False
#     else:
#         invalidInput=True

#---------------With complex structures-----
# BMI (Body Mass Index) Calculator
UNITS = {
    'weight': {
        'M': 'KG',
        'I': 'Pounds'
    },
    'height': {
        'M': 'Meters',
        'I': 'Inches'
    }
}
BMI_RANGE = {
    15: 'Severe Thinness',
    16: 'Moderate Thinness',
    18.5: 'Mild Thinness',
    25: 'Normal',
    30: 'Overweight',
    35: 'Obese Class I',
    40: 'Obese Class II',
    41: 'Obese Class III'
}


def bmi(unit, weight, height):
    if unit == 'M':
        result = round(weight / (height ** 2), 2)
    else:
        result = round((703 * weight) / (height ** 2), 2)

    return result


def get_bmi_range(bmi):
    for limit, range_name in BMI_RANGE.items():
        if bmi <= limit:
            return range_name
        return BMI_RANGE[41]


def print_bmi(unit, weight, height, bmi, bmi_range):
    print(f'The BMI for {weight} {UNITS["weight"][unit]} and {height} {UNITS["height"][unit]} is: {bmi}')
    print('BMI Classification:', bmi_range)


def is_float(num):
    try:
        result = float(num)
    except ValueError:
        result = False
    return result


def convert_feet_inches(feet):
    return feet * 12


unit = ''  # Metric (Kg / Meters) / Imperial (Pounds / Inches)
weight = ''
height = ''
while unit not in ['M', 'I']:
    unit = input('Select a unit system => Metric / Imperial: (M / I): ').upper()
while not isinstance(weight, float):
    weight = is_float(input(f'Type the weight in {UNITS["weight"][unit]}: '))
while not isinstance(height, float):
    height = is_float(input(f'Type the height in {UNITS["height"][unit]} (eg. 1.75 OR 5.20): '))
if unit == 'I':
    i, d = divmod(height, 1)
    height = convert_feet_inches(i) + (d * 100)
bmi = bmi(unit, weight, height)
bmi_range = get_bmi_range(bmi)
print_bmi(unit, weight, height, bmi, bmi_range)