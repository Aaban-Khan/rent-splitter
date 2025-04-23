rent = float(input("Enter total rent of flat: "))
food = float(input("Enter the amount of total food ordered: "))
electricity_spend = float(input("Enter total electricity spend: "))
electricity_per_unit = float(input("Enter electricity per unit: "))
persons = int(input("Enter total persons live in flat: "))

electricity_bill = electricity_spend * electricity_per_unit
total = rent + food + electricity_bill
total_bill = total // persons

def monthly_split():
    print("\n--- Monthly Split Summary ---")
    print(f"Total Rent: ₹{rent}")
    print(f"Total Food: ₹{food}")
    print(f"Electricity Bill: ₹{electricity_bill}")
    print(f"Total Persons: {persons}")
    print(f"=> Total Bill: {total}")
    print(f"=> Each person has to pay: ₹{round(total_bill,2)}")

monthly_split()