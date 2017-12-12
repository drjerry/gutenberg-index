# Project Gutenberg index

The texts from Project Gutenberg are ideal for training and validation data
for a NLP research, particularly because there is no restrictive licensing
around its acquisition or usage.

At the end of 2017 there are over 56k texts available. The public "index"
of the archive is a file tree of XML files that can be downloaded from the
[feeds page](http://www.gutenberg.org/wiki/Gutenberg:Feeds).
This resource is problematic for local search and querying, and a couple
open source projects address this:

 1. [gutenberg](https://github.com/c-w/gutenberg) pushes the index into a
    local BSD-DB database, and exposes methods for querying its metadata via
    supplied python scripts.

 3. An [openzim project](https://github.com/openzim/gutenberg) allows one
    to download the entire archive as a ZIM file.

The tools here attempt something much simpler: convert the file tree of XML
into a file of pruned JSON files. Then tools like
[jq-1.5](https://stedolan.github.io/jq/manual/v1.5/)
can be used to query on basically any field.


## Usage

The main script targets Python 3 and requires `lxml` as its only dependency.

    $ virtualenv -p python3 venv
    $ source venv/bin/activate
    $ pip install lxml

The next command will create a `$HOME/gutenberg` folder on your system,
fetch the latest archive index, and extract it to index.jsonl in that folder.

    $ sh index.sh


## License

BSD 2-Clause 
