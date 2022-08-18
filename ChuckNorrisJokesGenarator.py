#Code that Prints Random Chuck Norris Jokes fetched from http://api.icndb.com/jokes/random

import json
from urllib.request import urlopen



    



key = '0'

while (key!='q'):# loop terminates with q as input
    with urlopen('http://api.icndb.com/jokes/random') as reponse:
        data=json.loads(reponse.read())#fetches next joke!
    print(data['value']['joke']) # exports from json only the joke part
    key=input('press any letter to change joke or q to quite')
    
print('Chuck says bye bye!')