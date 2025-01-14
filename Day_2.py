amount  = float(input("What is the Total Bill: "))
people = int(input("Person: "))
tip = float(input("Tip percentage: "))
percen_tage = tip/100
tip_cal = amount*percen_tage
split_cal = ((tip_cal+amount)/people)
final_bill = "{:.2f}".format(split_cal)
print(final_bill)
