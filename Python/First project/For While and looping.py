# for letter in 'ComIT':     # First Example will print COMIT sequence as FOR is a loop and will
#     # do reiterations on the sequence
#    print('Current Letter :', letter)
#
# fruits = ['banana', 'apple',  'mango']
# for fruit in fruits:        # Second Example
#    print('Current fruit :', fruit) # statements section
#
# for index in range(len(fruits)): # Third Example
#    print('Current fruit :', fruits[index])
# words = input("Type any word:") Wrong code
# if isinstance(words, str):
#     print("all good keep going")
# else:
#     words = float(words)
#
# For words in 'words':
#     print("Current word :", word)

#
# words = input("Type any word:")
# if isinstance(words, str):
#     print("all good keep going")
# else:
#     words = float(words)
#
# for word in words:
#     print("Current word :", word)
# #-----------------------------------------------
# for x in 'This is long test':
#     print('each letter', x)
# #-----------------------------------------
        # for y in [0, 2, 3, 4, 6, 7, 8, 9]:
        #   is_even = lambda x: x % 2 ==0
        # filter(is_even, y)
# y = [0,2,3,4,6,7,8,9]
# is_even = lambda x: x % 2 ==0 # delegate, all delegates are functions
# even_numbers = filter(is_even, y)
# for n in even_numbers:
#     print(n)
#-----------------------------
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
#------------------------------
testing = 'Testing a bunch of words'
length_testing = len(testing.replace(" ", ""))
print(testing, length_testing)
#-------------------------
sentence = ' hello apple'
