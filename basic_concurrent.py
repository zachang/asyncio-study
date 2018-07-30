def coroutine_decorator(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start

def natural_numbers(*targets):
    try:
        number = int(input("Enter any natural numer > 1:"))
        if number < 1:
            print("Please enter a number greater than one")
            return natural_numbers(*targets)

        for num in range(1, number):
            targets[0].send(num)
            targets[1].send(num)
    except ValueError:
        print("Wrong input, enter valid integer")
        return natural_numbers(*targets)


@coroutine_decorator
def check_number_kind(next_target):
    """Sorts numbers into even, odd, odd-prime and even-prime"""
    while True:
        number = (yield)
        if number < 2 and number % 2 != 0:  
            next_target.send(f"{number} is an odd number")
        elif number % 2 == 0 and number == 2:
            next_target.send(f"{number} is an even and a prime number ")
        elif number % 2 == 0:
            next_target.send(f"{number} is an even number")
        else: 
            for num in range(2, number):
                if number % num != 0:
                    next_target.send(f"{number} is an odd and a prime number")
                    break


@coroutine_decorator
def output_number_kind():
    """Outputs values from check_number_kind function"""
    try:
        while True:
            line = (yield)
            print(line)
    except GeneratorExit:
        print("Done. Goodbye")


@coroutine_decorator
def sum_numbers(next_target):
    """Calculates sum of numbers in a range"""
    summation = 0
    while True:
        number = (yield)
        summation = summation + number
        next_target.send(summation)


@coroutine_decorator
def output_sum():
    """Outputs sum of numbers from sum_number function"""

    try:
        while True:
            line = (yield)
            print({'summation': line})
    except GeneratorExit:
        print("Done. Goodbye")

if __name__ == "__main__":
    natural_numbers(check_number_kind(output_number_kind()),
                     sum_numbers(output_sum())
                    )