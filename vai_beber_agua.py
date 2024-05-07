#! /usr/bin/env python3
"""
Xx VAI BEBER ÁGUA!! xX

Lembrete pra ir beber água a cada 3hrs mais ou menos :D
"""
import tkinter
import random
import time
import os


def mostrar_imagem(path_imagem:str):
    """
    Cria uma janela tkinter fullscreen para mostrar a imagens preenchida na tela
    Só clicar na tela que a janela é destruída
    """
    root = tkinter.Tk()
    img = tkinter.PhotoImage(master=root, file=path_imagem)
    label = tkinter.Label(master=root, image=img)
    label.place(
        x=0,
        y=0,
        width=root.winfo_screenwidth(),
        height=root.winfo_screenheight()
    )
    root.bind('<Button-1>', lambda event=None: root.destroy())
    root.attributes('-fullscreen', 1)
    root.mainloop()


def msg_aguardando(motivo='\b', tempo=10):
    quantidade_pontos = 0
    for i in range(tempo, -1, -1):
        prompt = f'\rAguardando {motivo} {i}seg' + '.' * quantidade_pontos
        borracha = ' ' * len(prompt)  + '\b' * len(prompt)

        quantidade_pontos += 1
        if quantidade_pontos == 4:
            quantidade_pontos = 0
        
        print(prompt, end='\r', flush=True)
        time.sleep(1)
        print(borracha, end='\r', flush=True)
    print('')


PATH_IMAGENS = os.path.join('bisaco', 'imagens', '')
ALBUM = [img for img in os.listdir(PATH_IMAGENS) if img.endswith('.png')]

TEMPO_ESPERA = 10800

while True:
    random.shuffle(ALBUM)

    for indice, imagem in enumerate(ALBUM, start=1):
        msg_aguardando(motivo='um pokin', tempo=TEMPO_ESPERA)
        print(f'[{indice}] VAI BEBER ÁGUA!!! :D')
        mostrar_imagem(path_imagem=PATH_IMAGENS + imagem)
        print('-' * 30)
