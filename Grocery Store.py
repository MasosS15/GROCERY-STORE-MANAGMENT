# Welding materials and stock Management System

import sys

# In-memory store for products
Materials = {}

# Add product
def add_material():
    material_id = input("Enter Material ID: ")
    if material_id in products:
        print("material ID already exists.")
        return
    name = input("Enter material Name: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))
    materials[material_id] = {'name': name, 'price': price, 'quantity': quantity}
    print("material added successfully.\n")

# View all products
def view_material():
    if not materials:
        print("No materials in inventory.\n")
        return
    print("\n--- material List ---")
    for pid, info in materials.items():
        print(f"ID: {pid}, Name: {info['name']}, Price: {info['price']}, Quantity: {info['quantity']}")
    print()

# Update product
def update_material():
    material_id = input("Enter material ID to update: ")
    if material_id not in materials:
        print("material not found.\n")
        return
    name = input("Enter New material Name: ")
    price = float(input("Enter New Price: "))
    quantity = int(input("Enter New Quantity: "))
   material[material_id] = {'name': name, 'price': price, 'quantity': quantity}
    print("Product updated successfully.\n")

# Delete product
def delete_material():
    material_id = input("Enter material ID to delete: ")
    if material_id in materials:
        del material[material_id]
        print("material deleted successfully.\n")
    else:
        print("material not found.\n")

# Purchase/Bill generation
def purchase_material():
    if not material:
        print("No materials available for purchase.\n")
        return

    cart = {}
    total = 0

    while True:
        material_id = input("Enter material ID to purchase (or 'done' to finish): ")
        if material_id.lower() == 'done':
            break
        if material_id not in material:
            print("Invalid material ID.")
            continue
        quantity = int(input("Enter quantity: "))
        if quantity > materials[material_id]['quantity']:
            print("Insufficient stock.")
            continue
        price = materials[material_id]['price']
        total += price * quantity
        materials[material_id]['quantity'] -= quantity
        cart[material_id] = {'name': materials[material_id]['name'], 'quantity': quantity, 'price': price}

    # Bill
    print("\n----- Bill -----")
    for pid, item in cart.items():
        print(f"{item['name']} - {item['quantity']} x {item['price']} = {item['quantity'] * item['price']}")
    print(f"Total Amount: {total:.2f}")
    print("----------------\n")

# Menu
def menu():
    while True:
        print("=== Grocery Store Management ===")
        print("1. Add materials")
        print("2. View materials")
        print("3. Update material")
        print("4. Delete material")
        print("5. Purchase materials")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_materials()
        elif choice == '2':
            view_materials()
        elif choice == '3':
            update_materials()
        elif choice == '4':
            delete_materials()
        elif choice == '5':
            purchase_materials()
        elif choice == '6':
            print("Exiting system. THANK YOU VISIT AGAIN !")
            sys.exit()
        else:
            print("Invalid choice. Please try again.\n")

# Run the system
menu()
