import os
import ast
from typing import Any


def get_env(key: str, default: Any = None, required: bool = False) -> str:
    value = None
    try:
        value = os.environ[key]
        return ast.literal_eval(value)
    except KeyError:
        if required and default is None:
            raise RuntimeError(f'Env variable {key} is not set')
        return default
    except (SyntaxError, ValueError):
        return value
