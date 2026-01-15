def is_valid(*args):
    return all(isinstance(i, (int,float)) for i in args)

def monthly_split(rent, food, electricity_bill, persons):
    total = (rent + food + electricity_bill) / persons
    print("\n--- Monthly Split Summary ---")
    print(f"Total Rent: ₹{rent}")
    print(f"Total Food: ₹{food}")
    print(f"Electricity Bill: ₹{electricity_bill}")
    print(f"Total Persons: {persons}")
    print(f"=> Each person has to pay: ₹{round(total,2)}")

try:
    rent = float(input("Enter total rent of flat: "))
    food = float(input("Enter the amount of total food ordered: "))
    electricity_spend = float(input("Enter total electricity spend: "))
    electricity_per_unit = float(input("Enter electricity per unit: "))
    persons = int(input("Enter total persons live in flat: "))

    if is_valid(rent, food, electricity_spend, electricity_per_unit, persons):
        electricity_bill = electricity_spend * electricity_per_unit
        monthly_split(rent, food, electricity_bill, persons)
    else:
        raise ValueError(f"❌ All values must be int or float")

except ValueError as e:
    raise ValueError(f"Error: {e}")
