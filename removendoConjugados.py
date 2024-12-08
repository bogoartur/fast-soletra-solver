from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import *
import time

def respostasSoletra():
    respostasPassadas = []
    with open("respostasSoletra.txt", encoding="utf-8") as respostas:
        for palavras in respostas:
            respostasPassadas.append(palavras.strip("\n"))
    return respostasPassadas

def updateTodasPalavrasSemAcento():
    respostasPassadas = respostasSoletra()
    with open("todasPalavrasSemAcento.txt", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

        palavrasExistentes = {linha.strip() for linha in linhas}
    with open("todasPalavrasSemAcento.txt", "a", encoding="utf-8") as arquivo:
        for palavra in respostasPassadas:
            if palavra not in palavrasExistentes:
                arquivo.write(palavra + "\n")
                palavrasExistentes.add(palavra)
def updateVerbosConjugados():
    respostasPassadas = respostasSoletra()
    with open("verbosConjugados.txt", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open("verbosConjugados.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            if linha.strip("\n") not in respostasPassadas and len(linha.strip("\n")) > 3:
                arquivo.write(linha)
updateVerbosConjugados()

updateTodasPalavrasSemAcento()   

driver = webdriver.Firefox()
driver.get('https://g1.globo.com/jogos/soletra/')

botaoIniciar = driver.find_element(By.CLASS_NAME, "intro-button")
action = ActionBuilder(driver)

ActionChains(driver).click(botaoIniciar).perform()
#driver.implicitly_wait(7)
action.pointer_action.move_to_location(1240, 40)
action.perform
ActionChains(driver).click().perform()

def getLetraCentral():
    letraCentral = str(driver.find_element(By.CLASS_NAME, "center").text)
    return letraCentral.lower()

letraCentral = getLetraCentral()

def getLetasOpcionais():
    letrasOpcionais = []
    for circulo in driver.find_elements(By.CLASS_NAME, "outer"):
        letrasOpcionais.append(circulo.find_element(By.CLASS_NAME, "cell-letter").text.lower())
    return letrasOpcionais

letrasOpcionais = getLetasOpcionais()
print(letraCentral, letrasOpcionais)

alfabeto = ["a", "b", "ç", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alfabeto.remove(letraCentral)
alfabetoSemOpcionais = list(set(alfabeto) - set(letrasOpcionais))

def getPalavrasPossiveis():
    palavrasPossiveis = []
    with open("todasPalavrasSemAcento.txt", "r", encoding="utf-8") as arquivo:
        for palavra in arquivo:
            palavra = palavra.strip().lower()
            if len(palavra) > 3:
                if letraCentral in palavra:
                    if not any(letra in palavra for letra in alfabetoSemOpcionais):
                        palavrasPossiveis.append(palavra)

    return palavrasPossiveis

palavrasPossiveis = getPalavrasPossiveis()

def organizar(lista):
    
    lista.sort(key=lambda palavra: (len(palavra), palavra))
    return lista



def contaLetrasUnicas(palavra):
    letrasUnicas = {letra for letra in palavra if str(letra).isalpha()}
    return len(letrasUnicas)


def getVerbosConjugados():
    verbosConjugados = []
    updateVerbosConjugados()
    with open("verbosConjugados.txt", encoding="utf-8") as arquivo:
        for palavra in arquivo:
            palavra = palavra.strip().lower()
            verbosConjugados.append(palavra)
    return verbosConjugados

def getVerbosInfinitivo():
    verbosInfinitivo = []
    with open("verbosInfinitivo.txt", encoding="utf-8") as arquivo:
        for palavra in arquivo:
            palavra = palavra.strip().lower()
            if len(palavra) > 3:
                verbosInfinitivo.append(palavra)
    return verbosInfinitivo

verbosInfinitivo = getVerbosInfinitivo()
verbosConjugados = getVerbosConjugados()

verbosSemInfinitivos = list(set(verbosConjugados) - set(verbosInfinitivo))

#with open("conjugadosARemover.txt", "a") as arquivo:
 #   for i in verbosSemInfinitivos:
 #       if not (str(i).endswith("ado") or str(i).endswith("ido") or str(i).endswith("edo") or str(i).endswith("odo") or str(i).endswith("udo")):
   #         arquivo.write(i + '\n')

palavrasPossiveis = list(set(palavrasPossiveis) - set(verbosSemInfinitivos))
palavrasPossiveis = organizar(palavrasPossiveis)

apagarTudo = ActionBuilder(driver)
apagarTudo.key_action.send_keys(Keys.BACKSPACE)
def tentarPalavrasPossiveis():
    for palavra in palavrasPossiveis:
        tamanho = len(palavra)
        ActionChains(driver).send_keys(palavra).send_keys(Keys.ENTER).perform()
        time.sleep(0.2)
        for n in range(tamanho):
            apagarTudo.key_action.send_keys(Keys.BACKSPACE)
            time.sleep(0.1)
test_text = ["caca", "caça"]

print(palavrasPossiveis)
tentarPalavrasPossiveis()
        


