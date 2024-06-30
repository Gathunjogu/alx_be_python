# finance_calculator.py

print("Script started")

try:
    # User input for financial details
    print("Asking for monthly income")
    monthly_income_str = input("Enter your monthly income: ")
    print(f"Received input for monthly income: {monthly_income_str}")
    monthly_income = float(monthly_income_str)
    print(f"Converted monthly income to float: {monthly_income}")

    print("Asking for monthly expenses")
    monthly_expenses_str = input("Enter your total monthly expenses: ")
    print(f"Received input for monthly expenses: {monthly_expenses_str}")
    monthly_expenses = float(monthly_expenses_str)
    print(f"Converted monthly expenses to float: {monthly_expenses}")

    # Calculate monthly savings
    monthly_savings = monthly_income - monthly_expenses
    print(f"Calculated monthly savings: {monthly_savings}")

    # Project annual savings with 5% interest
    annual_savings = monthly_savings * 12
    interest = annual_savings * 0.05
    projected_savings = annual_savings + interest
    print(f"Calculated projected savings: {projected_savings}")

    # Output results
    print(f"Your monthly savings are ${monthly_savings:.2f}.")
    print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")

except ValueError as e:
    print(f"Error: Invalid input. Please enter numeric values. Details: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("Script ended")
