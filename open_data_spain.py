# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json
import os
import subprocess
import requests
import wget



#Data parameters
main_url="http://datos.gob.es"
data_id="l01280796-aparcamientos-publicos-municipales"

format_ext={
    "json": "JSON",
    "csv":"CSV",
    "xls":"XLS",
    "html":"HTML",
    "xml-app":"XML-APP",
    "pdf":"PDF",
    "ascii":"ASCII",
    "pc-axis":"PC-Axis",
    "xlsx":"XLSX"
} #TODO add the rest of the formats




def catalog_downloader(keyphrase,format,max_of_pages):

    #format=".json"
    page=1
    #max_of_pages=16
    #keyphrase="madrid"
    extra_arg="&publisher_display_name=Ayuntamiento+de+Madrid"

    data_titles=[]
    data_urls=[]
    database_urls=[]
    repositories={}
    one_repository={}

    for page in range(max_of_pages):

        print("\n\nPage: "+str(page+1)+"\n\n")

        #Collecting repositories #TODO read the catalog using the atom link instead of scrapping http://datos.gob.es/feeds/dataset.atom
        # r  = requests.get("http://datos.gob.es/es/catalogo?q=madrid&sort=metadata_modified+desc&publisher_display_name=Ayuntamiento+de+Madrid"+"&page="+str(page+1))
        if format!="":
            r  = requests.get("http://datos.gob.es/es/catalogo"+"?q="+keyphrase+"&sort=metadata_modified+desc"+"&res_format_label="+format_ext["json"]+extra_arg+"&page="+str(page+1))
        else:
            r  = requests.get("http://datos.gob.es/es/catalogo"+"?q="+keyphrase+"&sort=metadata_modified+desc"+extra_arg+"&page="+str(page+1))

        data = r.text
        #print("http://datos.gob.es/es/catalogo?q=madrid&sort=metadata_modified+desc&publisher_display_name=Ayuntamiento+de+Madrid+&page="+str(page))
        soup = BeautifulSoup(data,"lxml")

        #http://datos.gob.es/es/catalogo?q=madrid&sort=metadata_modified+desc&publisher_display_name=Ayuntamiento+de+Madrid&page=2
        #http://datos.gob.es/es/catalogo?q=madrid&sort=metadata_modified+desc&publisher_display_name=Ayuntamiento+de+Madrid+&page=1

        #Parsing the data
        file= open(keyphrase+"_databases"+".json", "w")
        for link in soup.find_all('strong',class_="dge-list__title dataset-heading"):
            aux_database_urls=[]
            data_titles.append(link.get_text().replace("\n",""))
            data_urls.append(main_url+link.a.get("href"))

            print("\n\n"+data_titles[-1]+": "+data_urls[-1])

            b  = requests.get(data_urls[-1])
            data_b = b.text
            soup_b = BeautifulSoup(data_b,"lxml")
            for link in soup_b.find_all('a',class_="btn btn-primary resource-url-analytics"):
                aux_database_urls.append(link.get("href"))
                print(link.get("href"))

            database_urls.append(aux_database_urls)

        #Creating the json data
        for index in range(len(data_titles)):
            #print(data_titles[index]+": "+data_urls[index])
            one_repository[data_titles[index]]={"title":data_titles[index],"url":data_urls[index],"data_files":database_urls[index]}

    #Saving the data in a file as a json format
    file.write(json.dumps(one_repository, indent=4, sort_keys=True,ensure_ascii=False).encode('utf8'))
    file.close()

def json_parser(json_url):
    #print ("Downloading: "+json_url)
    #wget.download(json_url, 'data.json')
    #file= open("data.json", "r")
    #parsed_json = json.loads(file.read())

    #with open('data.json') as json_file:
    #    data = json.load(json_file.)

    #Read of the json (be careful with the invalid characters)
    file=open("data.json","r")
    data=file.read()#.decode('utf8')
    file.close()
    json_data=json.loads(data)

    #Parser of the POF actividades Madrid proximos 100 dias
    print(json_data["@graph"][0]["title"])
    print(json_data["@graph"][0]["description"])
    print(json_data["@graph"][0]["event-location"])
    print(json_data["@graph"][0]["dtstart"])
    print(json_data["@graph"][0]["dtend"])

def main():
    catalog_downloader(keyphrase="madrid",format="",max_of_pages=16)
    #json_parser("http://datos.madrid.es/egob/catalogo/206974-0-agenda-eventos-culturales-100.json")

if __name__ == "__main__":
    main()


#for repository in repositories:
#    print(repository)


#Reading from the json file
# file= open("madrid-catalogo.json", "r")
# parsed_json = json.loads(file.read())

# print(parsed_json['\nExpedientes de contrataci\u00f3n adjudicados\n'])

'''
<div class="btn-group">
        <a href="http://datos.madrid.es/egob/catalogo/206974-0-agenda-eventos-culturales-100.json" class="btn btn-primary resource-url-analytics" target="_blank">
            <i class="icon-download"></i>
            Descargar

        </a>
      </div>
'''


'''
<strong class="dge-list__title dataset-heading">

              <a href="/es/catalogo/l01280796-accidentes-de-trafico-2009-a-2014-seguridad-vial">Accidentes de tráfico. Datos desde 2009 (Seguridad vial)</a>
</strong>
'''

'''
#Selected dataset
#Downloading the page
r  = requests.get("http://datos.gob.es/apidata/catalog/dataset/"+data_id+format)
data = r.text
soup = BeautifulSoup(data,"lxml")

#Select the right dataset and download the file
file= open(data_id, "w")
file.write(data)
file.close()
'''

#l01280796-aparcamientos-publicos-municipales

#http://datos.gob.es/apidata/catalog/dataset/l01280148-presion-barometrica-2015.json


'''
import json
import urllib2

url = "https://www.govtrack.us/data/congress/113/votes/2013/s11/data.json"
data = json.load(urllib2.urlopen(url))
'''
