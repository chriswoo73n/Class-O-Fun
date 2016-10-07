#this code will calculate the user salary per yr along with bonus 
employee_name = input("Enter Employee Name: ")
employee_category = input("Enter Employee Category: ")
yearly_salary = float(input("Enter Yearly Salary: "))

hrs_per_yr = 2080
federal_tax_rate = .18
fica_tax_rate = .062
medicare_tax_rate = .0145
work_day_hours = 8
sick_days_used = 5
total_months_worked = 12
monthly_sick_accrual = 8
exec_min_salary = 150000
manager_min_salary = 90000
skill_min_salary = 50000
unskill_min_salary = 15080
exec_bonus_ratio = 1/2
manager_bonus_ratio = 2/5
skill_bonus_ratio = 1/4
unskill_bonus_ratio = 1/20
bonus = 0


earned_sick_hours = total_months_worked * monthly_sick_accrual
used_sick_hours = sick_days_used * work_day_hours
carry_over_sick = earned_sick_hours - used_sick_hours
hours_worked = hrs_per_yr - used_sick_hours
print_statement = True

if(employee_name == "Guido" and yearly_salary == 0 or yearly_salary < 0):
    print("Guido van Rossum is creator of Python")
    print_statement = False
elif(employee_category == 'E' or employee_category == 'e'):
    hourly_rate = yearly_salary / hrs_per_yr
    bonus = hours_worked * hourly_rate * exec_bonus_ratio

elif(employee_category == 'M' or employee_category == 'm'):
    if(yearly_salary <= manager_min_salary or yearly_salary >= exec_min_salary):
        yearly_salary = manager_min_salary

    hourly_rate = yearly_salary / hrs_per_yr
    bonus = hours_worked * hourly_rate * manager_bonus_ratio

elif(employee_category == 'S' or employee_category == 's'):
    if(yearly_salary <= skill_min_salary or yearly_salary >= manager_min_salary):
        yearly_salary = skill_min_salary

    hourly_rate = yearly_salary / hrs_per_yr
    bonus = hours_worked * hourly_rate * manager_bonus_ratio
elif(employee_category == 'U' or employee_category == 'u'):
    if(yearly_salary <= unskill_min_salary or yearly_salary >= skill_min_salary):
        yearly_salary = unskill_min_salary

    hourly_rate = yearly_salary / hrs_per_yr
else:
    print_statement = not(print_statement)
    print("\nInvalid employee category entry")

if(print_statement):
    federal_tax_year = yearly_salary * federal_tax_rate
    fica_tax_year = yearly_salary * fica_tax_rate
    medicare_tax_year = yearly_salary * medicare_tax_rate

    total_salary = yearly_salary + bonus;
    net_salary = total_salary - federal_tax_year - fica_tax_year - \
                medicare_tax_year

    print("\nEmployee Name: \t", employee_name)
    print("Hourly Rate: \t", format(hourly_rate, '10.2f'))
    print("\nSalary: \t", format(yearly_salary, '10.2f'))
    print("Bonus: \t\t", format(bonus, '10.2f'))
    print("Total Salary: \t", format(total_salary, '10.2f'))
    print("Fed Tax: \t", format(federal_tax_year, '10.2f'))
    print("FICA Tax: \t", format(fica_tax_year, '10.2f'))
    print("Medicare Tax: \t", format(medicare_tax_year, '10.2f'))
    print("Net Salary: \t", format(net_salary, '10.2f'))
    print("\nSick Hours Earned: \t", earned_sick_hours)
    print("Sick Hours Used: \t", used_sick_hours)
    print("Sick Hours Carryover: \t", carry_over_sick)

