total_bill=float(input("What is the total bill? $"))
tip_percent=float(input("What percentage would you like to give tip? %"))
total_people=float(input("How many people to split bill?"))

tip_amount=((tip_percent)/100)*total_bill

tip_per_person=total_bill+tip_amount/total_people

print( "Each person should pay",tip_per_person)

