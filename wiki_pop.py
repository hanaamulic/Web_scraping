import requests
import bs4
from bs4 import BeautifulSoup as bs
import pandas as pd
import unicodedata
import re

# cities = ['Berlin', 'Hamburg', 'Frankfurt','Munich','Stuttgart','Leipzig','Cologne','Dresden','Hannover','Paris', 'Barcelona','Lisbon','Madrid']
cities = ['Berlin','Paris','Amsterdam','Barcelona','Rome','Lisbon','Prague','Vienna','Madrid']

def City_info(soup):
    
    ret_dict = {}
    ret_dict['city'] = soup.h1.get_text()
    
    
    if soup.select_one('.mergedrow:-soup-contains("Mayor")>.infobox-label') != None:
        i = soup.select_one('.mergedrow:-soup-contains("Mayor")>.infobox-label')
        mayor_name_html = i.find_next_sibling()
        mayor_name = unicodedata.normalize('NFKD',mayor_name_html.get_text())
        ret_dict['mayor']  = mayor_name
    
    if soup.select_one('.mergedrow:-soup-contains("City")>.infobox-label') != None:
        j =  soup.select_one('.mergedrow:-soup-contains("City")>.infobox-label')
        area = j.find_next_sibling('td').get_text()
        ret_dict['city_size'] = unicodedata.normalize('NFKD',area)

    if soup.select_one('.mergedtoprow:-soup-contains("Elevation")>.infobox-data') != None:
        k = soup.select_one('.mergedtoprow:-soup-contains("Elevation")>.infobox-data')
        elevation_html = k.get_text()
        ret_dict['elevation'] = unicodedata.normalize('NFKD',elevation_html)
    
    if soup.select_one('.mergedtoprow:-soup-contains("Population")') != None:
        l = soup.select_one('.mergedtoprow:-soup-contains("Population")')
        c_pop = l.findNext('td').get_text()
        ret_dict['city_population'] = c_pop
    
    if soup.select_one('.infobox-label>[title^=Urban]') != None:
        m = soup.select_one('.infobox-label>[title^=Urban]')
        u_pop = m.findNext('td')
        ret_dict['urban_population'] = u_pop.get_text()

    if soup.select_one('.infobox-label>[title^=Metro]') != None:
        n = soup.select_one('.infobox-label>[title^=Metro]')
        m_pop = n.findNext('td')
        ret_dict['metro_population'] = m_pop.get_text()
    
    if soup.select_one('.latitude') != None:
        o = soup.select_one('.latitude')
        ret_dict['lat'] = o.get_text()

    if soup.select_one('.longitude') != None:    
        p = soup.select_one('.longitude')
        ret_dict['long'] = p.get_text()
    
    return ret_dict



list_of_city_info = []
for city in cities:
    url = 'https://en.wikipedia.org/wiki/{}'.format(city)
    web = requests.get(url,'html.parser')
    soup = bs(web.content)
    list_of_city_info.append(City_info(soup))
df_cities = pd.DataFrame(list_of_city_info)
# df_cities = df_cities.set_index('city')
df_cities