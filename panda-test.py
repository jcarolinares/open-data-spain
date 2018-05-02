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

data = json.load(open('206974-0-agenda-eventos-culturales-100.json'))

df = pd.DataFrame(data["@graph"])


print(df.head(5))
