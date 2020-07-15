import functools


def say_hello(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('hello!')
        return func(*args, **kwargs)
    return wrapper



def say_goodbye():
    print('hello!')

@say_hello
def goInto():
    print("我需要找一本达芬芬的书··············")

if __name__ == '__main__':
    goInto()