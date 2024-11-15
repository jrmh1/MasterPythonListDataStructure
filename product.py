product_list = ["Laptop", "Desk Chair", "Smartwatch", "Notebook", "Running Shoes"]
product_categories = ["Electronics", "Furniture", "Electronics", "Stationery", "Apparel"]
product_prices = [30000.00, 3000.00, 2500.00, 100.00, 4500.00]
product_stocks = [50, 200, 150, 0, 100]
product_supplier_emails = ["supplier1@gmail.com", "supplier2@gmail.com", "supplier3@gmail.com", "supplier4@gmail.com", "supplier5@gmail.com"]


print("Product Data:")
for i in range(len(product_list)):
    print(f"Product: {product_list[i]}, Category: {product_categories[i]}, Price: ₱{product_prices[i]}, Stock: {product_stocks[i]}, Supplier Email: {product_supplier_emails[i]}")
