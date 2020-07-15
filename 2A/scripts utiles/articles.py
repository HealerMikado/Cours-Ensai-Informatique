from lxml import etree
import urllib.request


opener = urllib.request.build_opener()
tree = etree.parse(opener.open('https://www.lemonde.fr/rss/une.xml'))
titres = tree.xpath('//item/title')
for titre in titres:
    print(titre.text.encode("utf-8"))