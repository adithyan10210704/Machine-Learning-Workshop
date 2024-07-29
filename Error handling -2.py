try:
    result=int("abc")
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occured {e}")
