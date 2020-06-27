def BMI(weight, height):
    return round(weight / (height ** 2), 2)
def bmi2(weight,height):
    weight_kg = weight / 2.285
    height_m = height / 39.37
    return round(weight_kg / (height_m ** 2), 2)