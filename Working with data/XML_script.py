#!/usr/bin/python3
import xml.dom.minidom as xmldom
import xml.sax as xmlsax

#directory = input("Enter xml file path:")
directory = "C:\\Users\\Michal\\Documents\\Python Homework\\Working with data\\books.xml"

dom_parsed = xmldom.parse(directory)

#create new elements with dom
for index in range(len(dom_parsed.getElementsByTagName("book"))):
    new_element = dom_parsed.createElement("edition")
    element_text = dom_parsed.createTextNode("first")
    new_element.appendChild(element_text)
    dom_parsed.getElementsByTagName("book")[index].appendChild(new_element)

#change categories with dom
for index in range(len(dom_parsed.getElementsByTagName("book"))):
    dom_parsed.getElementsByTagName("book")[index].getAttributeNode("category").nodeValue = "food"

xml_write = dom_parsed.toxml()

class sax_handler(xmlsax.ContentHandler):
    def __init__(self):
        self.current = ""
        self.title = ""
        self.author = ""
        self.year = ""
        self.price = ""

    def startElement(self, tag, attributes):
        self.current = tag

    def endElement(self, name):
        self.current = ""

    def characters(self, content):
        if self.current == "title":
            self.title = content
            print("Book title: ", self.title)
        elif self.current == "author":
            self.author = content
            print("Book author: ", self.author)
        elif self.current == "year":
            self.year = content
            print("Book year: ", self.year)
        elif self.current == "price":
            self.price = content
            print("Book price: ", self.price, "\n")

handler = sax_handler()
parser = xmlsax.make_parser()
parser.setContentHandler(handler)
parser.parse(directory)

print("Original file displayed above, writing additional data to books_dom_modified.xml")
with open("Working with data/books_dom_modified.xml", "w") as f:
    f.write(xml_write)