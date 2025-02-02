import pyautogui as py
import time
import pandas as pd
py.PAUSE = 0.5

py.press("win")
py.write("chrome")
py.press("enter")
py.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
py.press("enter")

time.sleep(2)
py.click(x=879, y=516)
py.write("giovannaEmma16@gmail.com")
py.press("tab")
py.write("senhaSuperSecreta")
py.press("tab")
py.press("enter")

#lendo e armazenando a tabela na variável tabela
tabela = pd.read_csv("produtos.csv")

#Próximo passo é cadastrar os produtos
#Lógica: como eu fasso para cadastrar 1 produto

for linha in tabela.index:
    # o .loc é um comando para procurar alguma informação, localizar algo na tabela através da linha
    codigo = tabela.loc[linha , "codigo"]
    py.click(x=916, y=370)
    py.write(codigo)
    py.press("tab")
    py.write(tabela.loc[linha , "marca"])
    py.press("tab")
    py.write(tabela.loc[linha , "tipo"])
    py.press("tab")

    py.scroll(-200)

    py.write(str(tabela.loc[linha , "categoria"]))
    py.press("tab")
    py.write(str(tabela.loc[linha , "preco_unitario"]))
    py.press("tab")
    py.write(str(tabela.loc[linha , "custo"]))
    py.press("tab")

    obs = str(tabela.loc[linha , "obs"])
    if obs != "nan":
        py.write(obs)
    py.press("tab")
    py.press("enter")

    py.scroll(2000)
