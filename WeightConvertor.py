
# simple prints
print('welcome to the weight converter!')
print('''
how it works? well its simple you imput your wieght(lbs or kg) then you choose the type of weight(again or lbs or kg) then the code will convert it to the
opposite type of wieght.
remember to follow me on github.com david896<3
''')
# here we are getting our value of weight and we check if the value we got is in pounds or kilograms
valOfWeight = float(input("tell us your weight: "))
resp = input('kg or lbs? :')
print()
print(valOfWeight)
print(resp)
# now here we are having the conversion
if resp == 'lbs':
    print('converting...')
    print('here is your weight in kilograms :', valOfWeight / 2.20)
#Now we are going to do an elif for converting the kg into lbs:
if resp == 'kg':
    print('converting...')
    print('here is your weight in pounds:', valsOfWeight * 2.20)
