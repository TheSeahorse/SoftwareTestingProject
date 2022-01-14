from os import pipe2
import unittest

from bs4 import BeautifulSoup

with open("alex.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

class TestFindNextSibling(unittest.TestCase):
    def test_find_next_sibling_none(self):
        """If no sibling exists it should return None"""
        deepest_p1 = soup.find_all('p')[3]
        deepest_p2 = soup.find_all('p')[4]
        self.assertEqual(deepest_p1.find_next_sibling('div'), None)
        self.assertEqual(deepest_p2.find_next_sibling(), None)
    
    def test_find_next_sibling_blank(self):
        """When calling with no arguments, should return the closest next sibling, if there is one"""
        p2 = soup.find_all('p')[1]
        p3 = soup.find_all('p')[2]
        div1 = soup.find('div')
        self.assertEqual(p2.find_next_sibling(), p3)
        self.assertEqual(p3.find_next_sibling(), div1)
    
    def test_find_next_sibling_specific(self):
        """When calling with argument, find the next sibling of that type"""
        p1 = soup.find('p')
        div1 = soup.find('div')
        self.assertEqual(p1.find_next_sibling('div'), div1)


class TestFindNextSiblings(unittest.TestCase):
    def test_find_next_siblings_none(self):
        """When no next siblings with correct parameters exist it should return []"""
        deepest_p1_string = soup.find(string='Hello')
        self.assertEqual(deepest_p1_string.find_next_siblings(), [])
        div1 = soup.find('div')
        self.assertEqual(div1.find_next_siblings(),[])
        first_p = soup.find('p')
        self.assertEqual(first_p.find_next_siblings('h1'),[])

    def test_find_next_siblings_one(self):
        """When only one next sibling with correct parameters exist, return that one only"""
        p2 = soup.find_all('p')[1]
        p3 = soup.find_all('p')[2]
        div1 = soup.find('div')
        self.assertEqual(p2.find_next_siblings('p'),[p3])
        self.assertEqual(p3.find_next_siblings(),[div1])

    def test_find_next_siblings_all(self):
        """Test for more than one next sibling"""
        h1 = soup.find('h1')
        p1 = soup.find('p')
        p2 = soup.find_all('p')[1]
        p3 = soup.find_all('p')[2]
        div1 = soup.find('div')
        self.assertEqual(h1.find_next_siblings(), [p1,p2,p3,div1])
        self.assertEqual(h1.find_next_siblings('p'), [p1,p2,p3])
        self.assertEqual(p1.find_next_siblings('p'), [p2,p3])
        self.assertEqual(p2.find_next_siblings(), [p3,div1])


if __name__ == '__main__':
    unittest.main()