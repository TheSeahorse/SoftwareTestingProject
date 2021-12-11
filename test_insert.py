import unittest

from bs4 import BeautifulSoup

	# HTML From File
with open("index.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")
print(doc.prettify())


# Class to test the insert(pos, string) function that inserts a string at a specified location indicated by an index
class TestInsert(unittest.TestCase):

	# Test function to check if the insertion is performed successfully at position 1 of the string
	def test_insert_a(self):
		doc.h2.insert(1, " that has been appended!")
		self.assertEqual(str(doc.h2), "<h2>This is a Medium Header that has been appended!</h2>")

	# Test function to check if the insertion is performed successfully at the first position of the string
	def test_insert_b(self):
		doc.h2.insert(0, "Hej!")
		self.assertEqual(str(doc.h2), "<h2>Hej!This is a Medium Header that has been appended!</h2>")

	# Test function to check if a space can be inserted
	def test_insert_c(self):
		doc.h2.insert(1, " ")
		self.assertEqual(str(doc.h2), "<h2>Hej! This is a Medium Header that has been appended!</h2>")

	# Test function to check if a string can be added in the end of the existing string
	def test_insert_d(self):
		doc.h2.insert(5, "!!")
		self.assertEqual(str(doc.h2), "<h2>Hej! This is a Medium Header that has been appended!!!</h2>")


# Class to test the insert_before() function that inserts strings or tags immediately before something else in a parse tree
class TestInsertBefore(unittest.TestCase):

	# Test function to check new tag insertion before a tag
	def test_insert_before_a(self):
		tag = doc.new_tag("f")
		tag.string = "Enter"
		doc.title.insert_before(tag)
		self.assertEqual(str(doc.head), "<head>\n<f>Enter</f><title>Your Title Here</title>\n</head>")

	# Test function to check new tag insertion with nested tags
	def test_insert_before_b(self):
		tag = doc.new_tag("ag")
		tag.string = " again "
		doc.title.insert_before(tag)
		self.assertEqual(str(doc.head), "<head>\n<f>Enter</f><ag> again </ag><title>Your Title Here</title>\n</head>")

	# Test function to check if the string insertion is performed successfully
	def test_insert_before_c(self):
		doc.ag.insert_before("string_add")
		self.assertEqual(str(doc.head), "<head>\n<f>Enter</f>string_add<ag> again </ag><title>Your Title Here</title>\n</head>")

	# Test function to check if multiple string insertion is performed successfully
	def test_insert_before_d(self):
		doc.ag.insert_before("+a", "b", "c", "d")
		self.assertEqual(str(doc.head), "<head>\n<f>Enter</f>string_add+abcd<ag> again </ag><title>Your Title Here</title>\n</head>")


# Class to test the insert_after() function that inserts immediately after something else in a parse tree
class TestInsertAfter(unittest.TestCase):

	# Test function to check new tag insertion after a tag
	def test_insert_after_a(self):
		tag = doc.new_tag("after")
		tag.string = "isWorking"
		doc.title.insert_after(tag)
		self.assertEqual(str(doc.head), "<head>\n<f>Enter</f>string_add+abcd<ag> again </ag><title>Your Title Here</title><after>isWorking</after>\n</head>")

	# Test function to check new tag insertion inbetween tags
	def test_insert_after_b(self):
		ibt = doc.new_tag("ibt")
		ibt.string = "inbetween"
		doc.f.insert_after(ibt)
		self.assertEqual(str(doc.head), "<head>\n<f>Enter</f><ibt>inbetween</ibt>string_add+abcd<ag> again </ag><title>Your Title Here</title><after>isWorking</after>\n</head>")

	# Test function to check if the string insertion is performed successfully
	def test_insert_before_c(self):
		doc.ag.insert_after("another_string_add")
		self.assertEqual(str(doc.head), "<head>\n<f>Enter</f><ibt>inbetween</ibt>string_add+abcd<ag> again </ag>another_string_add<title>Your Title Here</title><after>isWorking</after>\n</head>")

	# Test function to check if the multiple string insertion is performed successfully
	def test_insert_before_d(self):
		doc.ibt.insert_after("A", "B", "C", "D")
		self.assertEqual(str(doc.head), "<head>\n<f>Enter</f><ibt>inbetween</ibt>ABCDstring_add+abcd<ag> again </ag>another_string_add<title>Your Title Here</title><after>isWorking</after>\n</head>")


# Testing the clear() function that removes a content of a tag
class TestClear(unittest.TestCase):

	# Testing a simple tag removal
	def test_clear_a(self):
		markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
		soup = BeautifulSoup(markup, 'html.parser')
		tag = soup.a
		tag.clear()
		self.assertEqual(str(tag), "<a href=\"http://example.com/\"></a>")

	# Testing tag removal for a that appears twice
	def test_clear_b(self):
		markup_2 = '<p><b>Hello</b> World<b>!</b> </p>'
		soup_2 = BeautifulSoup(markup_2, 'html.parser')
		tag_2 = soup_2.b
		tag_2.clear()
		self.assertEqual(str(tag_2), "<b></b>")

	# Testing tag with nested tag existing
	def test_clear_c(self):
		markup_3 = '<p><b>Hello</b> World<b>!</b> </p>'
		soup_3 = BeautifulSoup(markup_3, 'html.parser')
		tag_3 = soup_3.p
		tag_3.clear()
		self.assertEqual(str(tag_3), "<p></p>")

	# Testing tag removal for a special case
	def test_clear_d(self):
		markup_4 = '<p><b>Hello<c></b> World<b>!</b></c> </p>'
		soup_4 = BeautifulSoup(markup_4, 'html.parser')
		tag_4 = soup_4.c
		tag_4.clear()
		self.assertEqual(str(tag_4), "<c></c>")

# Testing the extract() function that removes a tag from the tree and returns it
class TestExtract(unittest.TestCase):

	# Testing if the tag is extracted
	def test_extract_a(self):
		extracted_tag_a = doc.ibt.extract()
		self.assertEqual(str(doc.head), "<head>\n<f>Enter</f>ABCDstring_add+abcd<ag> again </ag>another_string_add<title>Your Title Here</title><after>isWorking</after>\n</head>")

	# Testing if the tag is returned
	def test_extract_b(self):
		extracted_tag_b = doc.f.extract()
		self.assertEqual(str(extracted_tag_b), "<f>Enter</f>")

	# Testing if the tag is extracted for tag with nested tags
	def test_extract_c(self):
		extracted_tag_c = doc.head.extract()
		self.assertEqual(str(doc.find_all("head")), "[]")

	def test_extract_d(self):
		extracted_tag_d = doc.b.extract()
		self.assertEqual(str(extracted_tag_d), "<b color=\"red\">This is a new paragraph!</b>")

if __name__ == "__main__":
	unittest.main()
	
	
	
# one function per test - one class per function

#4 functions, 4-5 tests each
