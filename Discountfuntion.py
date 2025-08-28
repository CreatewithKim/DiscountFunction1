# Function to calculate discounted price
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:   # Apply discount only if 20% or more
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price   # No discount applied


# Prompt user for input
original_price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

# Use the function
final_price = calculate_discount(original_price, discount)

# Print result
print(f"Final Price: {final_price}")
