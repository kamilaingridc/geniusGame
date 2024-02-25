# importacoes-
import time
from tkinter import * 
import random 

# definindo tamanhos 
largura = 500
altura = 500
lado = 100
initx = largura/2-lado
inity = altura/2-lado

# lógica do jogo 
modelo = [0]
usuario = [0]

def aumentaNivel():
    nTemp = random.randint(1,4)
    modelo.append(nTemp)

# formando o quadrado
def quadrado(initx, inity, lado):
    return [initx, inity, initx+lado, inity, initx+lado, inity+lado, initx, inity+lado]

# funções de cada cor 
def green(event):
    print("Clicou no verde.")
    piscaGreen()
    usuario.append(1)

def red(event):
    print("Clicou no vermelho.")
    piscaRed()
    usuario.append(2)

def blue(event):
    print("Clicou no azul.")
    piscaBlue()
    usuario.append(3)

def yellow(event):
    print("Clicou no amarelo.")
    piscaYellow()
    usuario.append(4)

# impressão de clique
def piscaGreen():
    canvas.itemconfig("green", fill="pale green")
    window.update() # atualiza a cor
    time.sleep(0.2)
    canvas.itemconfig("green", fill="green2")
    window.update()

def piscaRed():
    canvas.itemconfig("red", fill="IndianRed1")
    window.update()
    time.sleep(0.2)
    canvas.itemconfig("red", fill="red2")
    window.update()

def piscaBlue():
    canvas.itemconfig("blue", fill="cornflower blue")
    window.update()
    time.sleep(0.2)
    canvas.itemconfig("blue", fill="blue2")
    window.update()

def piscaYellow():
    canvas.itemconfig("yellow", fill="light goldenrod")
    window.update()
    time.sleep(0.2)
    canvas.itemconfig("yellow", fill="yellow2")
    window.update()


# criando objetos
window = Tk()
canvas = Canvas(window, width=largura, height=altura, bg='white')
canvas.pack()

# criando o quadrado
canvas.create_polygon(quadrado(initx, inity, lado), fill='green2', tags='green')
canvas.create_polygon(quadrado(initx+lado, inity, lado), fill='red2',tags='red')
canvas.create_polygon(quadrado(initx, inity+lado, lado), fill='blue2', tags='blue')
canvas.create_polygon(quadrado(initx+lado, inity+lado, lado), fill='yellow2', tags='yellow')

# função de clique
canvas.tag_bind("green", "<ButtonPress-1>", green)
canvas.tag_bind("red", "<ButtonPress-1>", red)
canvas.tag_bind("blue", "<ButtonPress-1>", blue)
canvas.tag_bind("yellow", "<ButtonPress-1>", yellow)

# loop 
while(True):
    # condições para vencer 
    reason1 = len(usuario) == len(modelo)
    reason2 = usuario[-1] == modelo[len(usuario)-1]

    if( reason1 and reason2):
        aumentaNivel()
        usuario= [0]
        time.sleep(1)
        for i in modelo:
            if i == 1:
                piscaGreen()
            elif i == 2:
                piscaRed()
            elif i == 3:
                piscaBlue()
            elif i == 4:
                piscaYellow()
            
            time.sleep(0.1)
    elif(not reason2):
        print("Jogador perdeu!")
        exit()

    canvas.after(50)
    window.update_idletasks()
    window.update()
