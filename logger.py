import logging
from functools import wraps

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def log_call(func):
    """Decorador para registrar llamadas a funciones en un archivo de log.

    Args:
        func (Callable): La función que será decorada.

    Returns:
        Callable: Una nueva función que incluye el registro en logs.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"Llamada a {func.__name__} con args={args}, kwargs={kwargs}")
        return result
    return wrapper