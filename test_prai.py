import unittest

from bs4 import BeautifulSoup


class Testing(unittest.TestCase):

    def setUp(self):
        HTML = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">
        <html>
        <head>
        <title>title</title>
        </head>
        <body>
        <div id="main" class="fancy">
        <div id="footer">
        </div>
        """
        xml = """<tag xmlns:ns1="http://namespace1/" xmlns:ns2="http://namespace2/">
         <ns1:child>I'm in namespace 1</ns1:child>
         <ns2:child>I'm in namespace 2</ns2:child>
        </tag> """

        self.soup_html = BeautifulSoup(HTML, 'html.parser')
        self.soup_xml = BeautifulSoup(xml, "xml")

    def assertSelects(self, selector, expected_ids, **kwargs):
        element_ids = [el['id'] for el in self.soup_html.select(selector, **kwargs)]
        element_ids.sort()
        expected_ids.sort()
        self.assertEqual(expected_ids, element_ids,
            "Selector %s, expected [%s], got [%s]" % (
                selector, ', '.join(expected_ids), ', '.join(element_ids)
            )
        )
    def assertSelectsxml(self, selector, expected_ids, **kwargs):
        element_ids = [el['id'] for el in self.soup_xml.select(selector, **kwargs)]
        element_ids.sort()
        expected_ids.sort()
        self.assertEqual(expected_ids, element_ids,
            "Selector %s, expected [%s], got [%s]" % (
                selector, ', '.join(expected_ids), ', '.join(element_ids)
            )
        )
    assertSelectxml = assertSelectsxml

    assertSelect = assertSelects

    def assertSelectMultiple(self, *tests):
        for selector, expected_ids in tests:
            self.assertSelect(selector, expected_ids)

    def test_select_one_tag_one(self):
        """Test-Case that expects ."""
        """Test path [1,2,3,4,5,6,10]"""
        elements = self.soup_html.select('title')
        self.assertEqual(len(elements), 1)
        self.assertEqual(elements[0].name, 'title')
        self.assertEqual(elements[0].contents, ['title'])


    def test_select_elements_with_limit(self):
        """Test-Case that expects ."""
        """Test path [1,2,3,4,6,10]"""
        self.assertSelects('html div', ['main'], limit=1)

    def test_select_namespaced(self):
        """Test-Case that expects ."""
        """Test path [1,2,4,5,6,10]"""
        namespaces = dict(first="http://namespace1/", second="http://namespace2/")
        self.soup_xml.select("child", namespaces=namespaces)
        result=self.soup_xml.select("child", namespaces=namespaces)
        resultsetlist=[]
        for tag in result:
            resultsetlist.append(str(tag))
        self.assertEqual(["<ns1:child>I'm in namespace 1</ns1:child>", "<ns2:child>I'm in namespace 2</ns2:child>"],resultsetlist)

    def test_select_namespaced_with_limit(self):
        """Test-Case that expects ."""
        """Test path [1,2,4,5,6,10]"""
        namespaces = dict(first="http://namespace1/", second="http://namespace2/")
        result=self.soup_xml.select("child", namespaces=namespaces,limit=1)
        resultsetlist=[]
        for tag in result:
            resultsetlist.append(str(tag))
        self.assertEqual(["<ns1:child>I'm in namespace 1</ns1:child>"],resultsetlist)
