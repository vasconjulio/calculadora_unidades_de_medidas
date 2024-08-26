# importando tkinter
from tkinter import *
from tkinter import ttk

# criação janela e configurações basicas
janela =Tk()
janela.title("Calculadora Unidades de Medidas")
janela.geometry('650x260')
janela.configure(bg='black')

# cores
cor1 = '#3b3b3b' #preto
cor2 = '#ffffff' #branco
cor3 = '#48b3e0' #azul

# ------------- Frames para janela -------------
frame_cima = Frame(janela, width=450, height=50, bg=cor2, pady=0, padx=3, relief=FLAT)
frame_cima.place(x=2, y=2)

frame_esquerda = Frame(janela, width=450, height=220, bg=cor2, pady=0, padx=3, relief=FLAT)
frame_esquerda.place(x=2, y=54)

frame_direita= Frame(janela, width=198, height=260, bg=cor2, pady=0, padx=3, relief=FLAT)
frame_direita.place(x=454, y=2)

# ------------- Estilo para janela -------------
estilo = ttk.Style(janela)
estilo.theme_use("clam")

# ------------- Labels para Frame Cima -------------
l_app_nome = Label(frame_cima, text='Calculadora de Unidades de Medidas', height=1, padx=0, relief=FLAT, anchor='center', font=('Ivy 15 bold'), bg=cor2, fg=cor3)
l_app_nome.place(x=50, y=10)

janela.mainloop()