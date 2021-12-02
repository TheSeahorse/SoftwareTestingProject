import unittest

from bs4 import BeautifulSoup

# HTML From File
with open("test.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")


class Test(unittest.TestCase):
	
	def test1(self):
		self.assertEqual(doc.head.title.text,'Salman Movie Collection')
	def test2(self):
		self.assertEqual(len(((doc.find('h1',id="3").find_all_previous('h1')))),2)
	def test3(self):
		string_=doc.find('h1')
		self.assertEqual(len(string_.find_all_next()),2)
	def test4(self):
		doc.h1.append(' part 1')
		self.assertEqual(doc.h1.text,'jurassic park part 1')
	def test5(self):
		tag=doc.new_tag('i')
		tag.string='New Movies'
		doc.h1.insert_before(tag)
		print(doc.find('i'))
		self.assertEqual(len(doc.find('i')),1)

	

	




	



	
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
