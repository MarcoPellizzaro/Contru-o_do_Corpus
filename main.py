# Marco Vinícius Costódio Pellizzaro
'''
ENUNCIADO 
Sua  tarefa  será  transformar  um  conjunto  de  5  sites,  sobre  o  tema  de  processamento  de 
linguagem natural em um conjunto de cinco listas distintas de sentenças. Ou seja, você fará uma função 
que, usando a biblioteca Beautifull Soap, faça a requisição de uma url, e extrai todas as sentenças desta 
url. Duas condições são importantes:  
a) A página web (url) deve apontar para uma página web em inglês contendo, não menos que 
1000 palavras.  
b) O texto desta página deverá ser transformado em um array de senteças.   
'''
import requests
from bs4 import BeautifulSoup, Comment
import spacy

nlp = spacy.load("en_core_web_sm") 

url1 = 'https://en.wikipedia.org/wiki/Natural_language_processing'
url2 = 'https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html'
url3 = 'https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP'
url4 = 'https://towardsdatascience.com/your-guide-to-natural-language-processing-nlp-48ea2511f6e1'
url5 = 'https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/'

sites = [url1, url2, url3, url4, url5]

textos = []

i = 0
while i < 5:
  texto = []
  textos.append(texto)
  i += 1

i = 0;
while i < 5:                     
  html = requests.get(sites[i]).text                     
  soup = BeautifulSoup(html, 'html.parser')     
  for j in soup(['style', 'script', 'head', 'header', 'meta', '[document]', 'title', 'footer', 'iframe', 'nav']):
    j.decompose()
    texts = ' '.join(soup.stripped_strings)                      
  page = nlp(texts)

  for x in page.sents:
      textos[i].append(x.text)

  i += 1;

for i in textos:
  print(i)
