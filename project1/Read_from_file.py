employee_collection = open("employee.txt", "r")

print(employee_collection.read())

print(employee_collection.readlines())


for emp in employee_collection.readlines():
    print(emp)

employee_collection.close()


employee_collection = open("employee.txt", 'a')

employee_collection.write("\n from Asia")


employee_collection.close()

employee_collection = open("employee1.txt", 'a')

employee_collection.cl