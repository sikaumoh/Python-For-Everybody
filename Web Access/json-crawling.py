import json
import ssl
import urllib.request, urllib.parse, urllib.error

data = '''
{
"name": "Chuck",
"phone": {
"type" : "intl",
"number" : "+1 734 303 4456"
},
"email" : {
"hide": "yes"
}
}
'''

info = json.loads(data)
# print('Name:', info['name'])  # prints out Name: Chuck
# print('Hide:', info['email']['hide'])  # prints out Hide: yes

# Exercise 1
Connecting to data
url = 'http://py4e-data.dr-chuck.net/comments_1187248.json'
connection = urllib.request.urlopen(url)
data = connection.read().decode()

try:
    document = json.loads(data)
except:
    print('Issue with json.loads()')
    quit()

total = 0
for item in document['comments']:
    number = int(item['count'])
    total += number
print(total)

# Exercise 2
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

tag = True
while tag:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    parms['key'] = 42
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        document = json.loads(data)
    except:
        break

    # print(json.dumps(document['results'][0], indent=4))
    # print(document['results'][0])
    for k, v in document['results'][0].items():
        if k != 'place_id': continue
        print('Place_ID:', v)
        tag = False
