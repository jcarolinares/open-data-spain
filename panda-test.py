#Panda test

import json
import pandas as pd
import wget
from datetime import datetime


# df=pd.read_json("data.json")

#http://datos.madrid.es/egob/catalogo/206974-0-agenda-eventos-culturales-100.csv
#http://datos.madrid.es/egob/catalogo/201132-0-turismo.json
#df=pd.read_json("http://datos.madrid.es/egob/catalogo/206974-0-agenda-eventos-culturales-100.json")
#df=pd.read_excel("http://datos.madrid.es/egob/catalogo/213693-0-monumentos-madrid.xls")

#df=pd.read_csv("http://datos.madrid.es/egob/catalogo/200967-0-mercados.csv")
#df=pd.read_json("http://datos.madrid.es/egob/catalogo/200967-0-mercados.json")

json_url="http://datos.madrid.es/egob/catalogo/206974-0-agenda-eventos-culturales-100.json"

print ("Downloading: "+json_url)
wget.download(json_url)

file=open('206974-0-agenda-eventos-culturales-100.json',"r")

file_data=file.read()
file.close()

file=open('206974-0-agenda-eventos-culturales-100.json',"w")
file_data=file_data.replace("\\","")
file.write(file_data)
file.close()


#Pandas
data = json.load(open('206974-0-agenda-eventos-culturales-100.json'))
df = pd.DataFrame(data["@graph"])

#How to access data
print("\n")
print (df['title'][2])
print(df['description'][2])
print(df['dtstart'][2])
print(df['dtend'][2])


#Convert a string to a real datetime object
date_obj = datetime.strptime(df['dtstart'][2], '%Y-%m-%d %H:%M:%S.%f') #%Y%m%dT%H%M%S

print (date_obj)
