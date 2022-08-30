import inspect

from rich.console import RenderableType

__all__ = ["log", "panic"]


def log(*args: object, verbosity: int = 0, **kwargs) -> None:
    # TODO: There may be an early-out here for when there is no endpoint for logs
    from ._context import active_app

    app = active_app.get()

    caller = inspect.stack()[1]
    app.log(*args, verbosity=verbosity, _textual_calling_frame=caller, **kwargs)


def panic(*args: RenderableType) -> None:
    from ._context import active_app

    app = active_app.get()
    app.panic(*args)
