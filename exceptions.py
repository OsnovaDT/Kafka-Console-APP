"""Custom exceptions."""


class ConfigIncorrectError(Exception):
    def __init__(self, config) -> None:
        super().__init__(f"Config is incorrect: {config}")
