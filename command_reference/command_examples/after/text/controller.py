from dataclasses import dataclass, field

from .edit import Edit


@dataclass
class TextController:
    undo_stack: list[Edit] = field(default_factory=list)

    def execute(self, edit: Edit) -> None:
        edit.execute()
        self.undo_stack.append(edit)

    def undo(self) -> None:
        if not self.undo_stack:
            return
        edit = self.undo_stack.pop()
        edit.undo()

    def undo_all(self) -> None:
        while self.undo_stack:
            self.undo()
