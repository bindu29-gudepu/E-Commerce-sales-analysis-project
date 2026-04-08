# Sample sales data
products = ["Laptop", "Mobile", "Headphones", "Tablet", "Smartwatch"]
sales = [50000, 30000, 15000, 20000, 25000]
# Print product-wise sales
print("Product-wise Sales Data:")
for p, s in zip(products, sales):
print(p, ":", s)
# Basic calculations
total_sales = sum(sales)
average_sales = total_sales / len(sales)
max_sales = max(sales)
min_sales = min(sales)
best_product = products[sales.index(max_sales)]
worst_product = products[sales.index(min_sales)]
print("\n===== RESULTS =====")
print("Total Sales =", total_sales)
print("Average Sales =", average_sales)
print("Best Selling Product =", best_product)
print("Worst Selling Product =", worst_product)
# Products above average
print("\nProducts Above Average:")
for p, s in zip(products, sales):
if s > average_sales:
print(p)
# Sales percentage
print("\nSales Percentage:")
for p, s in zip(products, sales):
percentage = (s / total_sales) * 100
print(p, ":", round(percentage, 2), "%")
print("\n===== END OF ANALYSIS =====")
