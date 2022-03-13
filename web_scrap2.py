from bs4 import BeautifulSoup
import requests

f = open("index.html","r")
doc = BeautifulSoup(f,"html.parser")
'''
the find tag gives the first occurence of whatever we are tryinh to find while the 
find_all tag gives su all the values in a form of a list
'''
tag = doc.find("option")
#to access or modify an attribute we can acess it like a dictionary
#tag['value'] = "lol bro"
#tag['color'] = "blue"
# to get all the attributes
print(tag.attrs)
print(tag)

#searching for multiple tag names using a list
tags = doc.find_all(["p","div","li"])
print(tags)

uni_tag = doc.find_all(["option"],text = "Undergraduate")
#to search for a class name, instead of using the KEYWORD class we use class_

tag_class = doc.find_all(class_="btn-item")
print(tag_class)