# Get inputs
bill = float(input("Enter bill amount: "))
tip_percent = float(input("Enter tip percentage: "))

# Calculate tip and total
tip = bill * (tip_percent / 100)
total = bill + tip

# Print results
print(f"Tip amount: {tip:.2f}")
print(f"Total amount to pay: {total:.2f}")

