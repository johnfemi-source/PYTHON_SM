distance = float(input("Enter distance (miles): "))
mpg = float(input("Enter fuel efficiency (mpg): "))
price = float(input("Enter price per gallon ($): "))

cost = (distance / mpg) * price

print(f"\nCost of trip: ${cost:.2f}")
