from text.commands import AppendText, Batch, ChangeTitle, Clear
from text.controller import TextController
from text.processor import Processor


def main() -> None:

    # create a processor
    processor = Processor()

    # create a text controller
    controller = TextController()

    # create some documents
    doc1 = processor.create_document("ArjanCodes")
    doc2 = processor.create_document("Meeting Notes")

    # append some text to the documents
    controller.execute(AppendText(doc1, "Hello World!"))
    controller.execute(AppendText(doc2, "The meeting started at 9:00."))

    # update the title of the first document
    controller.execute(ChangeTitle(doc1, "Important Meeting"))
    controller.undo()

    print(processor)

    # execute a batch of commands
    controller.execute(
        Batch(
            commands=[
                AppendText(doc1, "Hello World!"),
                ChangeTitle(doc2, "Useless Meeting."),
                Clear(doc2),
            ]
        )
    )

    print(processor)

    # # undo
    controller.undo()
    print(processor)


if __name__ == "__main__":
    main()
