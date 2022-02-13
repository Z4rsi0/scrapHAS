import requests
from bs4 import BeautifulSoup

url = 'https://www.has-sante.fr/jcms/c_2608425/fr/ue-2-de-la-conception-a-la-naissance-pathologie-de-la-femme-heredite->
response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text, 'lxml')
    for link in soup.select('div.encart div.wysiwyg ul li a[href]'):  #penser à faire pareil avec 'div.encart div.wysiwyg ul li u a[href]'
        lien = str(link['href'])                    #sélection du lien
        lien = lien.lstrip("https://has-sante.fr/") #uniformisation
        print(lien)
