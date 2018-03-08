def simple_coroutine():
    print('Coroutine started')
    x = yield           # Wait for a value from send()
    print('-> coroutine recieved:', x)


if __name__ == '__main__':
    my_coro = simple_coroutine()
    print(my_coro)
    next(my_coro)       # Execute to yield
    my_coro.send(42)    # Will trigger a Stop Iteration Error
