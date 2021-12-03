import unittest

from bs4 import BeautifulSoup

with open("test.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

class Test(unittest.TestCase):

    pass