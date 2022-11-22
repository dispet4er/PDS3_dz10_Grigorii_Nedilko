from random import randrange

def unique_values():
    try:
        n = int(input("please enter the maximum number/value of random values to check: "))
        if n < 0:
            raise Exception(f'please enter number that will be > 0')
        list = [randrange(n + n) for i in range(n)]
        for i in list:
            if list.count(i) > 1:
                return False, print("there are NOT only unique values in the list", list)
        return True, print("there are only unique values in the list", list)
    except ValueError as ex3:
        print(f'please enter the number not the text')
    finally:
        print(f'successfully done!')

unique_values()