# Passo 1: Entrar no Sistema da Empresa
# Passo 2: Fazer Login
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar Produto
# Passo 5: Repetir o passo 4 até acabar a lista de produtos
import pyautogui
import time

#garante segurança para não acumular processos
pyautogui.PAUSE = 1
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
