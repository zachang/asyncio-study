def first_coroutine(pattern):
    print(f"Looking for ... {pattern}")
    while True:
        line = (yield) # yield expression
        if pattern in line:
            print(line)

_coroutine = first_coroutine("python")
next(_coroutine) # Priming
_coroutine.send("Yeah, but no, but yeah, but no")
_coroutine.send("A series on pythonistas")
_coroutine.send("A series of tubes")
_coroutine.send("python generators rock!")