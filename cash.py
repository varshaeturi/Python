# penny = 1
# nickles = 5
# dimes = 10
# quarters = 25
penny = 0
nickle = 0
dime = 0
quarter = 0


cash_input = float(input("please enter the money: "))
#print(cash_input)

if cash_input < 0:
    print("invalid input")
        
        
elif cash_input == 0:
    print("0")
       

        
new_cash = (cash_input * 100)

while new_cash > 0:        
    if new_cash  >= 25:
        quarter+=1
        new_cash = new_cash - 25
                
    if new_cash < 25 and new_cash >= 10:
        dime+=1
        new_cash = new_cash - 10

    if new_cash < 10 and new_cash >= 5:
        nickle+=1
        new_cash = new_cash - 5
                
    if new_cash < 5 and new_cash >= 1:
        penny+=1
        new_cash = new_cash -1 
                
    total_cash = (quarter + dime + nickle + penny) 

print(total_cash)
    
        
            
                

        

        


        


   