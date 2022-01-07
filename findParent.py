from os import pipe2
import unittest

from bs4 import BeautifulSoup

with open("alex.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

class TestFindAll(unittest.TestCase):
    def test_find_all_nothing(self):
        """When nothing is to be found, find all should return and empty array"""
        self.assertEqual(soup.find_all('h2'), [])
    
    def test_find_all_one(self):
        """Making sure find all only finds one thing when there only is one thing to find"""
        self.assertEqual(len(soup.find_all('head')), 1)
        self.assertEqual(soup.find_all('h1')[0].string, 'A Sample HTML Document (Test File)')
    
    def test_find_all_many(self):
        """Making sure find all finds all the things it can find"""
        self.assertEqual(len(soup.find_all('meta')), 4)
        self.assertEqual(soup.find_all('p')[2].string, 'Read the HTML5 download attribute guide')
    
    def test_find_all_limit(self):
        """Making sure limit works together with find all"""
        self.assertEqual(len(soup.find_all('meta', limit=0)),[])
        self.assertEqual(len(soup.find_all('meta', limit=1)),1)
        self.assertEqual(soup.find_all('a', limit=1)[0].string, 'Go back to the demo')


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


class TestFindNextSibling(unittest.TestCase):
    def test_find_next_sibling_none(self):
        """If no sibling exists it should return None"""
        deepest_p1 = soup.find_all('p')[3]
        deepest_p2 = soup.find_all('p')[4]
        self.assertEqual(deepest_p1.find_next_sibling('div'), None)
        self.assertEqual(deepest_p2.find_next_sibling(), None)
    
    def test_find_next_sibling_blank(self):
        """When calling with no arguments, should return the closest next sibling, and if there are none, returns none"""
        p2 = soup.find_all('p')[1]
        p3 = soup.find_all('p')[2]
        div1 = soup.find('div')
        self.assertEqual(p2.find_next_sibling(), p3)
        self.assertEqual(p3.find_next_sibling(), div1)
        self.assertEqual(div1.find_next_sibling(), None)
    
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
        """When only one sibling with correct parameters exist, return that one only"""
        p2 = soup.find_all('p')[1]
        p3 = soup.find_all('p')[2]
        div1 = soup.find('div')
        self.assertEqual(p2.find_next_siblings('p'),[p3])
        self.assertEqual(p3.find_next_siblings(),[div1])

    def test_find_next_siblings_all(self):
        """Test for more than one sibling"""
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