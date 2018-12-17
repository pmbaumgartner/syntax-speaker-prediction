import prodigy
from prodigy.components.loaders import JSONL


@prodigy.recipe("audio-choice")
def audio_annotation(dataset, source):
    stream = JSONL(source)
    stream = add_options(stream)
    stream = list(stream)
    return {
        "dataset": dataset,
        "stream": stream,
        "view_id": "choice",
        "progress": progress,
    }


def add_options(stream):
    """Helper function to add options to every task in a stream."""
    options = [
        {"id": "scott", "text": "🤪🐂 Scott"},
        {"id": "wes", "text": "🦈 Wes"},
        {"id": "other", "text": "⛔️ other"},
    ]
    for task in stream:
        task["options"] = options
        yield task


def progress(session_count, total):
    custom_progress = session_count / total
    return custom_progress
