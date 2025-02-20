year=int(input("Enter the Deposited Year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    p=float(input("Enter Principal: "))            
    r=float(input("Enter Rate of Interest: "))
    t=float(input("Enter Tenure: "))
    print("The interest is: ",p*r*t/100)
else:
    print("Not valid")
