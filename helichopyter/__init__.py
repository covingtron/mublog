from collections.abc import Callable
from typing import Any

definitions: list[tuple[Any, ...]] = []


class _TerraformPlaceholder:
    def __getattr__(self, name: str) -> str:
        if name == 'string':
            return 'string'
        if name == 'workspace':
            return 'terraform.workspace'
        return f'terraform.{name}'


terraform = _TerraformPlaceholder()


class _LocalPlaceholder:
    def __getattr__(self, name: str) -> str:
        return f'local.{name}'


local = _LocalPlaceholder()


class _VarPlaceholder:
    def __getattr__(self, name: str) -> str:
        return f'var.{name}'


var = _VarPlaceholder()


def required_providers(**kwargs: Any) -> None:
    definitions.append(('terraform', 'required_providers', kwargs))


def provider(name: str, **kwargs: Any) -> None:
    definitions.append(('provider', name, kwargs))


def locals(**kwargs: Any) -> None:  # noqa: A001
    definitions.append(('locals', kwargs))


def resource(type_: str, name: str) -> Callable[..., None]:
    def inner(*args: Any, **kwargs: Any) -> None:
        definitions.append(('resource', type_, name, args, kwargs))

    return inner


def data(type_: str, name: str) -> Callable[..., None]:
    def inner(**kwargs: Any) -> None:
        definitions.append(('data', type_, name, kwargs))

    return inner


def variable(name: str) -> Callable[..., None]:
    def inner(**kwargs: Any) -> None:
        definitions.append(('variable', name, kwargs))

    return inner


def output(name: str) -> Callable[..., None]:
    def inner(**kwargs: Any) -> None:
        definitions.append(('output', name, kwargs))

    return inner


def provisioner(type_: str) -> Callable[..., dict[str, Any]]:
    def inner(**kwargs: Any) -> dict[str, Any]:
        return {'_provisioner': type_, 'args': kwargs}

    return inner


class _Block:
    def __init__(self, name: str, contents: dict[str, Any]) -> None:
        self._name = name
        self._contents = contents


def block(name: str, **kwargs: Any) -> _Block:
    return _Block(name, kwargs)
