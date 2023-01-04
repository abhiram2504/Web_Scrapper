from bs4 import BeautifulSoup
import requests
import re

url = "https://coinmarketcap.com/"
result = requests.get(url).text

doc=BeautifulSoup(result,"html.parser")

table_body = doc.tbody
#table_contents gives a list of all the tags inside the table
trs = table_body.contents

'''
.next_siblings
.contents
.children
.parent
'''
#the contents in the tabale are teh siblings of each otehr thus we could parse
#throught them
#looping through the prices, thus createing a dictionary
prices = {}
#looking at the top 10 coins
for tr in trs[:9]:
    # we do it fomr 2 to 4 beucase we would like to just get the
    #price and teh name the frst two are icon and the rank
    name,price = tr.contents[2:4]
    #we the the name which is in teh p tag, .string to give us in the hting in the p tag
    fixed_name = name.p.string
    #the price is also in teh p tag
    fixed_price = price.a.string
    #print(name.p.string)
    #print(fixed_price)
    #setting the key to the value in the dictoray 
    prices[fixed_name]=fixed_price
print(prices)

