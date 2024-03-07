import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui 

# Será aberto o navegador web do whatsapp para login do usuário, com espera de 30s
webbrowser.open('https://web.whatsapp.com/')
sleep(30)

# Ler planilha e guardar as informações, nome , telefone e vencimento.
workbook= openpyxl.load_workbook('clientes.xlsx')
pag_clientes = workbook['Planilha1']

for linha in pag_clientes.iter_rows(min_row=2):   
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value
    
    #Exemplo de mensagem personalizada para cada pessoa
    mensagem = f'Olá {nome} seu boleto vence no dia {vencimento.strftime("%d/%m/%Y")}. Mantenha sempre sua fatura em dia para não perder os descontos do seu produto. Segue o link para pagamento https://www.link_do_pagamento.com.br '
    
    
    
    # Modo de espera para carregar a página 10s
    sleep(10)
    
    try:
        # Criar links personalizados do whatsapp.
        # Enviar mensagens para cada cliente com base na planilha.    
        link_msg_whatsapp = f'https://wa.me/{telefone}/? text={quote(mensagem)}'
        webbrowser.open(link_msg_whatsapp)
        
        
        # o link foi recenteme atualizado e para enviar deve clicar em 3 lugares
        # 1° clicando em iniciar conversa  
        iniciar_conversa = pyautogui.locateCenterOnScreen('init.png')
        sleep(5)
        pyautogui.click(iniciar_conversa[0], iniciar_conversa[1])    
        sleep(5)
        
    
        # 2° clicando para usar a versão web  
        web_zap = pyautogui.locateCenterOnScreen('web.png')
        sleep(5)
        pyautogui.click(web_zap[0], web_zap[1])
        
        # Modo de espera para carregar a página 10s
        sleep(10)
        
        # 3° clicando para enviar a mensagem  
        seta = pyautogui.locateCenterOnScreen('seta.png')
        sleep(5)
        pyautogui.click(seta[0], seta[1])
        sleep(5)
        
        # Após enviar devemos fechar a guia, para não abrir guias demais
        # e não sobrecarregar o a máquina
        pyautogui.hotkey('crtl','w')
        sleep(5)
    except:
        print(f'Não foi possivél enviar mensagem para {nome}')
        with open('erros.csv','a',newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},{telefone}')    
        
    

