from pdb import set_trace
import logging
import os
import unittest
import sys
import tempfile

from bs4 import (
    BeautifulSoup,
    BeautifulStoneSoup,
    GuessedAtParserWarning,
    MarkupResemblesLocatorWarning,
)
from bs4.builder import (
    TreeBuilder,
    ParserRejectedMarkup,
)
from bs4.element import (
    CharsetMetaAttributeValue,
    Comment,
    ContentMetaAttributeValue,
    SoupStrainer,
    NamespacedAttribute,
    Tag,
    NavigableString,
)

import bs4.dammit
from bs4.dammit import (
    EntitySubstitution,
    UnicodeDammit,
)
from bs4.testing import (
    default_builder,
    SoupTest
)

try:
    from bs4.builder import LXMLTreeBuilder, LXMLTreeBuilderForXML

    LXML_PRESENT = True
except ImportError as e:
    LXML_PRESENT = False


class BlackBoxTesting(SoupTest):

    def test_find_first_content_of_tag(self):
        """Positive Test-Case that gets first content of tag."""
        soup = self.soup("<x>1</x><y>2</y><x>3</x><y>4</y>")
        self.assertEqual(soup.find("x").string, "1")

    def test_find_all_tag_by_tag_name(self):
        """Positive Test-Case that finds all tags for given tag name and list them."""
        soup = self.soup("<h1>prashanna</h1><h1>rai</h1>")
        result=soup.find_all("h1")
        resultsetlist=[]
        for tag in result:
            resultsetlist.append(str(tag))
        self.assertEqual(['<h1>prashanna</h1>', '<h1>rai</h1>'], resultsetlist)
        self.assertEqual(2, len(result))
        soup.select()

    def test_find_all_using_limit(self):
        """Test case that test number of items for matching tag using limit """
        soup = self.soup("<h1>prashanna</h1><h1>rai</h1><h1>rai1</h1>")
        result= soup.find_all('h1', limit=2)
        resultsetlist=[]
        for tag in result:
            resultsetlist.append(str(tag))
        self.assertEqual(['<h1>prashanna</h1>', '<h1>rai</h1>'], resultsetlist)
        self.assertEqual(2, len(result))
