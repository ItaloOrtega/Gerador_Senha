#Import de todas as bibliotecas utilizadas
from tkinter import *
import random
import pyperclip
import tkinter
import string

#Dicionario que contem as opções que o usuario pode ou não ativar
vars = {"lma": True,"n": True,"ce": False,"om": False,"pd":False}

#Função que coloca letras maiusculas e minusculas na senha do usuário
def letra(linha,tam):
  linha = str(linha)
  #Caso a linha não possua nenhum caracter, logo precisa ser colocado letras minusculas
  if linha == "":
    #Adiciona uma qtd X de caracteres minusculos, de acordo a divisão feita aleatoriamente
    for x in range(tam[0]):
      linha = linha + str(string.ascii_lowercase[random.randint(0,len(string.ascii_lowercase)-1)])
  #Caso tenha uma palavra pre-definida e ela não tendo o tamanho escolhido da senha
  if linha != "" and len(linha) != tam[0]:
    #É adicionado mais caracteres minusculos, para que a senha seja do tamanho correto
    for x in range(tam[0]-len(linha)):
      linha = linha + str(string.ascii_lowercase[random.randint(0,len(string.ascii_lowercase)-1)])
  #Caso lma = True significa que o usuário quer letras maiusculas na senha
  if vars["lma"] is True:
    #Adicionara letras maiusculas até cont ser igual a qtd da divisão
    for y in range(tam[1]):
      #For que percorre a senha atual
      for x in range(len(linha)):
        #Sendo o caracter atual uma letra minuscula
        if string.ascii_lowercase.find(linha[x]) != -1:
          #Tem 50% de chance dessa letra virar maiuscula
          if random.choice([True,False]) is True:
            linha = linha[:x] + linha[x].upper() + linha[x+1:]  
      #Adiciona no final uma letra maiuscula
      linha = linha + str(string.ascii_uppercase[random.randint(0,len(string.ascii_uppercase)-1)])
  return linha

#Função que adiciona números na senha
def n(linha,tam):
  #Lista de números de 0 a 9
  lista = list(range(0,10))
  #For para adicionar no minimo a qtd de valores da divisão da senha
  for y in range(tam):
    for x in range(len(linha)): #Percorre a senha atual
      #If para trocar algumas letras por números
      if linha[x].upper() == "I":
        if random.choice([True,False]) is True:
          linha = linha[:x] + "1" + linha[x+1:]   
      elif linha[x].upper() == "E":
        if random.choice([True,False]) is True:
          linha = linha[:x] + "3" + linha[x+1:] 
      elif linha[x].upper() == "O":
        if random.choice([True,False]) is True:
          linha = linha[:x] + "0" + linha[x+1:]

    linha = linha + str(lista[random.randint(0,len(lista)-1)])
  return linha

#Mesma coisa da função 'n' , mas com caracteres especiais
def ce(linha,tam):
  lista = ["!","@","#","$","%","&"]
  for y in range(tam):
    for x in range(len(linha)):
      if linha[x].upper() == "A":
        if random.choice([True,False]) is True:
          linha = linha[:x] + "@"+ linha[x+1:]
      elif linha[x].upper() == "S":
        if random.choice([True,False]) is True:
          linha = linha[:x] + "$" + linha[x+1:] 
      elif linha[x].upper() == "E":
        if random.choice([True,False]) is True:
          linha = linha[:x] + "&" + linha[x+1:] 
    linha = linha + lista[random.randint(0,len(lista)-1)]
  
  return linha

#Função que adiciona caracteres matematicos no final da senha
def om(linha,tam):
  lista = ["/","*","-","+",",","."]
  for x in range(tam):
    linha = linha + lista[random.randint(0,len(lista)-1)]
  return linha

#Função que ativa ou desativa a maioria das opções disponiveis para o usuario
def att_normal(rb,sttr):
  global vars
  if vars[sttr] == False:
    vars[sttr] = True
  else:
    vars[sttr] = False
    rb.set(None)

#Função que ativa ou desativa a entrada de palavras pre definidas na senha
def att_pd(entrada, rb):
  global vars
  if vars["pd"] == False:
    vars["pd"] = True
    entrada.config(state="normal")
  else:
    vars["pd"] = False
    entrada.config(state="disable")
    rb.set(None)

#Função sai da aplicação toda
def sair():
  quit()

#Função para copiar a senha generada
def copiar():
  pyperclip.copy(entrada.get())

#Função que gera as senhas
def gerar(entr_palav,entr_final,btt):
  entr_final.delete(0, 'end') #Caso tenha uma senha na entrada, ela é limpada
  linha = "" #linha inicial
  if lbl_erro["text"] == "ERRO": #Caso tenha acontecido um erro anteriormente
    lbl_erro.config(text="",bg= "#CCCCCC" ,fg="#000000")

  #Caso do maximo e minimo valores forem menores do que 10 e 6 respectivamente, ou nem existir
  try:
    maax = int(ent_max.get())
    if maax < 10:
      maax = 10
  except:
    maax = 10
  
  try:
    miin = int(ent_min.get())
    if miin < 6:
      miin = 6
  except:
    miin = 6
  
  #Caso tenham palavras pre definidas para colocar na senha
  if entr_palav['state'] != tkinter.DISABLED:
    #Copia todos os caracteres dentro da entrada para a linha
    linha = entr_palav.get()
    flag = False #Flag para verificar se tem ou não somente letras
    for x in string.ascii_letters: #Percorre todas 
      if linha.find(x) != -1:
        flag = True
        break
    if flag is False:
      lbl_erro.config(text="ERRO", bg="#CC3300",fg="#FFFFFF")
      return
    for x in linha:
      if string.ascii_letters.find(x) == -1:
        linha = linha.replace(str(x),"")
  
  #A qtd de divisores que existirão para divir a senha em partes não identicas
  tam_div = 1 #Sempre tem 1 no minimo, que são as letras minusculas
  for x in vars.keys(): #Percorre o dicionario
    #Essa opção sendo verdadeira e diferente de 'pd'
    if vars[x] is True and x != "pd": 
      tam_div += 1
  
  #Caso tenham palavras reservadas
  if entr_palav['state'] != tkinter.DISABLED:
    #Diminui em um os divisores, pois a qtd de caracters das letras minusculas é igual...
    # a qtd de caractes das palavras predefinidas
    tam_div -= 1
  
  #Verifica se a tamanho maximo e minimo possui a quantidade minima, que é a soma de:
  #Pelo menos 1 caracter das opções escolhidas adicionados no final
  #E se existir palavras predefinidas, todos os caracteres delas

  if maax-1 <= (len(linha) + tam_div):
    #Sendo menor que essa soma, modifica o maximo
    maax = int(len(linha) + tam_div*3)
    ent_max.delete(0, 'end')
    ent_max.insert(END,maax)
  
  if miin < (len(linha) + tam_div):
    #Mesma coisa mas com o minimo
    miin = int(len(linha) + tam_div)
    ent_min.delete(0, 'end')
    ent_min.insert(END,miin)
  
  #Escolhe o tamanho final da senha
  #Que será um valor entre o máximo e o minimo
  tam = random.randint(miin,maax)

  #Verifica se a o tamanho escolhido é possivel dados as opções escolhidas
  while tam -(tam_div+len(linha)) < 0:
    #Não sendo, entra nesse while até ser
    tam = random.randint(miin,maax)
  
  #Adiciona novamente 1 na quantidade de divisores, que são as opções escolhidas pelo usuario
  if entr_palav['state'] != tkinter.DISABLED:
    tam_div += 1
  
  tam_final = 0
  tamanhos = []

  #Caso o usuario só queira letras minusculas, ou seja, nenhuma opção
  if tam_div == 1:
    tamanhos.append(tam)
  #Caso ele tenha escolhido alguma opção
  else:
     #Faz esse while até que a somatoria da divisão do tamanho da senha pelas opções escolhidas...
     # Seja igual ao tamanho que a senha tem que ser 
    while tam_final != tam:
      tamanhos = [] #Lista dos tamanhos para cada opção
      for x in range(tam_div): #Range para percorrer todas as opções escolhidas pelo usuario
        #Caso tenha um palavras predefinidas o primeiro valor é a qtd de caracteres dessas palavras
        if entr_palav['state'] != tkinter.DISABLED:
          if x == 0:
            tamanhos.append(len(linha))
          #Senão for o primeiro valor, a qtd de caracteres será igual a:
          #Um valor entre 1 e Tamanho_Total_Senha - Qtd_Caracteres_Palavras_Predefinidas
          else:
            tamanhos.append(random.randint(1,tam-len(linha)))
        #Caso não tenha palavras predefinidas
        else:
          #O valor será entre 1 e Tamanho_Total_Senha - Qtd_Opções_escolhidas
          tamanhos.append(random.randint(1,tam-tam_div+1))
      #Somatoria dessa lista deve ser igual o tamanho escolhido para ser o da senha
      tam_final = sum(tamanhos)
  
  #Adiciona todas as opções escolhidas pelo usuario na senha
  cont = 0 #Posição atual da qtd de caracteres reservados para essa senha
  linha = letra(linha,tamanhos) #Adiciona letras maiusculas e minusculas
  if vars["lma"] is True:#Caso tenha letras maiusculas, soma 1 no contador
    cont += 1
  #Adiciona números
  if vars["n"] is True:
    cont += 1
    linha = n(linha,tamanhos[cont])
  #Adiciona caracteres especiais
  if vars["ce"] is True:
    cont += 1
    linha = ce(linha,tamanhos[cont])
  #Adiciona operadores matematicos
  if vars["om"] is True:
    cont += 1
    linha = om(linha,tamanhos[cont])
  
  #Ativa o botão de copiar e a entry da senha gerada
  entr_final.config(state="normal")
  entr_final.insert(END,linha) #Coloca a senha gerada na entrada
  btt.config(state="normal")


#Criação da tela
tela = Tk()
tela.title("Gerador de Senha")
larg_s = tela.winfo_screenwidth() # largura da tela do usuario
alt_s = tela.winfo_screenheight() # altura da tela do usuario
#calcaula as coordenadas para mostrar a tela da aplicação no meio do monitor
t_x = 650
t_y = 760
a = (larg_s/2) - (t_x/2)
b = (alt_s/2) - (t_y/2)
tela.geometry('%dx%d+%d+%d' % (t_x, t_y, a, b-50))
tela.geometry(f"{t_x}x{t_y}")
tela.resizable(False, False) #Desabilita a redimensão da janela
tela.configure(bg= "#CCCCCC")
tela.protocol("WM_DELETE_WINDOW", quit) #Coloca o X da janela para sair da aplicação toda

#Labels para melhor visualização dos botões
lbl_aux0 = Label(tela, text="    ", bg= "#CCCCCC",font= "Calibri 12")
lbl_aux0.grid(row=0, column=0, columnspan=20)
lbl_aux1 = Label(tela, text="    ", bg= "#CCCCCC",font= "Calibri 12")
lbl_aux1.grid(row=3, column=0)
lbl_aux2 = Label(tela, text="    ", bg= "#CCCCCC",font= "Calibri 12")
lbl_aux2.grid(row=3, column=2)

for x in range(0,24,2): #Aux para pular os radio buttons
  lbl_auxs = Label(tela, text="    ", bg= "#CCCCCC",font= "Calibri 12")
  lbl_auxs.grid(row=2+x, column=0)

lbl_titulo = Label(tela, text="Gerador de senhas",bg= "#CCCCCC" ,fg="#000000", font= "Calibri 17")
lbl_titulo.grid(row=1, column=2)

#Entry da senha gerada
entrada =  Entry(tela, text="",width=33, bg= "#FFFFFF", fg="#000000",font= "Calibri 10", state="disable")
entrada.grid(row=3, column=2)
#Botão para copiar a senha gerada para o Control+C do computador
btt_copiar = Button(tela, text='Copiar', padx=50, pady=15, bg="#FFFFFF", fg="#000000",
command= lambda: copiar(), font= "Calibri 12", state="disable")
btt_copiar.grid(row=5, column= 2)

#Entradas e labels dos valores maximos e minimos do tamanho da senha
lbl_max = Label(tela, text="Tam. Max",bg= "#CCCCCC" ,fg="#000000", font= "Calibri 12")
lbl_max.grid(row=7, column=3)
ent_max = Entry(tela, text="",width=5, bg= "#FFFFFF", fg="#000000",font= "Calibri 12")
ent_max.grid(row=9, column= 3)
ent_max.insert(END,10)

lbl_min = Label(tela, text="Tam. Min",bg= "#CCCCCC" ,fg="#000000", font= "Calibri 12")
lbl_min.grid(row=7, column=1)
ent_min = Entry(tela, text="",width=5, bg= "#FFFFFF", fg="#000000",font= "Calibri 12")
ent_min.grid(row=9, column= 1)
ent_min.insert(END,6)

#Lista de variaveis que estão ligadas aos radiobuttons para ativalos e desativalos
vars_tk = []
for x in range(5):
  vv = IntVar()
  if x < 2: #Os três primeiros começam ja selecionados
    vv.set(x+1)
  else:
    vv.set(0)
  vars_tk.append(vv)

#Radiobuttons que representam as opções de caracteres na senha
rdb_lma = Radiobutton(tela,text="Usar Letras Maiusculas", padx=5, bg="#FFFFFF", fg="#000000", variable=vars_tk[0],
value=1,command= lambda: att_normal(vars_tk[0],"lma"), font= "Calibri 12")
rdb_lma.grid(row=11, column= 2)
rdb_n = Radiobutton(tela,text="Usar Números", padx=5, bg="#FFFFFF", fg="#000000", variable=vars_tk[1],
value=2, command= lambda: att_normal(vars_tk[1],"n"), font= "Calibri 12")
rdb_n.grid(row=13, column= 2)
rdb_ce = Radiobutton(tela,text="Usar Caracteres Especiais\n( @, #, $, %, & )",
padx=5, bg="#FFFFFF", fg="#000000", variable=vars_tk[2], value=3,
command= lambda: att_normal(vars_tk[2],"ce"), font= "Calibri 12")
rdb_ce.grid(row=15, column= 2)
rdb_om = Radiobutton(tela,text="Usar Operadores Matematicos\n( +, -, *, / )",
padx=5, bg="#FFFFFF", fg="#000000", variable=vars_tk[3], value=4,
command= lambda: att_normal(vars_tk[3],"om"), font= "Calibri 12")
rdb_om.grid(row=17, column= 2)
rdb_pd = Radiobutton(tela,text="Usar Palavras Pré-Definidas", 
padx=5, bg="#FFFFFF", fg="#000000", variable=vars_tk[4], value=5,
 command= lambda: att_pd(entrada_p,vars_tk[4]), font= "Calibri 12")
rdb_pd.grid(row=19, column= 2)

#Entrada para palavras que o usuario quer que a senha possua
entrada_p =  Entry(tela, text="",width=33, bg= "#FFFFFF", fg="#000000",font= "Calibri 15", state='disable')
entrada_p.grid(row=21, column=2)

lbl_erro = Label(tela, text="",bg= "#CCCCCC" ,fg="#000000", font= "Calibri 12")
lbl_erro.grid(row=25, column=2)

#Botão para gerar a senha
btt_gerar = Button(tela, text='Gerar', padx=50, pady=15, bg="#FFFFFF", fg="#000000",
command= lambda: gerar(entrada_p,entrada,btt_copiar), font= "Calibri 12")
btt_gerar.grid(row=23, column= 2)

#Ligação de teclas do teclado a funções da aplicação
tela.bind('<Return>',lambda event:gerar(entrada_p,entrada,btt_copiar))
tela.bind('<KP_Enter>',lambda event:gerar(entrada_p,entrada,btt_copiar))
tela.bind('<Control-c>', lambda event:copiar())
tela.bind('<Control-C>', lambda event:copiar())
tela.bind('<Escape>', lambda event:sair())
tela.mainloop()