class CustomException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        return 'please enter the number less then 1000. custom exception raised'



n = int(input('Please enter the number less then 1000 '))

if n > 1000:
    raise CustomException("oops!")
else:
    print('Successfully done!')