


try:
    print(hi,John)
    value = 10/0
    number = int(input("enter a number: "))
    print(number)
    
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")
except NameError as err:
    print(err)