# Shopping Cart System
# AI Engineering - AM


# Import datetime to display the current date on the receipt
import datetime
 
 
# Store Inventory
# Matching indexes in products and prices to represent the same item
products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]
 

# Creating an empty shopping cart
shopping_cart = [] # This list stores the names of the products the customer selects
 
 
# Displaying available products and the prices
def display_products(products, prices):
    print("========== AVAILABLE PRODUCTS ==========")
 
    # Using a for loop to display every product and price
    for i in range(len(products)):
        print(i + 1, ".", products[i], "$", format(prices[i], ".2f"))
 
 
# Adding a product to shopping cart
def add_product(products, prices, shopping_cart):
 
    display_products(products, prices) # Display the products so the customer can choose
 
    valid_choice = False
 
    while valid_choice == False: # Keep asking until a valid product number is entered
        choice = int(input("Enter product number: "))
 
        if choice >= 1 and choice <= len(products):
            shopping_cart.append(products[choice - 1])
            print(products[choice - 1], "was added to your cart!")
            valid_choice = True
        else:
            print("Invalid product!")
            print("Please choose a number between 1 and", len(products))
 
 
# Removing one product from shopping cart
def remove_product(shopping_cart):
    if len(shopping_cart) == 0: # Check whether cart is empty
        print("Your shopping cart is empty!")
        print("There is nothing to remove.")
        return
    print("========== YOUR SHOPPING CART ==========")
 
    # Displaying every item in the cart
    for i in range(len(shopping_cart)):
        print(i + 1, ".", shopping_cart[i])
 
    valid_choice = False
 
    # Asking until the customer selects a valid cart position
    while valid_choice == False:
        choice = int(input("Enter item number to remove: "))
 
        if choice >= 1 and choice <= len(shopping_cart):
            removed_item = shopping_cart.pop(choice - 1)
            print(removed_item, "was removed from your cart!")
            valid_choice = True
        else:
            print("That item does not exist in your cart!")
 
 
# Displaying the shopping cart with prices
def display_cart(shopping_cart, products, prices):
    # Checking whether the cart is empty
    if len(shopping_cart) == 0:
        print("Your shopping cart is empty!")
        return
    print("========== YOUR SHOPPING CART ==========")
 
    # Displaying product and find the price
    for i in range(len(shopping_cart)):
        item = shopping_cart[i]
        price_index = products.index(item)
        price = prices[price_index]
 
        print(i + 1, ".", item, "$", format(price, ".2f"))
 
    # Displaying the total number of items
    print("Total Items:", len(shopping_cart))
 
 
# Calculating and returning the shopping cart subtotal
def calculate_total(shopping_cart, products, prices):
 
    # Starting the running total at zero
    total = 0.0
 
    # Adding each product's price to the running total
    for item in shopping_cart:
        price_index = products.index(item)
        total = total + prices[price_index]
 
    # Returning calculated subtotal
    return total
 
 
# Displaying the current subtotal
def display_total(shopping_cart, products, prices):
 
    # Calculating the subtotal using the calculate_total function
    subtotal = calculate_total(shopping_cart, products, prices)
 
    print("========== CURRENT TOTAL ==========")
 
    # Displaying every item and its price
    for item in shopping_cart:
        price_index = products.index(item)
        print(item, "$", format(prices[price_index], ".2f"))
 
    # Displaying the subtotal (once, after the loop)
    print("Subtotal: $", format(subtotal, ".2f"))
 
 
# Calculating the discount rate based on the subtotal
def calculate_discount(subtotal):
 
    # Applying the correct discount for the subtotal
    if subtotal < 10:
        return 0.00
    elif subtotal < 20:
        return 0.05
    elif subtotal < 40:
        return 0.10
    else:
        return 0.15
 
 
# Completing the checkout and printing the receipt
def checkout(shopping_cart, products, prices):
 
    # Not allowing checkout when the cart is empty
    if len(shopping_cart) == 0:
        print("Your shopping cart is empty!")
        print("Please add an item before checking out")
        return False
 
    # Calculating the subtotal and discount rate
    subtotal = calculate_total(shopping_cart, products, prices)
    discount_rate = calculate_discount(subtotal)
 
    # Calculating the money saved and the final total
    amount_saved = subtotal * discount_rate
    final_total = subtotal - amount_saved
 
    today = datetime.date.today()
 
    print("========== RECEIPT ==========")
 
    # Display the current date
    print("Date:", today.strftime("%m/%d/%Y"))
 
    print("---------------------")
 
    # Displaying every purchased item and its price
    for item in shopping_cart:
        price_index = products.index(item)
        print(item, "$", format(prices[price_index], ".2f"))
 
    # Displaying the subtotal, discount savings, and the final total
    print("---------------------")
    print("Subtotal: $", format(subtotal, ".2f"))
    print("Discount:", int(discount_rate * 100), "%")
    print("Amount Saved: $", format(amount_saved, ".2f"))
    print("Final Total: $", format(final_total, ".2f"))
    print("Thank you for shopping!")
 
    # Return True to show that checkout succeeded
    return True
 
 
# Displaying the main menu
def main():
 
    # Use this variable to control the menu loop
    shopping = True
 
    # Repeat the menu while the customer is shopping
    while shopping == True:
        print("========== SMART SHOPPING CART ==========")
        print("1. View Available Products")
        print("2. Add Product to Cart")
        print("3. Remove Product from Cart")
        print("4. View Shopping Cart")
        print("5. View Current Total")
        print("6. Checkout")
 
        # Asking the customer to choose a menu option
        choice = int(input("Enter your choice: "))
 
        # Calling the correct function for each menu option
        if choice == 1:
            display_products(products, prices)
        elif choice == 2:
            add_product(products, prices, shopping_cart)
        elif choice == 3:
            remove_product(shopping_cart)
        elif choice == 4:
            display_cart(shopping_cart, products, prices)
        elif choice == 5:
            display_total(shopping_cart, products, prices)
        elif choice == 6:
            # Stop shopping only if checkout succeeds
            checkout_complete = checkout(shopping_cart, products, prices)
 
            if checkout_complete == True:
                shopping = False
 
        else:
            # Displaying a message for the invalid menu selection
            print("Invalid option!")
            print("Please choose a number between 1 and 6")
 
 
# Starting the program
main()
 