from os import pipe2
import unittest

from bs4 import BeautifulSoup

with open("alex.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

class TestFindParent(unittest.TestCase):
    def test_find_parent_none(self):
        """Finding things that don't exist should return None"""
        deepest_p1_string = soup.find(string='Hello')
        self.assertEqual(deepest_p1_string.find_parent('h1'), None)
        head = soup.find('head')
        self.assertEqual(head.find_parent('body'), None)
    
    def test_find_parent_blank(self):
        """Calling find_parent() without argument should return closest parent"""
        p1_string = soup.find(string='A blank HTML document for testing purposes.')
        self.assertEqual(p1_string.find_parent().string, 'A blank HTML document for testing purposes.')
        head = soup.find('head')
        title = soup.find('title')
        self.assertEqual(title.find_parent(),head)
    
    def test_find_parent_multiple(self):
        """Finding parent when there are multiple that fit results in the closest parent"""
        hello = soup.find(string='Hello')
        div2 = soup.find_all('div')[1]
        self.assertEqual(hello.find_parent('div'), div2)


class TestFindParents(unittest.TestCase):
    def test_find_parents_none(self):
        """Making sure find parents can't find items out of range"""
        h1 = soup.find('h1')
        self.assertEqual(h1.find_parents('div'), [])
        self.assertEqual(h1.find_parents('title'), [])
        self.assertEqual(h1.find_parents('p'), [])

    def test_find_parents_one(self):
        """Finding a single item"""
        h1 = soup.find('h1')
        self.assertEqual(len(h1.find_parents('body')), 1)
        second_a = soup.find_all('a')[1]
        self.assertEqual(len(second_a.find_parents('p')), 1)
        self.assertEqual(second_a.find_parents('p')[0].string, 'Read the HTML5 download attribute guide')

    def test_find_parents_all(self):
        """Finding all parents"""
        first_a = soup.find('a')
        self.assertEqual(len(first_a.find_parents()), 3)
        title_string = soup.find(string="A Sample HTML Document (Test File)")
        self.assertEqual(len(title_string.find_parents()), 3)
        head = soup.find('head')
        self.assertEqual(len(head.find_parents()),1)

if __name__ == '__main__':
    unittest.main()
