#write a python program to build a calculator
user_input = input("enter input without spaces: ")
for i in user_input:
    if i =='+' or i=='-' or i=='*' or i=='/':
        oper = i
print(oper)
new_list = user_input.split(oper)
print(new_list)
if oper == '+':
    cal = float(new_list[0]) + float(new_list[1])
elif oper == '-':
    cal = float(new_list[0]) - float(new_list[1])
elif oper == '*':
    cal = float(new_list[0]) * float(new_list[1])
elif oper == '/':
    cal = float(new_list[0]) / float(new_list[1])
else:
    print("invalid oper")
print(round(cal, 2))

       