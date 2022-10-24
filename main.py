from bs4 import BeautifulSoup
import requests
import os

url = 'https://en.wikipedia.org/wiki/Parsing'
res1 = requests.get(url)
url = 'https://academic.oup.com/jamia/article/18/5/544/829676?login=false'
res2 = requests.get(url)
url = 'https://en.wikipedia.org/wiki/Natural_language_processing'
res3 = requests.get(url)
url = 'https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP'
res4 = requests.get(url)
url = 'https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/'
res5 = requests.get(url)
html_pages = {res1.text, res2.text, res3.text, res4.text, res5.text}

corpus = []

for html_page in html_pages:
  soup = BeautifulSoup(html_page, 'html.parser')
  linhas = soup.get_text().split("\n")
  corpus.append(linhas)

while True:
  _ = os.system('clear')
  print("Pesquisar")
  pesquisa = input(">>")

  _ = os.system('clear')
  print("Pesquisando: " + pesquisa)

  sair = False
  for i in corpus:
    for j in i:
      if pesquisa in j.lower():
        print(j)
        entrada = input(">>ENTER para continuar procurando\n>>digite sair para sair\n>>")
        os.system('clear')
        print("Pesquisando: " + pesquisa)
        
        if entrada.lower() == "sair":
          sair = True
          break
    if sair:
      break
