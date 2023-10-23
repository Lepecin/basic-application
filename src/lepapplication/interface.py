import subprocess
from .commands import Command


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
