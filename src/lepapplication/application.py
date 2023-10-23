import subprocess

from .commands import Command


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


class CommandInterface:
    """
    A command interface provides a wrapper for a command object
    for running it and adding extra metadata when initiating it.
    """

    command: Command
    """
    Command for which interface is made.
    """

    metadata: dict[str, str]
    """
    Metadata used to overide input data to the interface.
    """

    def __init__(self, command: Command) -> None:
        self.command = command

    def __call__(self, **metadata) -> "CommandInterface":
        self.metadata = metadata
        return self

    def run(self, **data: str):
        """
        Run the command with the kwargs provided to it.

        data: Kwargs used as an input to the command.
        """

        data.update(self.metadata)

        script = self.command.command(**data)

        for cmd in script:
            subprocess.run(cmd())
