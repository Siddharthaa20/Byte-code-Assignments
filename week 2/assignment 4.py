transactions = [5000, -250, 12000, -50, 0, 7000, -1500]

for transaction in transactions:
    if transaction > 0:
        print(f"Valid transaction: {transaction}")
    elif transaction == 0:
        print("Warning: Zero value transaction found.")
    else:
        print(f"ERROR: Invalid transaction: {transaction}")
