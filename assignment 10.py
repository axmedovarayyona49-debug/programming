sales_data = [
    "E101|Laptop|1200.00",
    "E102|Mouse|25.50",
    "E101|Monitor|300.00",
    "E103|Headphones|150.00",
    "E102|Keyboard|50.00",
    "E103|Laptop|1000.00",
    "E101|Mousepad|15.00"
]

def compile_sales(sales_data):
    result = {}
    for record in sales_data:
        emp_id, _, cost_str = record.split("|")
        cost = float(cost_str)

        if emp_id in result:
            result[emp_id] += cost
        else:
            result[emp_id] = cost
    return result

def show_best_employee(total_sales):
    max_amount = -1
    max_emp = None

    print("Employee Sales Summary:")
    for emp_id, amount in total_sales.items():
        print(f"{emp_id}: ${amount:.2f}")

        if amount > max_amount:
            max_amount = amount
            max_emp = emp_id

    print("-" * 35)
    print(f"Highest Seller: {max_emp} with ${max_amount:.2f}")

summary = compile_sales(sales_data)
show_best_employee(summary)
