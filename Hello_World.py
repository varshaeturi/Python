# This program says hello and asks for my name

print ('hello world!')
print ('what is your name?') #asks for name
myName = input()
print ('it is good to meet you,' + myName)
print ('the length of your name is:')
print (len(myName))
print ('what is your age?') #asks for your age
myAge = input()
print ('you will be'  + str(int(myAge) + 1) + 'in a year.')
