 # -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import pandas as pd
import numpy as np
import calendar
import requests
from bs4 import BeautifulSoup
import time
years=[
2013
,2014
,2015
,2016
,2017
,2018
,2019
,2020]
columns=d = {'date': [], 'hour': [],"temperature":[]}
df = pd.DataFrame(d)
for year in years:
    monthIte=0
    monthRange = [31,28,31,30,31,30,31,31,30,31,30,31]
    months =["janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"]
    for month in months:
        for day in range(1,(monthRange[monthIte]+1),1):
                
                print(day,month,year)
                url = 'https://www.infoclimat.fr/observations-meteo/archives/'+str(day)+'/'+str(month)+'/'+str(year)+'/paris-montsouris/07156.html'
                response = requests.get(url)
                time.sleep(1)
                if response.ok:
                    print("ok")
                    soup = BeautifulSoup(response.text, 'lxml')
                    body = soup.find("tbody")
                    L=[]
                    try:
                        temps = body.findAll("span", {"class" : 'tipsy-trigger'})
                    
                        for t in temps:
                            if ("raf" or "mm/1h" or "hPa") not in t.text:
                                
                                L.append(t.text)
                                print(t.text)
                        while L!=[]:
                            hour= L.pop(0)
                            temperature = L.pop(0)
                            date=str(monthIte+1)+"/"+str(day)+"/"+str(year)
                            new_row = {"date":date,"hour":hour,"temperature":temperature}
                            df = df.append(new_row,ignore_index=True)
                        
                    except (AttributeError,IndexError):
                        print("page was not well loaded")
                time.sleep(5)
        monthIte+=1
        

df.to_csv("températureParis.csv")
                

            