from abc import abstractmethod, ABC


class __CommandAbstract(ABC):
    @abstractmethod
    def command(self, **data) -> list[str]:
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

    def command(self, **data) -> list[str]:
        args: list[str] = []
        for command in self.commands:
            args.append(";")
            args.extend(command.command(**data))

        return args
