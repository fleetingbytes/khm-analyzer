from collections.abc import Callable
from functools import partial, wraps
from typing import Any

from khm_renderer.corrections import default_corrections
from khm_renderer.separators import Separators


def inject_default_separators[R](
    func: Callable[..., R] | None = None, *, kwarg_name: str = "sep"
) -> Callable[..., R]:
    if func is None:
        return partial(inject_default_separators, kwarg_name=kwarg_name)

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> R:
        if kwargs.get(kwarg_name) is None:
            kwargs[kwarg_name] = Separators()
        return func(*args, **kwargs)

    return wrapper


def inject_default_corrections[R](
    func: Callable[..., R] | None = None, *, kwarg_name: str = "corrections"
) -> Callable[..., R]:
    if func is None:
        return partial(inject_default_separators, kwarg_name=kwarg_name)

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> R:
        if kwargs.get(kwarg_name) is None:
            kwargs[kwarg_name] = default_corrections
        return func(*args, **kwargs)

    return wrapper
