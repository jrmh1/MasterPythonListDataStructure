
employee_ids = [1, 2, 3, 4, 5]
employee_names = ["Bogart Torres", "Bogart Reyes", "Bogart Dela Cruz", "Lisa Wong", "Paul McDonald"]
employee_departments = ["Sales", "Human Resources", "IT", "Marketing", "Finance"]
employee_ages = [30, 25, 40, 28, 35]
employee_emails = ["bogart.torres@company.com", "bogart.reyes@company.com", "bogart.delacruz@company.com", "lisa.wong@company.com", "paul.mcdonald@company.com"]


print("Employee Data:")
for i in range(len(employee_ids)):
    print(f"ID: {employee_ids[i]}, Name: {employee_names[i]}, Department: {employee_departments[i]}, Age: {employee_ages[i]}, Email: {employee_emails[i]}")