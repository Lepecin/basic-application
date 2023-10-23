from lepapplication import Command, CompoundCommand


class TestOneCommand(Command):
    def command(self, message: str, **data) -> list[str]:
        print(f"Running command: {self.__class__.__name__}")
        print(f"This command prints message one: {message}")
        print(f"Additional arguments include:")
        for key, value in data.items():
            print(key, value)
        return []


class TestTwoCommand(Command):
    def command(self, **data) -> list[str]:
        print(f"Running command: {self.__class__.__name__}")
        print("A dull command :)")
        return []


class TestThreeCommand(CompoundCommand):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        super().__call__(
            TestOneCommand(),
            TestTwoCommand(),
        )
