def safe_divide(a,b):
    try:
        result=a/b
    except ZeroDivisionError:
        print("Error:Cannot divide by 0!")
    except TypeError:
        print("Error: Both arguments must be numbers")
    else:
        print(f"Result:{result}")
    finally:
        print("Execution completed")
safe_divide(10,2)
safe_divide(10,0)
safe_divide(10,'a')
