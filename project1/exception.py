try:
    print(10/0)
    num = int(input("Enter the number "))
    print(num)

except ZeroDivisionError:
    print("division errror")

except ValueError:
    print("invalid entry")

