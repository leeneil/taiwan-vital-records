import pandas as pd
from bs4 import BeautifulSoup as bs
import urllib
import json
import re

dateROC = True

url = 'http://statis.moi.gov.tw/micst/stmain.jsp?sys=220&ym=8301&ymt=10610&kind=21&type=1&funid=c0120101&cycle=1&outmode=0&compmode=0&outkind=1&fldspc=0,7,&cod00=1&rdm=xjheyiqm'
filename = 'marriage_stats.htm'
# filename = 'birth_stats.htm'

# html = urllib.request.urlopen(url)
html = open(filename, 'rb').read().decode("big5").encode("utf8")

soup = bs(html, 'html.parser')
table = soup.find('table', {'class': 'tblcls'})


# print(table)

rows = table.findAll('tr')

# print(rows)

data = [ [], {} ]


for row in rows:
    # first try to find headers
    ths= row.findAll('th', {'class': 'stytitle'})
    if len(ths) > 0:
        print(ths[1])
        data[0].append( [ ths[i].string for i in range(1, len(ths))  ] )
        continue
    # then data body
    th = row.find('th', {'class': 'stycode'})
    tds = row.findAll('td', {'class': 'stydata'})
    # if th.string == '': continue
    thisDate = th.string
    if dateROC:
        m = re.match(r"(\d+)年\s?(\d+)月", thisDate)
        print( ( m.group(1), m.group(2) ) )
        thisDate = str(int(m.group(1))+1911) + '-' + m.group(2)
    print(thisDate)
    print([td.string for td in tds])
    data[1][thisDate] \
    = [float(td.string.replace(',', '').replace(' ','')) if td.a == None else float(td.a.string.replace(',', '').replace(' ','')) for td in tds]

print(data[1])
print(data[0])

with open(filename+'.json', 'w') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=2)
