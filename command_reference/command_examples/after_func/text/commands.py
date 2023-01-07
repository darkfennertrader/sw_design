from typing import Callable

from .document import Document

UndoFunction = Callable[[], None]
EditFunction = Callable[[], UndoFunction]


def append_text(doc: Document, text: str) -> UndoFunction:
    def undo():
        doc.text = doc.text[: -len(text)]

    doc.append(text)
    return undo


def clear_text(doc: Document) -> UndoFunction:
    text = doc.text

    def undo():
        doc.text += text

    doc.clear()
    return undo


def change_title(doc: Document, title: str) -> UndoFunction:
    old_title = doc.title

    def undo():
        doc.set_title(old_title)

    doc.set_title(title)
    return undo


def batch(edits: list[EditFunction]) -> UndoFunction:
    undo_fns = [edit() for edit in edits]

    def undo():
        for undo_fn in reversed(undo_fns):
            undo_fn()

    return undo
