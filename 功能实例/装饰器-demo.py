import functools

'''
    @functools.wraps(func)，这是python提供的装饰器。它能把原函数的元信息拷贝到装饰器里面的 func 函数中。
    函数的元信息包括docstring、name、参数列表等等
    可以尝试去除@functools.wraps(func)，你会发现test.__name__的输出变成了wrapper。
    
'''

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        print('args = {}'.format(*args))
        print('加入自己的操作')
        return func(*args, **kwargs)

    return wrapper


@log
def test(p):
    print(test.__name__ + " param: " + p)

test("I'm a param")