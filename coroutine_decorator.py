def coroutine_decorator(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        next(cr)
        return cr
    return start

@coroutine_decorator
def first_coroutine(pattern):
    print(f"Looking for ... {pattern}")
    try:
        while True:
            line = (yield) # yield expression
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("Going away. Goodbye")

_coroutine = first_coroutine("Django")
_coroutine.send("Yeah, but no, but yeah, but no")
_coroutine.send("A series on Django's models")
_coroutine.send("A series of tubes")
_coroutine.send("Django rocks!")