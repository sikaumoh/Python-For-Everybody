# XML Schema a way to validate data is correct
import xml.etree.ElementTree as ET
data = '''
<person>
<name>Chuck</name>
<phone type="intl">+1 734 303 4456</phone>
<email hide="yes"/>
</person>
'''

tree = ET.fromstring(data)
# print('Name:', tree.find('name').text)  # prints out Name: Chuck
# print('Attr:', tree.find('email').get('hide'))  # prints out Attr: yes

# Exercise 
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# web scraping
url = 'http://py4e-data.dr-chuck.net/comments_1187247.xml'
data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)
comments = tree.findall('comments/comment')
total = 0
for item in comments:
    number = int(item.find('count').text)
    total += number
print(total)
