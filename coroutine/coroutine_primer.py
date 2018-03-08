from functools import wraps


def coroutine(func):
    """ Forward to next yield """

    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@coroutine
def averager():
    """ Compute Average with Primer

    >>> coro_avg = averager()
    >>> from inspect import getgeneratorstate
    >>> getgeneratorstate(coro_avg)
    'GEN_SUSPENDED'
    >>> coro_avg.send(10)
    10.0
    >>> coro_avg.send(30)
    20.0
    >>> coro_avg.send(5)
    15.0
    """
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count
