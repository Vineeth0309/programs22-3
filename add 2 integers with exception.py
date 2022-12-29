try:
    k=int(input("Enter First Value: "))
    j=int(input("Enter Second Value: "))
    d=k/j
    print(d)
except ValueError as e:
    print('Pls Input Integer Only',e)
except ZeroDivisionError as e:
    print('Second Number Should Not Be Zero',e)
except Exception as e:
    print('Other Error',e)
