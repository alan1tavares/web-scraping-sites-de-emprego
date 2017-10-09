from bs4 import BeautifulSoup
import requests

def scrapHomePage(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    
    vagas = soup.find_all(class_="jobs-post")

    nomes = [nome.get_text().strip() for nome in soup.select(".jobs-post .column h4 a")]
    lugares = [lugar.get_text().strip() for lugar in soup.select(".jobs-post .column .jobs-place")]
    tipoVagas = [tipo.get_text().strip() for tipo in soup.select(".button.job_type")]

def scrapPaginaEmprego(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    conteudo = soup.find(class_="section-content")
    
    texto = ""
    for x in conteudo.stripped_strings:
        texto += repr(x)
    texto = texto.replace("''", " ").replace("(adsbygoogle = window.adsbygoogle || []).push({});", " ")
    
    return (texto)

url = "http://queroworkar.com.br/blog/vagas/"
page = requests.get(url)

if (str(page.status_code)[0] == "2"): 
    # scrapHomePage(page)
    scrapPaginaEmprego()
