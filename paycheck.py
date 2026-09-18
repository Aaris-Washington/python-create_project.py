# Name: Aaris Washington
# Date: 9/17/2026
# Course: COMP 163
# Project 1: Paycheck Calculator

# Put your name after "# Name:" above. The grader checks that it is filled in.

# Read four values from the user, in this order:
employee_name =input("Enter the employee's name: ")
hours_worked= float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate of pay: "))
tax_rate_percent = float(input("Enter tax rate as a percent: "))
#
# Hours worked and the hourly rate can have a fraction in them, like 37.5
# hours or 10.25 hours. Use float() for all three numbers, not int().
# int("37.5") crashes.
#
# Then calculate:
gross pay     = hours worked * hourly rate
tax withheld  = gross pay * (tax rate / 100)
net pay       = gross pay - tax withheld

# Then print the four required output lines.
# The exact format is in README.md. Match it exactly or the tests will fail.
print(f"(Employee: {employee_name}")
print(f"Gross pay: ${gross_pay:.2f}")
print(f"Tax withheld: ${tax_withheld:.2f}")
print(f"Net pay: ${net_pay:.2f}")
# Chapters 1 and 2 only. Use variables, input(), arithmetic, type conversion,
# and print(). Do not use if statements, loops, functions, or imports.
# Your code runs top to bottom, once.
