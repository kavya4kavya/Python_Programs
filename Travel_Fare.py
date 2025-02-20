print("Travel Destinations with charges")
print("""
                    Place                       Charge
                 1. Bengaluru           1000
                 2.Mumbai                2000
                 3.Delhi                      1500
                 4.Kolkata                  4000
                 5.Chennai                 3000
                 6.Lucknow                4500
                 7. Jaipur                    3500""")
c1=int(input("Enter Destination 1: "))
c2=int(input("Enter Destination 2: "))
c3=int(input("Enter Destination 3: "))
charge=[1000,2000,1500,4000,3000,4500,3500]
print("The total fare is: ",charge[c1-1],"+",charge[c2-1],"+",charge[c3-1],"=",charge[c1-1]+charge[c2-1]+charge[c3-1])
