import unittest

from bs4 import BeautifulSoup

with open("hamza.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")
# HTML From File



class TestReplaceWith(unittest.TestCase):
		def test_replacewith_i(self):
			new_tag=doc.new_tag("i")
			new_tag.string="How to win friends and influence people with i tag"
			doc.h1.replace_with(new_tag)
			self.assertEqual(str(doc.i),'<i>How to win friends and influence people with i tag</i>')

		def test_replacewith_h2(self):
			new_tag=doc.new_tag("h3")
			new_tag.string="Rich Dad Poor Dad with h3 tag"
			doc.h1.replace_with(new_tag)
			self.assertEqual(str(doc.h3),'<h3>Rich Dad Poor Dad with h3 tag</h3>')

		def test_replacewth_bold(self):
			new_tag=doc.new_tag("mark")
			new_tag.string="You Are a Badass: How to Stop Doubting Your Greatness and Start Living an Awesome Life with mark bold"
			doc.h1.replace_with(new_tag)
			self.assertEqual(str(doc.mark),'<mark>You Are a Badass: How to Stop Doubting Your Greatness and Start Living an Awesome Life with mark bold</mark>')

		def test_replacewith_small(self):
			new_tag=doc.new_tag("small")
			new_tag.string="The Power of Now: A Guide to Spiritual Enlightenment with small tag"
			doc.h1.replace_with(new_tag)
			self.assertEqual(str(doc.small),'<small>The Power of Now: A Guide to Spiritual Enlightenment with small tag</small>')


class TestWrap(unittest.TestCase):

	def test_wrap_with_div(self):
		doc.p.wrap(doc.new_tag("div"))
		self.assertEqual(str(doc.div),'<div><p id="story"><h2>line begins</h2></p></div>')
	
	def test_wrap_with_b(self):
		doc.title.string.wrap(doc.new_tag("b"))
		self.assertEqual(str(doc.title),'<title><b>Hamza Book Collection</b></title>')
		
	def test_wrap_with_i(self):
		doc.title.b.string.wrap(doc.new_tag("i"))
		self.assertEqual(str(doc.title),'<title><b><i>Hamza Book Collection</i></b></title>')


class TestUnwrap(unittest.TestCase):

	def test_unwrap_div(self):
		doc.body.div.unwrap()
		self.assertEqual(len(doc.find_all('div')),0)

	def test_unwrap_bold(self):
		doc.h6.label.unwrap()
		self.assertEqual(str(doc.h6),'<h6>This is a medium header</h6>')

	def test_unwrap_italic(self):
		doc.h5.b.i.unwrap()
		self.assertEqual(str(doc.h5),'<h5><b>This is footer</b></h5>')
	
	
class Test_smooth(unittest.TestCase):
	def test_smooth_h2(self):
		doc.h2.append(", from here")
		doc.smooth()
		doc.h2.prettify()
		self.assertEqual(doc.h2.contents,['line begins, from here'])
	
	def test_smooth_title(self):
		doc.title.b.i.append(", review the list for free")
		doc.smooth()
		doc.title.prettify()
		self.assertEqual(doc.title.b.i.contents,['Hamza Book Collection, review the list for free'])

	def test_smooth_line_ends(self):
		doc.find(id="ends").append(", from here")
		self.assertEqual(str(doc.find(id="ends")),'<p id="ends"> line ends, from here</p>')


if __name__ == "__main__":
	unittest.main()
