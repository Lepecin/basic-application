from abc import abstractmethod, ABC
from .cmd import Script


class __CommandAbstract(ABC):
    @abstractmethod
    def command(self, **data) -> Script:
        pass


class Command(__CommandAbstract):
    name: str | None

    def __init__(self, name: str | None = None) -> None:
        super().__init__()
        self.name = name


class CompoundCommand(Command):
    commands: list[Command]

    def __call__(self, *commands: Command) -> "CompoundCommand":
        self.commands = list(commands)
        return self

    def command(self, **data) -> Script:
        return sum((command.command(**data) for command in self.commands), [])
