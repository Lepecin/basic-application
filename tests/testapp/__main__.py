from lepapplication import App, get_args
from lepapplication.commands.test import (
    TestOneCommand,
    TestTwoCommand,
    TestThreeCommand,
    Command,
)


class SaveConfigCommand(Command):
    def command(self, **data) -> list[str]:
        data_saved = {
            "greeting": "hello",
            "farewell": "bye",
            **data,
        }
        print(f"Saved data {data_saved}")
        return []


app = App(
    TestOneCommand("one"),
    TestTwoCommand("two"),
    TestThreeCommand("three"),
    SaveConfigCommand("save"),
)
app.get_metadata(**{})


option, data = get_args()
app(option).run(**data)
