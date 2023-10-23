from .commands import Command
from .interface import CommandInterface


class App:
    """
    Factory object of command interfaces.
    """

    commands: list[Command]
    """
    List of command objects that can be dispatched by the app.
    """

    metadata: dict[str, str]
    """
    Dictionary of metadata to be used in the app.
    """

    def __init__(self, *commands: Command) -> None:
        self.commands = list(commands)

    def get_metadata(self, **metadata: str):
        self.metadata = metadata

    def command_dict(self) -> dict[str, Command]:
        return {
            command.name: command
            for command in self.commands
            if not command.name is None
        }

    def __call__(self, method: str):
        command = self.command_dict()[method]
        return CommandInterface(command)(**self.metadata)
