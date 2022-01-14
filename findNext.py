from os import pipe2
import unittest

from bs4 import BeautifulSoup

with open("alex.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")


class TestFindNext(unittest.TestCase):
    def test_find_next_none(self):
        """When no next exists should return None"""
        deepest_p2_string = soup.find(string="Hi there!")
        self.assertEqual(deepest_p2_string.find_next(), None)

    def test_find_next_one(self):
        """When not given parameters should return the the closest match"""
        p3 = soup.find_all('p')[2]
        a2 = soup.find_all('a')[1]
        div1 = soup.find('div')
        div2 = soup.find_all('div')[1]
        self.assertEqual(p3.find_next(), a2)
        self.assertEqual(a2.find_next(), div1)
        self.assertEqual(div1.find_next(), div2)

    def test_find_next_specific(self):
        """When given specific parameters, should return the next match with those parameters"""
        a1 = soup.find_all('a')[0]
        a2 = soup.find_all('a')[1]
        div1 = soup.find('div')
        div2 = soup.find_all('div')[1]
        self.assertEqual(a1.find_next('a'), a2)
        self.assertEqual(a1.find_next('div'), div1)

class TestFindAllNext(unittest.TestCase):
    def test_find_all_next_none(self):
        """When no next exists, should return an empty list []"""
        deepest_p2_string = soup.find(string="Hi there!")
        self.assertEqual(deepest_p2_string.find_all_next(), [])
    
    def test_find_all_next_many(self):
        """All next should return a list of all next matches"""
        div1 = soup.find('div')
        div2 = soup.find_all('div')[1]
        p4 = soup.find_all('p')[3]
        p5 = soup.find_all('p')[4]
        self.assertEqual(div1.find_all_next(), [div2,p4,p5])
        self.assertEqual(p4.find_all_next(), [p5])

    def test_find_all_next_specific(self):
        """When called with parameters should return a list of next matches with those parameters"""
        p1 = soup.find('p')
        div1 = soup.find('div')
        div2 = soup.find_all('div')[1]
        p4 = soup.find_all('p')[3]
        p5 = soup.find_all('p')[4]
        self.assertEqual(p1.find_all_next('div'),[div1,div2])
        self.assertEqual(div1.find_all_next('p'),[p4,p5])

if __name__ == '__main__':
    unittest.main()