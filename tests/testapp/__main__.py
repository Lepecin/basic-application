from ...src.lepapplication.application import App
from ...src.lepapplication.commands import (
    TestOneCommand,
    TestTwoCommand,
    TestThreeCommand,
)


app = App(
    TestOneCommand("one"),
    TestTwoCommand("two"),
    TestThreeCommand("three"),
)

app.get_metadata(greeting="hello", shell=True)

app("three").run(message="yo", farewell="bye")
