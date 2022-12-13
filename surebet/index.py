import requests
from bs4 import BeautifulSoup

# while True :
url = 'https://pt.surebet.com/surebets'

response = requests.get ( url )
site = BeautifulSoup ( response.text, 'html.parser' )
margem = '1.00'

jogo = site.find ( 'tbody', attrs = {'class' : 'surebet_record'} )

profite = jogo.find ( 'span', attrs = {'class' : 'profit'} )

modalidade = jogo.find ( 'span', attrs = {'class' : 'minor'} )

odds1 = jogo.find ( 'td', attrs = {'class' : 'value odd_record_FECCHA'} )
print ( '-----INFORMAÇÕES-----' )

if modalidade.text >= margem :
   print ( 'Partida segura' )
else :
   print ( 'Melhor não' )

print ( jogo.prettify () )
print ( 'modalidae:', modalidade.text )
print ( 'Profite:', profite.text )
print('odds1:', odds1)
print ( '----------------------' )