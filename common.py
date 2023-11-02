from typing import Callable

from config import logger


def describer(func: Callable):
    def wrapper(*args, **kwargs):
        logger.info(f"Выполняется функция {func.__name__}")
        logger.info(f"Аргументы: {args}\n{kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Функция {func.__name__} выполнена")
        return result

    return wrapper
