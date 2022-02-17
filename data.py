import requests
import xml.etree.ElementTree as ET
from urllib.request import urlopen

url = 'https://www.tcmb.gov.tr/kurlar/today.xml'
resp = requests.get(url=url)
tree = ET.parse(urlopen(url))
root = tree.getroot()

list = []
list.append(root.findall('Currency'))

for i in list[0]:
    currencycode = i.get('Kod')
    banknotebuy = i.find("BanknoteBuying").text
    banknoteselling = i.find("BanknoteSelling").text
    if currencycode == "USD":
        print("Dolar alış: ", banknotebuy)
        print("Dolar satış: ", banknoteselling)
    if currencycode == "EUR":
        print("Euro alış: ", banknotebuy)
        print("Euro satış: ", banknoteselling)
