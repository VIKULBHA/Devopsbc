# n = input('Choose a number')
# print ('Number %s \n' % (n))
#
# print ('Number:', n)
#
# if ( n == 100 ):
#     print("Value of the random number is equal to 100")
# else:
#     print("Value of the random number is NOT equal to 100")
#
n = input("Please enter an integer: ")
if isinstance(n, int):
    print("all good keep going")
else:
    n = float(n)

if n < 0:
    print('Negative')
elif n == 0:
    print('Zero')
elif n == 1:
    print('Single')
else:
    print('Higher value')

print("The value of random_number is: ", n)