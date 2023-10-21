from abc import abstractmethod, ABC


class __CommandAbstract(ABC):
    @abstractmethod
    def args(self) -> list[str]:
        pass

    @abstractmethod
    def paramters(self, **data):
        pass


class Command(__CommandAbstract):
    name: str

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name
