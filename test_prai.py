import logging
import unittest

from bs4.testing import (
    default_builder,
    SoupTest
)

try:
    from bs4.builder import LXMLTreeBuilder, LXMLTreeBuilderForXML

    LXML_PRESENT = True
except ImportError as e:
    LXML_PRESENT = False
from bs4 import BeautifulSoup
xml = """<tag xmlns:ns1="http://namespace1/" xmlns:ns2="http://namespace2/">
 <ns1:child>I'm in namespace 1</ns1:child>
 <ns2:child>I'm in namespace 2</ns2:child>
</tag> """
soup = BeautifulSoup(xml, "xml")

soup.select("child")
# [<ns1:child>I'm in namespace 1</ns1:child>, <ns2:child>I'm in namespace 2</ns2:child>]

class BlackBoxTesting(SoupTest):

    def test_find_first_content_of_tag(self):
        """Positive Test-Case that gets first content of tag."""
        soup = self.soup("<x>1</x><y>2</y><x>3</x><y>4</y>")
        soup.select("x","x",1)
        #self.assertEqual(soup.select("x").string, "1")

