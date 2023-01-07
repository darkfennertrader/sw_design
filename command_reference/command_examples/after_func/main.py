from functools import partial

from text.commands import append_text, batch, change_title, clear_text
from text.processor import Processor


def main() -> None:

    # create a processor
    processor = Processor()

    # create some documents
    doc1 = processor.create_document("ArjanCodes")
    doc2 = processor.create_document("Meeting Notes")

    print(processor)

    # append some text to the documents
    undo_append = append_text(doc1, "Hello World!")
    append_text(doc2, "The meeting started at 9:00.")

    # update the title of the first document
    undo_title_change = change_title(doc1, "Important Meeting")

    print(processor)

    # undo things
    undo_append()
    undo_title_change()

    print(processor)

    # execute a batch of commands
    undo_batch = batch(
        [
            partial(append_text, doc1, "Hello World!"),
            partial(change_title, doc1, "Useless Meeting"),
            partial(clear_text, doc2),
        ]
    )

    print(processor)

    # undo
    undo_batch()

    print(processor)


if __name__ == "__main__":
    main()
