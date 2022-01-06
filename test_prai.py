import unittest

from bs4 import BeautifulSoup

xml = """<tag xmlns:ns1="http://namespace1/" xmlns:ns2="http://namespace2/">
 <ns1:child>I'm in namespace 1</ns1:child>
 <ns2:child>I'm in namespace 2</ns2:child>
</tag> """
soup = BeautifulSoup(xml, "xml")

class Testing(unittest.TestCase):
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

    def setUp(self):
        self.soup = BeautifulSoup(self.HTML, 'html.parser')

    def assertSelects(self, selector, expected_ids, **kwargs):
        el_ids = [el['id'] for el in self.soup.select(selector, **kwargs)]
        el_ids.sort()
        expected_ids.sort()
        self.assertEqual(expected_ids, el_ids,
            "Selector %s, expected [%s], got [%s]" % (
                selector, ', '.join(expected_ids), ', '.join(el_ids)
            )
        )

    assertSelect = assertSelects

    def assertSelectMultiple(self, *tests):
        for selector, expected_ids in tests:
            self.assertSelect(selector, expected_ids)

    def test_one_tag_one(self):
        # 1,2,3,4,5,6,10
        els = self.soup.select('title')
        self.assertEqual(len(els), 1)
        self.assertEqual(els[0].name, 'title')
        self.assertEqual(els[0].contents, ['title'])


    def test_limit(self):
        # 1,2,3,4,6,10
        self.assertSelects('html div', ['main'], limit=1)
    # #attrs = {"class": "sister"}

    def test_find_by_namespaced_name(self):
        #[1,2,4,5,6,10]
        namespaces = dict(first="http://namespace1/", second="http://namespace2/")
        soup.select("second|child", namespaces=namespaces)
    def test_find_by_namespaced_name1(self):
        #[1, 2, 4, 5, 6, 10]
        namespaces = dict(first="http://namespace1/", second="http://namespace2/")
        soup.select("second|child", namespaces=namespaces,limit=1)

