from watchdog.observers import Observer
from watchdog.watchmedo import observe_with

from leanpub.shellcommandtrick import ShellCommandTrick


def pandoc_cmd(book):
    """Create the command to convert the files (listed in `book`)
    into a pdf. This is wrapped with echos that the build has started and
    is complete."""
    with open(book + ".txt") as f:
        return ('echo "Starting build of {book}.pdf"'
                " && pandoc {files} "
                "--smart --table-of-contents --chapters -o {book}.pdf"
                ' && echo "  {book}.pdf created."'
                ).format(book=book,
                         files=f.read().replace("\n", " "))

try:
    MAKE_BOOK = pandoc_cmd("Book")
except IOError:
    print("Can't find Book.txt in directory.")
    exit(1)

try:
    MAKE_SAMPLE = pandoc_cmd("Sample")
except IOError:
    # Sample.txt is optional.
    MAKE_SAMPLE = ""

# TODO watch images
PATTERNS = ["*.markdown", "*.md", "Book.txt", "Sample.txt"]
DIRECTORIES = "."
RECURSIVE = False

TIMEOUT = 1.0


def watch():
    """Watch for changes to the markdown files, and build the book and the
    sample pdf upon each change."""
    handler = ShellCommandTrick(shell_command=MAKE_BOOK + " && " + MAKE_SAMPLE,
                                patterns=PATTERNS,
                                terminate_on_event=True)
    observer = Observer(timeout=TIMEOUT)
    observe_with(observer, handler, DIRECTORIES, RECURSIVE)
