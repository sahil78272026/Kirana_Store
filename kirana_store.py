"""making a kirana store
asking items 
calculating there price and printing total in the end.
"""


total =0
list = []
while(True):
    userInput = input("Enter the item price or q to quit: \n")
    if userInput!='q':
        total = total + int(userInput)
        print(f"Order total so far {total}")
        list.append(userInput) 
    
    else:
        print("Thanks for shoppping with Us")
        break


print(f"Your total is : {total}")
print(f"You Have Ordered below items")
for items in list:
    print(items)
