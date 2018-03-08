def simple_coroutine():
    """ A simplest corotine example

    >>> my_coro = simple_coroutine()
    >>> print(my_coro)
    >>> next(my_coro)                       # Execute to yield
    >>> my_coro.send(42)                    # Will trigger a Stop Iteration Error

    """
    print('Coroutine started')
    x = yield                           # Wait for a value from send()
    print('-> coroutine recieved:', x)
