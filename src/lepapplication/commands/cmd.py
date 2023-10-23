class CMD:
    args: list[str]

    def __init__(self, *args: str) -> None:
        self.args = list(args)

    def __call__(self) -> list[str]:
        return self.args


Script = list[CMD]


def args_to_script(*args: str) -> Script:
    return [CMD(*args)]
