import pandas as pd
from bs4 import BeautifulSoup as bs
import urllib
import json

url = 'http://statis.moi.gov.tw/micst/stmain.jsp?sys=220&ym=8301&ymt=10610&kind=21&type=1&funid=c0120101&cycle=1&outmode=0&compmode=0&outkind=1&fldspc=0,7,&cod00=1&rdm=xjheyiqm'
filename = 'marriage_stats.htm'

# html = urllib.request.urlopen(url)
html = open(filename, 'rb').read().decode("big5").encode("utf8")

soup = bs(html, 'html.parser')
table = soup.find('table', {'class': 'tblcls'})


# print(table)

rows = table.findAll('tr')

# print(rows)

data = {}

for row in rows:
    th = row.find('th')
    tds = row.findAll('td')
    if th.string == '': continue
    print(th.string)
    print([td.string for td in tds])
    data[th.string] \
    = [float(td.string.replace(',', '').replace(' ','')) if td.a == None else float(td.a.string.replace(',', '').replace(' ','')) for td in tds]

print(data)
with open(filename+'.json', 'w') as outfile:
    json.dump(data, outfile)
