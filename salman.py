from logging import setLogRecordFactory
from typing import Text
import unittest

from bs4 import BeautifulSoup

# HTML From File
with open("salman_sample.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")


class Test_append(unittest.TestCase):
    def test_append_h1(self):
        doc.h1.append(" park")
        self.assertEqual(str(doc.h1),'<h1 id="1">jurassic park</h1>')
    def test_append_title(self):
        doc.title(" movie collection")
class Test_extend(unittest.TestCase):
    def test_extend_id_2(self):
        doc.body.find(id="2").extend([" 1"])
        self.assertEqual(str(doc.find(id="2")),'<h1 id="2">Mission ImPossible 1</h1>')
    def test_extend_id_5(self):
        doc.body.find(id="5").extend([", the fate of furious"])
        self.assertEqual(str(doc.find(id="5")),'<h1 id="5">Fast And Furious, the fate of furious</h1>')
class Test_NavigatableString(unittest.TestCase):
    def test_NavigatableString_h1_id_3(self):
        tag=doc.body.find(id="3")
        self.assertEqual(tag.string,"Mission Possible")
    def test_NavigatableString_h1_id_3_case2(self):
        tag=doc.body.find(id="3")
        self.assertEqual(str(type(tag.string)),"<class 'bs4.element.NavigableString'>")
    def test_NavigatableString_h1_id_3_case3(self):
        tag=doc.body.find(id="3")
        self.assertEqual(str(type(str(tag.string))),"<class 'str'>")
class Test_New_Tag(unittest.TestCase):
    def test_add_newtag_movie(self):
        new_tag=doc.new_tag("b")
        new_tag.string="Block buster movie"
        doc.body.find(id="4").append(new_tag)
        self.assertEqual(str(doc.body.find(id="4")),'<h1 id="4">The Matrix<b>Block buster movie</b></h1>')
class Test_decompose(unittest.TestCase):
    def test_decompose_tag_h2_start(self):
        doc.body.find(id="h2_1").b.decompose()
        self.assertEqual(str(doc.find(id="h2_1")),'<h2 id="h2_1"></h2>')
    def test_decompose_tag_h2_end(self):
        doc.body.find(id="h2_2").i.decompose()
        self.assertEqual(str(doc.find(id="h2_2")),'<h2 id="h2_2"></h2>')



    

        
        


if __name__ == "__main__":
	unittest.main()