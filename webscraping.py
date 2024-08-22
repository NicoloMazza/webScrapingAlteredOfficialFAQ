import requests
from pprint import pprint
from bs4 import BeautifulSoup
import re
import warnings

def richiediPagina(url):
    page = requests.get(url, verify = False)
    soup = BeautifulSoup(page.text, 'html.parser')
    open("file_script.txt", "w").close()
    with open("file_script.txt","a") as file:
        file.write(str(soup))

def cercaPattern(pattern, array):
    with open('file_script.txt', 'r') as file:
        for line in file:
            if re.search(pattern, line):
                array.append(line)

def pulisciStringa(array_da_pulire, array_pulito, estensione, pattern1, pattern2):
    for e in array_da_pulire:
        indice_iniziale = e.find(pattern1)
        indice_finale = e.find(pattern2)
        url_pulito = estensione + e[indice_iniziale+6:indice_finale-1]
        array_pulito.append(url_pulito)

def getFirst(url):
    richiediPagina(url)
    urls = []
    cercaPattern('href="/hc/en-us/sections/', urls)
    urls_da_contattare = []
    pulisciStringa(urls, urls_da_contattare, 'https://support.altered.gg', 'href', ">")
    return urls_da_contattare

def getDomande(url):
    richiediPagina(url)
    urls2 = []
    cercaPattern('href="/hc/en-us/articles/', urls2) #Serve a trovare il pattern delle domande
    domande = []
    pulisciStringa(urls2, domande, 'https://support.altered.gg', 'href', '>') #Qui abbiamo la pulizia delle domande

    risposte = []
    for e in domande:
        domanda_formattata = e[60:]
        domanda_formattata = domanda_formattata.replace("-", " ")
        with open("risultato_script.txt","a") as file:
            file.write(str(domanda_formattata.upper() + "?\n")) #scrivi la domanda
        richiediPagina(e) #chiede la pagina per la risposta cercata
        cercaPattern('<span data-sheets-root="1" style="font-size: 10pt; font-family: Arial; font-style: normal;">' or "</span>", risposte) #cerca la risposta nella pagina e la memorizza in risposte
        risposta_formattata = risposte[len(risposte)-1][121:-18]
        risposta_formattata = risposta_formattata.replace("<\br>", " ")
        risposta_formattata = risposta_formattata.replace("<br/>", " ")
        risposta_formattata = risposta_formattata.replace('<span style="font-size: 10pt; font-family: Arial; font-weight: bold; font-style: normal;">:', "\n-")
        with open("risultato_script.txt","a") as file:
            file.write(str(risposta_formattata + "\n"))

open("risultato_script.txt", "w").close()
warnings.filterwarnings("ignore")
urls = []
urls = getFirst('https://support.altered.gg/hc/en-us')  #da qui ho preso gli url di ogni singola sezione della pagina home di supporto
for e in urls: 						#per ogni url, qui, sto chiedendo di prendere le domande di quella specifica sezione
    with open("risultato_script.txt","a") as file:
        file.write(str("###############\n" + e[60:] + "\n###############\n"))
    getDomande(e)

#DEBUG PER VEDERE IL FILE FINALE
with open("risultato_script.txt","r") as file:
    for line in file:
        print(line)
