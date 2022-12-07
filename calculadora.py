from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Calculadora")
root.iconbitmap("ico.ico")

frame_tela = Frame(root, bg="black", width=235, height=50)
frame_tela.grid(row=0, column=0)
frame_corpo = Frame(root, bg="black", width=235, height=268)
frame_corpo.grid(row=1, column=0)

#Funcao
def click_igual():
  segundo_numero = tela.get()
  if segundo_numero.isnumeric() or "." in segundo_numero:
    tela.delete(0,END)
    if matematica=="soma":
      tela.insert(0, p_numero + float(segundo_numero))
    if matematica =="subtracao":
      tela.insert(0, p_numero - float(segundo_numero))
    if matematica =="divisao":
      tela.insert(0, p_numero / float(segundo_numero))
    if matematica =="multiplicacao":
      tela.insert(0, p_numero * float(segundo_numero))
    if matematica =="porcentagem":
      tela.insert(0, p_numero % float(segundo_numero))
  else:
    messagebox.showinfo(title="ERRO", message="Desculpe, esta calculadora aceita apenas números. Clique 'C' e digite um numero.")
    
def click_button(numero):
  atual=tela.get()
  tela.delete(0,END)
  tela.insert(END, str(atual)+ str(numero))

     
def click_soma():
  primeiro_numero = tela.get()
  if primeiro_numero.isnumeric() or "." in primeiro_numero: 
    global p_numero
    global matematica
    matematica="soma"
    p_numero = float(primeiro_numero)
    tela.delete(0,END)  
  else:
    messagebox.showinfo(title="ERRO", message="Desculpe, esta calculadora aceita apenas números. Clique 'C' e digite um numero.")

def click_sub():
  primeiro_numero = tela.get()
  if primeiro_numero.isnumeric() or "." in primeiro_numero:
    global p_numero
    global matematica
    matematica="subtracao"
    p_numero = float(primeiro_numero)
    tela.delete(0, END)
  else:
    messagebox.showinfo(title="ERRO", message="Desculpe, esta calculadora aceita apenas números. Clique 'C' e digite um numero.")  

def click_divi():
  primeiro_numero = tela.get()
  if primeiro_numero.isnumeric() or "." in primeiro_numero:
    global p_numero
    global matematica
    matematica="divisao"
    p_numero = float(primeiro_numero)
    tela.delete(0,END)
  else:
    messagebox.showinfo(title="ERRO", message="Desculpe, esta calculadora aceita apenas números. Clique 'C' e digite um numero.")    

def click_mult():
  primeiro_numero = tela.get()
  if primeiro_numero.isnumeric() or "." in primeiro_numero:
    global p_numero
    global matematica
    matematica="multiplicacao"
    p_numero = float(primeiro_numero)
    tela.delete(0,END)
  else:
    messagebox.showinfo(title="ERRO", message="Desculpe, esta calculadora aceita apenas números. Clique 'C' e digite um numero.")    

def click_porcentagem():
  primeiro_numero = tela.get()
  if primeiro_numero.isnumeric() or "." in primeiro_numero:
    global p_numero
    global matematica
    matematica="porcentagem"
    p_numero = float(primeiro_numero)
    tela.delete(0,END) 
  else:
    messagebox.showinfo(title="ERRO", message="Desculpe, esta calculadora aceita apenas números. Clique 'C' e digite um numero.")    
  
def deletar():
  tela.delete(0,END)
  
def click_ponto():
  tela.insert(END,".")

#Entrada
tela = Entry(frame_tela, bd=1, font=("ivy 15 "), justify=RIGHT, bg="black", fg="white")
tela.place(x=0,y=0,width=238,height=48)
#parte 1
bt_apagar = Button(frame_corpo, text="C", font=("ivy 13 bold"), bg="#92cbdc", fg="#906fa8", width=11,height=2, relief=RAISED, overrelief=RIDGE, command=deletar)
bt_apagar.place(x=0, y=0)

bt_resultado = Button(frame_corpo, text="=", font=("ivy 13 bold"), bg="#92cbdc", fg="#906fa8", width=5, height=2, relief=RAISED, overrelief=RIDGE, command=click_igual) 
bt_resultado.place(x=118, y=0)
             
bt_divisao = Button(frame_corpo, text="/", font=("ivy 13 bold"), bg="#906fa8",fg="#7cbfb6", width=5, height=2, relief=RAISED, overrelief=RIDGE, command=click_divi)
bt_divisao.place(x=177, y=0)

#parte 2
bt1 = Button(frame_corpo, text="1", font=("ivy 13 bold"), fg="#906fa8", bg="#ceddf2", width=5, height=2, relief=RAISED, overrelief=RIDGE, command= lambda: click_button(1))
bt1.place(x=0, y=52)

bt2 = Button(frame_corpo, text="2", font=("ivy 13 bold"), fg="#906fa8", bg="#ceddf2", width=5, height=2, relief=RAISED, overrelief=RIDGE, command= lambda: click_button(2))
bt2.place(x=59, y=52)
                   
bt3 = Button(frame_corpo, text="3", font=("ivy 13 bold"), fg="#906fa8", bg="#ceddf2", width=5, height=2, relief=RAISED, overrelief=RIDGE, command= lambda: click_button(3))
bt3.place(x=118, y=52)

btmult = Button(frame_corpo, text="*", font=("ivy 13 bold"), bg="#906fa8",fg="#7cbfb6", width=5, height=2, relief=RAISED, overrelief=RIDGE, command=click_mult)
btmult.place(x=177, y=52)

#parte 3
bt4 = Button(frame_corpo, text="4", font=("ivy 13 bold"), fg="#906fa8", bg="#ceddf2", width=5, height=2, relief=RAISED, overrelief=RIDGE, command= lambda: click_button(4))
bt4.place(x=0, y=104)

bt5 = Button(frame_corpo, text="5", font=("ivy 13 bold"), fg="#906fa8", bg="#ceddf2", width=5, height=2, relief=RAISED, overrelief=RIDGE, command= lambda: click_button(5))
bt5.place(x=59, y=104)
                   
bt6 = Button(frame_corpo, text="6", font=("ivy 13 bold"), fg="#906fa8", bg="#ceddf2", width=5, height=2, relief=RAISED, overrelief=RIDGE, command= lambda: click_button(6))
bt6.place(x=118, y=104)

btsub = Button(frame_corpo, text="-", font=("ivy 13 bold"), bg="#906fa8",fg="#7cbfb6", width=5, height=2, relief=RAISED, overrelief=RIDGE, command=click_sub)
btsub.place(x=177, y=104)

#parte 4
bt7 = Button(frame_corpo, text="7", font=("ivy 13 bold"), fg="#906fa8", bg="#ceddf2", width=5, height=2, relief=RAISED, overrelief=RIDGE, command= lambda: click_button(7))
bt7.place(x=0, y=156)

bt8 = Button(frame_corpo, text="8", font=("ivy 13 bold"), fg="#906fa8", bg="#ceddf2", width=5, height=2, relief=RAISED, overrelief=RIDGE, command= lambda: click_button(8))
bt8.place(x=59, y=156)
                   
bt9 = Button(frame_corpo, text="9", font=("ivy 13 bold"), fg="#906fa8", bg="#ceddf2", width=5, height=2, relief=RAISED, overrelief=RIDGE, command= lambda: click_button(9))
bt9.place(x=118, y=156)

btsoma = Button(frame_corpo, text="+", font=("ivy 13 bold"), bg="#906fa8",fg="#7cbfb6", width=5, height=2, relief=RAISED, overrelief=RIDGE, command=click_soma) 
btsoma.place(x=177, y=156)

#parte 5
bt0 = Button(frame_corpo, text="0", font=("ivy 13 bold"), fg="#906fa8", bg="#ceddf2", width=11,height=2, relief=RAISED, overrelief=RIDGE, command= lambda: click_button(0))
bt0.place(x=0, y=208)

bt_ponto = Button(frame_corpo, text=".", font=("ivy 13 bold"), fg="#906fa8", bg="#ceddf2", width=5, height=2, relief=RAISED, overrelief=RIDGE, command=click_ponto)
bt_ponto.place(x=118, y=208)
                   
bt_porcentagem = Button(frame_corpo, text="%", font=("ivy 13 bold"), bg="#906fa8",fg="#7cbfb6", width=5, height=2, relief=RAISED, overrelief=RIDGE, command= click_porcentagem)
bt_porcentagem.place(x=177, y=208)



root.geometry("235x309")

root.mainloop()