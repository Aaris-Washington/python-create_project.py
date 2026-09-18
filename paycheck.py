# Name: Aaris Washington
# Date: 9/17/2026
# Course: COMP 163
# Project 1: Paycheck Calculator

employee_name =input("Enter the employee's name: ")
hours_worked= float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate of pay: "))
tax_rate_percent = float(input("Enter tax rate as a percent: "))

gross_pay     = hours_worked * hourly_rate
tax_withheld  = gross_pay * (tax_rate_percent / 100)
net_pay       = gross_pay - tax_withheld

print(f"(Employee: {employee_name}")
print(f"Gross pay: ${gross_pay:.2f}")
print(f"Tax withheld: ${tax_withheld:.2f}")
print(f"Net pay: ${net_pay:.2f}")

