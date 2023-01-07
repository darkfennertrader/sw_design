from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class Receiver1:
    def action(self) -> None:
        print("Receiver1.action")


class Receiver2:
    def another_action(self) -> None:
        print("Receiver2.action")


class ConcreteCommand1(Command):
    def __init__(self, receiver: Receiver1) -> None:
        self.receiver = receiver

    def execute(self) -> None:
        print("ConcreteCommand1.execute")
        self.receiver.action()


class ConcreteCommand2(Command):
    def __init__(self, receiver: Receiver2) -> None:
        self.receiver = receiver

    def execute(self) -> None:
        print("ConcreteCommand2.execute")
        self.receiver.another_action()


def main() -> None:
    command1 = ConcreteCommand1(Receiver1())
    command2 = ConcreteCommand2(Receiver2())
    command1.execute()
    command2.execute()


if __name__ == "__main__":
    main()
