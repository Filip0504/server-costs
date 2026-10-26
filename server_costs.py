number_of_servers = int(input("How many servers do you have?\n"))
monthly_cost_per_server = float(input("How much do you pay per server?\n"))
discount_rate = 0.10

months_in_year = 12

monthly_total = number_of_servers * monthly_cost_per_server
yearly_total = monthly_total * months_in_year
monthly_discount_amount = monthly_total * discount_rate


print(f"The total monthly cost for {number_of_servers} servers would be: € {monthly_total:.2f}")
print(f"The total yearly cost for {number_of_servers} servers would be: € {yearly_total:.2f}")
print(f"The yearly cost of one server would be € {monthly_cost_per_server * months_in_year:.2f}")
print(f"The monthly discount would be € {monthly_discount_amount:.2f} and the total price per month would be € {monthly_total - monthly_discount_amount:.2f}")

