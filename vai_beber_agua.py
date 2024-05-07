#! /usr/bin/env python3
"""
Xx VAI BEBER ÁGUA!! xX

Lembrete pra ir beber água a cada 3hrs mais ou menos :D
"""
import random
import time
import os


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
ALBUM = [img for img in os.listdir(PATH_IMAGENS) if img.endswith('.jpg')]

TEMPO_ESPERA = 10800

while True:
    random.shuffle(ALBUM)
    for indice, img in enumerate(ALBUM, start=1):
        msg_aguardando(motivo='um tempin', tempo=TEMPO_ESPERA)
        print(f'[{indice}] VAI BEBER ÁGUA!!! :D')
        os.system(f'start /max {PATH_IMAGENS}"{img}"')
        kuteis.divisor_animado(colunas=30)
