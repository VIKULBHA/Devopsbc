#import fibo # full import
# print("running from main")
# fibo.fib(100)
# f = fibo.fib2(30)
# print(f)

# # we can also import a part of the file
# from fibo import fib2
# print("running from main")
# f = fib2(30)
# print(f)

#_______________
import BMIcalculator
print(BMIcalculator.BMI(100, 2))
print(BMIcalculator.bmi2(220, 77.8))

import fibo
from bmi_calculator import bmi
f = fib(100)
print(f)
print(bmi_calculator.bmi(100, 2))