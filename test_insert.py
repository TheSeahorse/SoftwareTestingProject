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


if __name__ == "__main__":
	unittest.main()
