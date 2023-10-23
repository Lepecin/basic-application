import pathlib

from .abstract import Command
from .cmd import Script, args_to_script
from .keyconvert import data_to_args


class InterfaceCommand(Command):
    app_path: str

    def __call__(self, app_path: str) -> "InterfaceCommand":
        self.app_path = pathlib.Path(app_path).__str__()
        return self

    def command(self, pypath: str, **data) -> Script:
        if not self.name is None:
            return args_to_script(
                pypath,
                self.app_path,
                self.name,
                *data_to_args(**data),
            )
        else:
            return []
