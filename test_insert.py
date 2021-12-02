import unittest

from bs4 import BeautifulSoup

	# HTML From File
with open("index.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")
print(doc.prettify())


class Test(unittest.TestCase):


	def test_insert(self):
		doc.h2.insert(1, " that has been appended!")
		self.assertEqual(str(doc.h2), "<h2>This is a Medium Header that has been appended!</h2>")
		doc.h2.insert(0, "Hej!")
		self.assertEqual(str(doc.h2), "<h2>Hej!This is a Medium Header that has been appended!</h2>")
		doc.h2.insert(1, " ")
		self.assertEqual(str(doc.h2), "<h2>Hej! This is a Medium Header that has been appended!</h2>")
		doc.h2.insert(5, "!!")
		self.assertEqual(str(doc.h2), "<h2>Hej! This is a Medium Header that has been appended!!!</h2>")

	def test_clear(self):
		markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
		soup = BeautifulSoup(markup, 'html.parser')
		tag = soup.a
		tag.clear()
		self.assertEqual(str(tag), "<a href=\"http://example.com/\"></a>")
		markup_2 = '<p><b>Hello</b> World<b>!</b> </p>'
		soup_2 = BeautifulSoup(markup_2, 'html.parser')
		tag_2 = soup_2.b
		tag_2.clear()
		self.assertEqual(str(tag_2), "<b></b>")
		tag_3 = soup_2.p
		tag_3.clear()
		self.assertEqual(str(tag_3), "<p></p>")

if __name__ == "__main__":
	unittest.main()
