## Freelancer de RPA - Bot-Whatsapp
# Este é um exemplo de uma demanda de um dos meus clientes para automatizar uma tarefa através de um bot integrado com o whatsapp.

## Entendendo o problema.
# Demanda do cliente:
- Preciso automatizar mensagens para meus clientes e gostaria de saber valores, e gostaria que entrasse em contato comigo para explicar melhor, eu quero poder mandar mensagens de cobrança em determinado dia para meus clientes com vencimentos diferentes.

# Como automatizar esse processo?
- Em qual versão de uso do whatsapp o bot atuará? 
R: (VERSÃO WEB)

- Quais tecnologias preciso para resolver essa demanda?
  Descrição dos processos a automatizar e tecnologia:
  R: A linguagem de programação será o python versão 3.12.1
  
    TECLADO    ---> PYAUTOGUI
    ACESSO AO SITE  ---> WEBBROWSER
    AUTOMATIZAR DIGITAÇÃO  ---> LINK WHATSAPP PERSONALIZADO
    AUTOMATIZAR LEITURAS DE DADOS DE UMA PLANILHA --->OPENPYXL
    
    ## Passo a passo 
    1° Será aberto o navegador web do whatsapp para login do usuário, com espera de 30s.
    
    2°  Ler planilha e guardar as informações, nome , telefone e vencimento.
    
    3° Acessar a página correta da planilha e percorrer os campos através de um laço 
    de repetição passando por cada linha e armazendo cada valor nas variáveis "nome", "telefone" e "vencimento".
    
    4° Personalizar cada mensagem com nome e vencimento de cada cliente (aqui usado urllib.parse --> quote) 
    
    5° Criar um tratamento de exceção "try" para cada laço, caso corra tudo bem passe para o próximo, caso haja um error criar um arquivo "erro.csv" e armazenar os dados dos que não foram enviados.
    
    6° O laço cria um link personalizado "https://wa.me/{telefone}/? text={quote(mensagem)}" passando o número de telefone 
    de cada cliente e a mensagem personalizada, abre o navegador, clica em iniciar conversa (com pyautogui), clica em usar 
    a versão web, em seguida abre a conversa com a mensagem já escrita e clica na seta de enviar (o pyautogui reconhece cada lugar para ser clicado pelas imagens recortadas), em seguida acionamos novamente o pyautogui.hotkey('crtl','w') para apertar as teclas crlt+w e fechar a guia, assim correrá por toda a planilha enviando a todos os clientes.
