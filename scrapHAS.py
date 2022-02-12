import requests
from bs4 import BeautifulSoup

url = 'https://www.has-sante.fr/jcms/c_2608425/fr/ue-2-de-la-conception-a-la-naissance-pathologie-de-la-femme-heredite-l-enfant-l-adolescent'

response = requests.get(url)

if response.ok:
    print(response.headers)
