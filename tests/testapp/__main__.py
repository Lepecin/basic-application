from lepapplication import App, get_args
from lepapplication.commands.test import (
    TestOneCommand,
    TestTwoCommand,
    TestThreeCommand,
)


app = App(
    TestOneCommand("one"),
    TestTwoCommand("two"),
    TestThreeCommand("three"),
)
app.get_metadata()


option, data = get_args()
app(option).run(**data)
