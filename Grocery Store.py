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
    name = input("Enter New Product Name: ")
    price = float(input("Enter New Price: "))
    quantity = int(input("Enter New Quantity: "))
    products[product_id] = {'name': name, 'price': price, 'quantity': quantity}
    print("Product updated successfully.\n")

# Delete product
def delete_material():
    product_id = input("Enter Product ID to delete: ")
    if product_id in products:
        del products[product_id]
        print("Product deleted successfully.\n")
    else:
        print("Product not found.\n")

# Purchase/Bill generation
def purchase_material():
    if not products:
        print("No products available for purchase.\n")
        return

    cart = {}
    total = 0

    while True:
        product_id = input("Enter Product ID to purchase (or 'done' to finish): ")
        if product_id.lower() == 'done':
            break
        if product_id not in products:
            print("Invalid Product ID.")
            continue
        quantity = int(input("Enter quantity: "))
        if quantity > products[product_id]['quantity']:
            print("Insufficient stock.")
            continue
        price = products[product_id]['price']
        total += price * quantity
        products[product_id]['quantity'] -= quantity
        cart[product_id] = {'name': products[product_id]['name'], 'quantity': quantity, 'price': price}

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
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Purchase Products")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_product()
        elif choice == '2':
            view_products()
        elif choice == '3':
            update_product()
        elif choice == '4':
            delete_product()
        elif choice == '5':
            purchase_products()
        elif choice == '6':
            print("Exiting system. THANK YOU VISIT AGAIN !")
            sys.exit()
        else:
            print("Invalid choice. Please try again.\n")

# Run the system
menu()
