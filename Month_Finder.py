c=int(input("Enter your choice: "))
month=["January", "February", "March","April","May","June","July","August","September","October","November","December"]
if c<=12:
    print("The month is: "+month[c-1])
else:
    print("Invalid Input")
    
