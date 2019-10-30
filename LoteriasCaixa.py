
import json
import requests
import bs4

site = requests.get('http://loterias.caixa.gov.br/wps/portal/loterias/landing/federal/')
#site = requests.get('http://loterias.caixa.gov.br/wps/portal/loterias/landing/quina/')

soup = bs4.BeautifulSoup(site.text, 'html.parser')
base = soup.find("base")['href']
urlBuscaResultado = soup.find("input", {"id": "urlBuscarResultado", "type": "hidden"})['value']
resp = requests.get(base + urlBuscaResultado)
resultado = json.loads(resp.text)


#Resultado para QUINA
#print(resultado)
#somente os numeros:
#print(resultado['resultadoOrdenado'].split('-'))

#Resultado para FEDERAL
resultado2 = resultado['premios']
resultado3 = resultado2[0]
print(resultado3)
