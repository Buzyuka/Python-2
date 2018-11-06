import logging
import inspect


def log():
    def decorator(func):
        def inner(*args, **kwargs):
            log = logging.getLogger('app.main')
            parent = inspect.getouterframes(inspect.currentframe())[1].function
            log.info(f"Функция {func.__name__} вызвана из функции {parent}; аргументы: {args}, {kwargs}")
            return func(*args, **kwargs)

        return inner

    return decorator
