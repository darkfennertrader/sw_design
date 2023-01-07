from typing import Protocol


class Edit(Protocol):
    def execute(self) -> None:
        """Execute an edit operation."""

    def undo(self) -> None:
        """Undo the edit operation."""
