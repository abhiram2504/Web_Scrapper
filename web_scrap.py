from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

#sent in a get request to acess the html page

result = requests.get(url)

doc = BeautifulSoup(result.text,"html.parser")

#print(doc.prettify)

prices = doc.find_all(text="$")
#this gets the parent tag of the value
parent = prices[0].parent
#there is a value in the strong tag which we need to acesss
strong = parent.find("strong")
print(strong.string)