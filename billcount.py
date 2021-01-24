print("Want to count bill? ")
bill   = float(input("what is total bill? $"))
tip    = int(input("how much do you like to give? 10, 12, or 15? "))
people = int(input("how many people? "))
tip_percent = tip/100
tip_all = tip_percent*bill
price  = bill + tip_all
person_bill = price/people
print(round(person_bill, 2))