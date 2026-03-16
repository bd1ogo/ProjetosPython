# Passo 1: Entrar no Sistema da Empresa
# Passo 2: Fazer Login
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar Produto
# Passo 5: Repetir o passo 4 até acabar a lista de produtos
import pyautogui
import time
import pandas

#garante segurança para não acumular processos
pyautogui.PAUSE = 2
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#Entrando no Sistema pelo navegador
pyautogui.press('win')
pyautogui.write('brave')
pyautogui.press('enter')

pyautogui.write(link)
pyautogui.press('enter')
#pausa para o site poder carregar com segurança
time.sleep(3)

#Fazendo Login
#email
pyautogui.click(x=985, y=431)
pyautogui.write('barrosof.diogo@gmail.com')
#senha
pyautogui.press('tab')
pyautogui.write('senhadificil123')
#logar
pyautogui.press('tab')
pyautogui.press('enter')                                                                                                                                                                                                                                                                                                                                                          


#pausa maior para o site poder carregar com segurança
time.sleep(3)                                                                                                                                                                           
#Abrindo a base de dados (importar o arquivo .csv)
tabela = pandas.read_csv('produtos.csv')

for linha in tabela.index:
    #Cadastrar produto
    #campo do código
    pyautogui.click(x=806, y=316) 
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')
    #campo da marca
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')
    #campo tipo
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')
    #campo do categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    #campo do preço
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')
    #campo de custo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')
    #campo de obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':  
        pyautogui.write(obs)
    pyautogui.press('tab') #passa para o campo de enviar

    #cadastra o produto
    pyautogui.press('enter')
    #voltar para o inicio para cadastrar o próximo produto
    pyautogui.scroll(5000)

    
