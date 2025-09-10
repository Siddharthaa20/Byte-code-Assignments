customer = {
    "customer_id": 101,
    "name": "Suresh",
    "city": "Hyderabad",
    "purchase_history": [2500, 1500, 5000]}

customer["email"] = "suresh.h@email.com"


total_purchase_value = sum(customer["purchase_history"])

print("Customer:", customer["name"])
print("Total Purchase Value:", total_purchase_value)
