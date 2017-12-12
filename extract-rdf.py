#!/usr/bin/env python3
#
# Parses gutenberg.org RDF files into JSON format.

import argparse
import json
import re
from lxml import etree


NAMESPACES = {
    'dcterms': 'http://purl.org/dc/terms/',
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'pgterms': 'http://www.gutenberg.org/2009/pgterms/',
}

EXTRACTORS = [
    {
        'key': 'language',
        'xpath': './/dcterms:language//rdf:value',
        'xform': lambda node: node.text,
        'first': True,
    },
    {
        'key': 'title',
        'xpath': './/dcterms:title',
        'xform': lambda node: node.text,
        'first': True,
    },
    {
        'key': 'author',
        'xpath': './/dcterms:creator//pgterms:name',
        'xform': lambda node: node.text,
        'first': True,
    },
    {
        'key': 'url',
        'xpath': './/pgterms:file/@rdf:about',
        'xform': lambda node: node,
        'filter': lambda item: re.match(r'.*\d+\.zip', item)
    },
]
'''Each "action" defines how a piece of data is extracted from an RDF file
and transformed to JSON.

Properties:
  key       [string]    Target JSON property name.
  xpath     [string]    Target RDF nodes, conforming to `lxml.xpath`.
  xform     [function]  Transformation applied to nodes satisfying xpath.
  filter    [function]  (Optional) Selects elements from xform-ed nodes.
  first     [boolean]   (Optional) Replaces list with first element (or None).
'''


def extract(node, key, xpath, xform, **kwargs):
    '''Applies an EXTRACTOR action to the input node, returning a list of
    key-value pairs.
    '''
    filter_ = kwargs.get('filter')
    data = list(filter(filter_,
        map(xform, node.xpath(xpath, namespaces=NAMESPACES))))
    if kwargs.get('first', False):
        data = (data + [None])[0]
    return (key, data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help='xml:base="http://www.gutenberg.org/"')
    args = parser.parse_args()

    root = etree.parse(args.infile)
    data = dict([extract(root, **kwargs) for kwargs in EXTRACTORS])
    print(json.dumps(data))
