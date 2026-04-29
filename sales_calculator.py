# small Business Sales Calculator

def add_sales():
    item = input("Enter item name:")
    price = float(input("Enter item price:"))
    quantity = int(input("Enter quantity sold:"))
    total = price * quantity
    return item, price, quantity, total

def display_sales(item, price, quantity, total):
    print("\n---Sale Record---")
    print(f"Item Name: {item}")
    print(f"Price: {price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total: {total:.2f}")

def calculate_summary(sales):
    grand_total = sum(sale[3] for sale in sales)
    print("\n---sales summary---")
    print(f"Total Sales Amount: {grand_total}")

#Main program loop
sales = []
while True:
    item, price, quantity, total = add_sales()
    display_sales(item, price, quantity, total)
    sales.append([item, price, quantity, total])

    choice = input("Do you want to add another sale? (y/n): ")
    if choice.lower() != 'y':
        break

calculate_summary(sales)