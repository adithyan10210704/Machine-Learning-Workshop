try:
    result=10/0
except ZeroDivisionError:
    print("You cannot divide by 0")
except ValueError:
    print("Invalid value")
