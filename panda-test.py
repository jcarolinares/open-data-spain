#Panda test

import json
import pandas as pd
import wget
# df=pd.read_json("data.json")

#http://datos.madrid.es/egob/catalogo/206974-0-agenda-eventos-culturales-100.csv
#http://datos.madrid.es/egob/catalogo/201132-0-turismo.json
#df=pd.read_json("http://datos.madrid.es/egob/catalogo/206974-0-agenda-eventos-culturales-100.json")
#df=pd.read_excel("http://datos.madrid.es/egob/catalogo/213693-0-monumentos-madrid.xls")

#df=pd.read_csv("http://datos.madrid.es/egob/catalogo/200967-0-mercados.csv")
#df=pd.read_json("http://datos.madrid.es/egob/catalogo/200967-0-mercados.json")

file=open('206974-0-agenda-eventos-culturales-100.json',"r")

file_data=file.read()
file.close()

file=open('206974-0-agenda-eventos-culturales-100.json',"w")
file_data=file_data.replace("\\","")
file.write(file_data)
file.close()


data = json.load(open('206974-0-agenda-eventos-culturales-100.json'))
df = pd.DataFrame(data["@graph"])
print(df.head(5))

#data = json.load(file_data)
