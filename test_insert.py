import unittest

from bs4 import BeautifulSoup

# HTML From File
with open("test.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")


class Test(unittest.TestCase):
	
	def test(self):
		self.assertEqual(doc.head.title.text,'Hamza Book Collection')
	def test_find_tags_and_change_name(self):
		self.assertEqual(len(doc.find_all("h1")),3)
		doc.h1.name="blockquote"
		self.assertEqual(len(doc.find('blockquote')),1)
	def test_find_parent(self):
		string_=doc.find(string='This is another line at the end')
		self.assertEqual(string_.find_parent().name,"h2")
	def test_find_next_siblings(self):
		self.assertEqual(len(doc.h1.find_next_siblings('h1')),2)
	def test_find_previous_siblings(self):
		self.assertEqual(len(((doc.find('h1',id="3").find_previous_siblings('h1')))),2)
	def test_wrap_tag(self):
		doc.h1.wrap(doc.new_tag("div"))
		self.assertEqual(len(doc.find('div')),1)
	

	




	



	
		# self.assertEqual(doc.find_parent(),)
		
		# self.assertEqual(doc.find_parent('h1'),'p')

		# doc.h2.insert(1, " that has been appended!")
		# self.assertEqual(str(doc.h2), "<h2>This is a Medium Header that has been appended!</h2>")
		# doc.h2.insert(0, "Hej!")
		# self.assertEqual(str(doc.h2), "<h2>Hej!This is a Medium Header that has been appended!</h2>")
		# doc.h2.insert(1, " ")
		# self.assertEqual(str(doc.h2), "<h2>Hej! This is a Medium Header that has been appended!</h2>")
		# doc.h2.insert(5, "!!")
		# self.assertEqual(str(doc.h2), "<h2>Hej! This is a Medium Header that has been appended!!!</h2>")


if __name__ == "__main__":
	unittest.main()
