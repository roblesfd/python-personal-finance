import logging
from functools import wraps
import time
from typing import List, Any, Callable

logging.basicConfig(
    filename="static/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def truncate(args: List[Any], max_items=4) -> List[Any]:
    """Trunca listas/dicts grandes para mostrar solo los primeros `max_items`."""
    if isinstance(args, list):
        if len(args) > max_items:
            return args[:max_items] + [f"... (+{len(args) - max_items} más)"]
        return args
    return args


def log_call(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorador para registrar llamadas a funciones en un archivo de log.

    Args:
        func (Callable): La función que será decorada.

    Returns:
        Callable: Una nueva función que incluye el registro en logs.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        truncated_args = tuple(truncate(a) for a in args)
        truncated_kwargs = {k: truncate(v) for k, v in kwargs.items()}

        logger.info(f"Llamada a {func.__name__} con args={truncated_args}, kwargs={truncated_kwargs}")
        return result
    return wrapper


def log_error(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.exception(f"Error en {func.__name__}: {e}")
            raise 
    return wrapper


def log_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """Logger de rendimiento, mide el tiempo de ejecución de funciones

    Args:
        func (Callable): Función a decorar/envolver

    Returns:
        Callable: Función envoltorio
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start 
        logger.info(f"func.__name__ tardó {duration:.4f}s")

        return result 

    return wrapper 