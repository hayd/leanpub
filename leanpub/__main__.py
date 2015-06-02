import argh
from subprocess import Popen

from leanpub.watcher import MAKE_BOOK, MAKE_SAMPLE, watch


def book():
    "Build full pdf (from Book.txt)."
    p = Popen(MAKE_BOOK, shell=True)
    p.wait()


def sample():
    "Build sample pdf (from Sample.txt)."
    if not MAKE_SAMPLE:
        return
    p = Popen(MAKE_SAMPLE, shell=True)
    p.wait()


# That's right, I'm overriding all
def all():
    "Build both the full and sample version of the book."
    book()
    sample()


parser = argh.ArghParser()
# TODO work out how to get all to be the default (i.e. without passing args)
parser.add_commands([all, book, sample, watch])

parser.description = "Build leanpub books locally from the command line."


def main():
    parser.dispatch()


if __name__ == '__main__':
    main()

