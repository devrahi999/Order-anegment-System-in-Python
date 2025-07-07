#Full Restaurant Order manegment system

def take_order():
    import random
    from datetime import datetime
    
    
    Menu = {
        "Coffee": 70,
        "Pasta": 60,
        "Black Coffee": 90,
        "Cold Coffee": 80,
        "Pizza": 150,
        "Burger": 80,
        "Salad": 40
    }
    
    print("Welcome To Our Tatu Restaurant!\n")
    print("Menu:")
    for item, price in Menu.items():
        print(f"{item} : {price} BDT")
    
    total_pay = 0
    ordered_items = []
    
    # -------- Order Loop --------
    while True:
        item = input("\nPlease select your item: ").strip()
        if item in Menu:
            qty_input = input("Quantity: ")
            if qty_input.isdigit():
                qty = int(qty_input)
                cost = Menu[item] * qty
                total_pay += cost
                ordered_items.append((item, qty, cost))
                print(f"Your ordered item '{item}' has been added.")
            else:
                print("Invalid quantity, please enter a number!")
        else:
            print(f"Sorry, '{item}' is not available in our menu.")
            
        more = input("Would you order more item? (yes/no): ").strip().lower()
        if more != "yes":
            break
    
    # -------- Remove Option --------
    if ordered_items:
        remove = input("\nDo you want to remove any item from your order? (yes/no): ").strip().lower()
        if remove == "yes":
            print("\nYour Ordered Items:")
            for idx, (item, qty, cost) in enumerate(ordered_items):
                print(f"{idx + 1}. {item} x {qty} = {cost} BDT")
    
            rmv_index = input("Enter the number of the item to remove: ")
            if rmv_index.isdigit():
                rmv = int(rmv_index)
                if 1 <= rmv <= len(ordered_items):
                    item, qty, cost = ordered_items.pop(rmv - 1)
                    total_pay -= cost
                    print(f"'{item}' has been removed from your orders.")
                else:
                    print("Invalid number, the item is out of range!")
            else:
                print("Invalid selection, item was not removed.")
    
    # -------- Quantity Update Option --------
        update = input("\nDo you want to update quantity of any item? (yes/no): ").strip().lower()
        if update == "yes":
            print("\nYour Ordered Items:")
            for idx, (item, qty, cost) in enumerate(ordered_items):
                print(f"{idx + 1}. {item} x {qty} = {cost} BDT")
    
            index_input = input("Enter the number of the item to update: ")
            if index_input.isdigit():
                index = int(index_input) - 1
                if 0 <= index < len(ordered_items):
                    item, old_qty, old_cost = ordered_items[index]
                    new_qty_input = input(f"Enter new quantity for {item}: ")
                    if new_qty_input.isdigit():
                        new_qty = int(new_qty_input)
                        new_cost = Menu[item] * new_qty
                        total_pay -= old_cost
                        total_pay += new_cost
                        ordered_items[index] = (item, new_qty, new_cost)
                        print(f"\nUpdated: {item} x {new_qty} = {new_cost} BDT")
                    else:
                        print("Invalid quantity input!")
                else:
                    print("Invalid item number!")
            else:
                print("Invalid input!")
    
    # -------- Final Summary --------
        print("\n--- Final Summary ---\n")
        for item, qty, cost in ordered_items:
            print(f"{item} x {qty} = {cost} BDT")
    
        if total_pay >= 500:
            discount = total_pay * 0.10
            after_discount = total_pay - discount
            print(f"\nTotal bill: {total_pay} BDT")
            print(f"Discount (10%): {discount} BDT")
        else:
            after_discount = total_pay
    
        vat = after_discount * 0.05
        print(f"VAT (5%): {vat} BDT")
        print(f"Final bill: {after_discount + vat} BDT")
        token = random.randint(10000, 99999)
        print(f"\n🧾 Your Order Token: #{token}")
        now = datetime.now().strftime( " %d-%m-%Y  |  %I:%M %p")
        print(f"⏱️ Order Time: {now}")
    
        print("\nThanks for your order! Your order will be delivered in a few minutes.")
    else:
        print("\nNo valid orders were placed.")
        print("Thanks for visiting our Restaurant!")



while True:
    take_order()

    more = input("\nDo you want to take next customer's order? (yes/no): ").strip().lower()
    if more != "yes":
        print("Closing order system. Goodbye!")
        break




