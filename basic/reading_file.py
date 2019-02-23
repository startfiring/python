
try:

    employee_file = open("employees.txt", "r")
    #employee_file = open("employees.txt", "w")
    #employee_file = open("employees.txt", "a")
    #employee_file = open("employees.txt", "r+")

    test = 10/0

except FileNotFoundError as err:
    print(err)

else:
    for step in employee_file.readlines():
        print(step)

    employee_file.close()

finally:
    print("close the file and exit")

#print(employee_file.readlines()[1])


