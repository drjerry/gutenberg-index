#!/bin/sh

DEST=$HOME/gutenberg

mkdir -p $DEST
wget -P $DEST http://www.gutenberg.org/cache/epub/feeds/rdf-files.tar.bz2
tar xvfj $DEST/rdf-files.tar.bz2 -C $DEST/

for NODE in $(find $DEST/cache -name "*.rdf")
do
    ./extract-rdf.py $NODE >> $DEST/index.jsonl
done
