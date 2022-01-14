from os import pipe2
import unittest

from bs4 import BeautifulSoup

with open("alex.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")


class TestFindPreviousSibling(unittest.TestCase):
    """If no sibling exists it should return None"""
    def test_find_previous_sibling_none(self):
        deepest_p1 = soup.find_all('p')[3]
        deepest_p2 = soup.find_all('p')[4]
        self.assertEqual(deepest_p1.find_previous_sibling(), None)
        self.assertEqual(deepest_p2.find_previous_sibling('title'), None)

    def test_find_previous_sibling_blank(self):
        """When calling with no arguments, should return the closest previous sibling, if there is one"""
        h1 = soup.find("h1")
        p1 = soup.find_all('p')[0]
        p2 = soup.find_all('p')[1]
        self.assertEqual(p1.find_previous_sibling(), h1)
        self.assertEqual(p2.find_previous_sibling(), p1)

    def test_find_previous_sibling_specific(self):
        """When calling with argument, find the previous sibling of that type"""
        h1 = soup.find('h1')
        p2 = soup.find_all('p')[1]
        p3 = soup.find_all('p')[2]
        self.assertEqual(p2.find_previous_sibling('h1'),h1)
        self.assertEqual(p3.find_previous_sibling('p'),p2)

class TestFindPreviousSiblings(unittest.TestCase):
    def test_find_previous_siblings_none(self):
        """When no previous siblings with correct parameters exist it should return []"""
        div2 = soup.find_all('div')[1]
        self.assertEqual(div2.find_previous_siblings(), [])
        p5 = soup.find_all('p')[4]
        self.assertEqual(p5.find_previous_siblings('div'), [])
    
    def test_find_previous_siblings_one(self):
        """When only one previous sibling with correct parameters exist, return that one only"""
        h1 = soup.find('h1')
        p1 = soup.find_all('p')[0]
        p2 = soup.find_all('p')[1]
        self.assertEqual(p1.find_previous_siblings(), [h1])
        self.assertEqual(p2.find_previous_siblings('p'), [p1])

    def test_find_previous_siblings_many(self):
        """Test for more than one previous sibling"""
        h1 = soup.find('h1')
        p1 = soup.find('p')
        p2 = soup.find_all('p')[1]
        p3 = soup.find_all('p')[2]
        div1 = soup.find('div')
        self.assertEqual(div1.find_previous_siblings(), [p3,p2,p1,h1])
        self.assertEqual(p3.find_previous_siblings(), [p2,p1,h1])
        self.assertEqual(p3.find_previous_siblings('p'), [p2,p1])


if __name__ == '__main__':
    unittest.main()