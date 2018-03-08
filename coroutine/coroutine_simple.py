def simple_coroutine():
    """ A simplest coroutine example

    >>> my_coro = simple_coroutine()
    >>> my_coro
    <generator object simple_coroutine at 0x104669240>
    >>> next(my_coro)
    -> Coroutine started
    >>> my_coro.send(42)
    -> Coroutine received: 42
    Traceback (most recent call last): # ➏
        ...
    StopIteration

    >>> my_coro = simple_coroutine()
         >>> my_coro.send(1729)
         Traceback (most recent call last):
           File "<stdin>", line 1, in <module>
         TypeError: can't send non-None value to a just-started generator
    """
    print('Coroutine started')
    while True:
        x = yield                           # Wait for a value from send()
        print('-> coroutine recieved:', x)


def simple_coroutine2(a):
    """ Coroutine with 2 values

    >>> my_coro2 = simple_coro2(14)
         >>> from inspect import getgeneratorstate
    >>> getgeneratorstate(my_coro2)
    'GEN_CREATED'
    >>> next(my_coro2)
    -> Started: a = 14
    14
    >>> getgeneratorstate(my_coro2)
    'GEN_SUSPENDED'
    >>> my_coro2.send(28)
    -> Received: b = 28
    42
    >>> my_coro2.send(99)
    -> Received: c = 99
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module> StopIteration
    >>> getgeneratorstate(my_coro2)
    'GEN_CLOSED'
    """
    print('-> Started: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)
