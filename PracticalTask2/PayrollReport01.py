# Welcome to Practical Task 2
# Let's get started

# First, let's import our file and convert it into a list
with open("Employees.txt", "r") as file:
    string_data = file.read()
list_data = string_data.split('\n')

# And define our dictionary
employees = {}

# Now we define a function to create our dictionary items
def create_item(shortlist):
    employees[shortlist[0]] = [shortlist[1], shortlist[2], float(shortlist[3])]

# And now we can create our dictionary
for i in range(0, len(list_data), 4):
    shortlist = list_data[i:i+4]
    create_item(shortlist)

# Now that we have our dictionary, we can get all the information we need
# Snce it has to be modular, we will have to define functions

# To print the list of employees
def print_employees(employees):
    for key, value in employees.items():
        display = f"{key} {value[0]} {value[1]} ${value[2]:,.2f}"
        print(display)

# For the total wages
def total_wages(employees):
    total = 0
    for x in employees:
        total += employees[x][2]
    return total
    

# For the total number of employees
def count_employees(employees):
    return len(employees)

# For the average wages
def average_wages(employees):
    total = total_wages(employees)
    count = count_employees(employees)
    if count == 0:
        return 0
    else:
        return total/count

# For total wages of managers
def total_manager_wages(employees):
    total = 0
    for x in employees:
        if employees[x][1] == "Manager":
            total += employees[x][2]
    return total

# For total wages of sales
def total_sales_wages(employees):
    total = 0
    for x in employees:
        if employees[x][1] == "Sales":
            total += employees[x][2]
    return total

# For total wages of administration
def total_administration_wages(employees):
    total = 0
    for x in employees:
        if employees[x][1] == "Administration":
            total += employees[x][2]
    return total

# Now for the final output
print_employees(employees)
print(f"\nTotal payroll: ${total_wages(employees):,.2f}")
print(f"Number on payroll: {count_employees(employees)}")
print(f"Average pay: ${average_wages(employees):,.2f}\n")
print("Total pay for:")
print(f"Managers: ${total_manager_wages(employees):,.2f}")
print(f"Sales: ${total_sales_wages(employees):,.2f}")
print(f"Admin: ${total_administration_wages(employees):,.2f}")

# Now let's make that into a string so we can use writelines to write it to our file
write_string = (f"Total payroll: ${total_wages(employees):,.2f}\n"
                f"Number on payroll: {count_employees(employees)}\n"
                f"Average pay: ${average_wages(employees):,.2f}\n\n"
                "Total pay for:\n"
                f"Managers: ${total_manager_wages(employees):,.2f}\n"
                f"Sales: ${total_sales_wages(employees):,.2f}\n"
                f"Admin: ${total_administration_wages(employees):,.2f}")

# And now we can write that string to our new file
with open("PayrollTeport.txt", "w") as file:
    file.write(write_string)

print("Operation completed.")
