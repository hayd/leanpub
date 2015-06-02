# leanpub cli

Build leanpub books locally from the command line.

> Note/Disclaimer: This is not an official Leanpub product, it simply uses
> pandoc to build a pdf from markdown in a similar way to Leanpub. Currently
> the output from leanpub *is different* in style (and this will probably
> always be the case), however I find that it massively speeds up the iteration
> process to be able to build a pdf which looks "similar enough" to Leanpub.

This implements a simple cli for building ebooks locally. Rather than having
upload your new change-set to Dropbox and then trigger leanpub build on
their site - do it all locally.

## Usage

To build the Book (this requires a `Book.txt`):

```sh
$ leanpub book
```

To build the Sample (this requires a `Sample.txt`):

```sh
$ leanpub sample
```

To build both:

```sh
$ leanpub all
```

You can also "watch" for changes in any of the markdown files you are using to
build the book i.e. when a markdown file is saved:

```sh
$ leanpub watch
```

You can get help via the command line with:

```sh
$ leanpub --help
```

## Installation

Install via [pip](https://pip.pypa.io/en/latest/installing.html):

```sh
$ pip install leanpub
```

*Note: if you don't have python installed I recommend
[miniconda](http://conda.pydata.org/miniconda.html); no-admin access required.*

This requires that pandoc is installed, if it's not install it
[here](http://pandoc.org/installing.html).

## Issues / troubleshooting / requests

Please post an [issue on github](https://github.com/hayd/leanpub).

### Going forward

I would like to improve the output to better match leanpub.
Any help it that direction (e.g. css, or prepending the title page) would be
great!

