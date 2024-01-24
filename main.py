import flet as ft
from flet import colors
import random
import time
import pygame
pygame.init()

def main(page = ft.Page):
    page.bgcolor = '#DCDCDC'
    page.title = 'Genius'
    page.window_width = 1015
    page.window_height = 738
    page.window_resizable = False
    page.window_minimizable = True
    page.window_maximizable = False
    page.window_center()
    page.padding = 0
    
    som_amarelo = pygame.mixer.Sound("som_amarelo.mp3")
    som_vermelho = pygame.mixer.Sound("som_vermelho.mp3")
    som_verde = pygame.mixer.Sound("som_verde.mp3")
    som_azul = pygame.mixer.Sound("som_azul.mp3")
    som_perdeu = pygame.mixer.Sound("som_perdeu.mp3")

    cores = ['amarelo', 'vermelho', 'verde', 'azul']

    verde_aceso = ft.Image(src = 'Verde_Aceso.png',
            width = 1000, height = 700, opacity = 0)
    vermelho_aceso = ft.Image(src = 'Vermelho_Aceso.png',
            width = 1000, height = 700, opacity = 0)
    azul_aceso = ft.Image(src = 'Azul_Aceso.png',
            width = 1000, height = 700, opacity = 0)
    amarelo_aceso = ft.Image(src = 'Amarelo_Aceso.png',
            width = 1000, height = 700, opacity = 0)

    sequencia_cores = []
    sequencia_atual = [0]
    maior_sequencia = [0]
    botao_clicado_index = [0]

    def mudar_voltar_botao(e):
        if e.data == 'true':
            voltar_botao.content.content.scale = 1.4
            voltar_botao.content.width += 4
            voltar_botao.content.height += 4
            voltar_botao.padding = 8
        else:
            voltar_botao.content.content.scale = 1.3
            voltar_botao.content.width = 100
            voltar_botao.content.height = 30
            voltar_botao.padding = 10
        page.update()

    def tirar_botoes():
        botao_amarelo.controls[0].on_click = None
        botao_vermelho.controls[0].on_click = None
        botao_verde.controls[0].on_click = None
        botao_azul.controls[0].on_click = None
    
    def botar_botoes():
        botao_amarelo.controls[0].on_click = botao_clicado
        botao_vermelho.controls[0].on_click = botao_clicado
        botao_verde.controls[0].on_click = botao_clicado
        botao_azul.controls[0].on_click = botao_clicado

    def voltar_para_inicio():
        time.sleep(0.2)
        page.remove(jogo)
        tirar_botoes()
        sequencia_cores.clear()
        sequencia_atual.clear()
        sequencia_atual.append(0)
        sequencia_atual_texto.content.value = f'Sequência atual: {max(sequencia_atual)}'
        record = max(maior_sequencia)
        maior_sequencia.clear()
        maior_sequencia.append(record)
        botao_clicado_index[0] = 0
        page.add(inicio)
        page.update()

    def voltar(e):
        voltar_para_inicio()
        voltar_botao.content.content.scale = 1.3
        voltar_botao.content.width = 100
        voltar_botao.content.height = 30
        voltar_botao.padding = 10
        page.update()

    voltar_botao = ft.Container(content = ft.Container(
        content = ft.Text("Voltar", color = colors.WHITE, weight=ft.FontWeight.W_700, scale = 1.3),
        bgcolor = colors.BLACK,
        width = 100,
        height = 30,
        border_radius = 100,
        on_click = voltar,
        on_hover = mudar_voltar_botao,
        alignment = ft.alignment.center
        ),
        width = 1000,
        height = 700,
        padding = 10,
        alignment = ft.alignment.bottom_right)

    def botao_clicado(e):
        if e.control.content.value != sequencia_cores[botao_clicado_index[0]]:
            som_perdeu.play()
            voltar_para_inicio()
        else:
            if e.control.content.value == 'amarelo':
                amarelo_aceso.opacity = 1
                page.update()
                som_amarelo.play()
                tirar_botoes()
                page.update()
                time.sleep(0.2)
                botar_botoes()
                amarelo_aceso.opacity = 0
                page.update()
            if e.control.content.value == 'vermelho':
                vermelho_aceso.opacity = 1
                page.update()
                som_vermelho.play()
                tirar_botoes()
                page.update()
                time.sleep(0.2)
                botar_botoes()
                vermelho_aceso.opacity = 0
                page.update()
            if e.control.content.value == 'verde':
                verde_aceso.opacity = 1
                page.update()
                som_verde.play()
                tirar_botoes()
                page.update()
                time.sleep(0.2)
                botar_botoes()
                verde_aceso.opacity = 0
                page.update()
            if e.control.content.value == 'azul':
                azul_aceso.opacity = 1
                page.update()
                som_azul.play()
                tirar_botoes()
                page.update()
                time.sleep(0.2)
                botar_botoes()
                azul_aceso.opacity = 0
                page.update()
            if e.control.content.value == sequencia_cores[botao_clicado_index[0]]:
                sequencia_atual[len(sequencia_cores)-1] += 1
                sequencia_atual_texto.content.value = f'Sequência atual: {max(sequencia_atual)}'
                botao_clicado_index[0] += 1
                page.update()
            if botao_clicado_index[0] == len(sequencia_cores):
                sequencia_atual.append(0)
                tirar_botoes()
                page.update()
                if max(sequencia_atual) >= max(maior_sequencia):
                    maior_sequencia.clear()
                    maior_sequencia.append(max(sequencia_atual))
                maior_sequencia_texto.content.value = f'Maior sequência: {max(maior_sequencia)}'
                page.update()
                funcionamento_do_jogo()

    botao_verde = ft.Stack([ft.Container(content = ft.Text('verde', width = 193, height = 193, opacity = 0), on_click = None)], width = 193, height = 193, left=285, top=134)
    botao_vermelho = ft.Stack([ft.Container(content = ft.Text('vermelho', width = 193, height = 193, opacity = 0), on_click = None)], width = 193, height = 193, right=285, top=134)
    botao_amarelo = ft.Stack([ft.Container(content = ft.Text('amarelo', width = 193, height = 193, opacity = 0), on_click = None)], width = 193, height = 193, left=285, bottom=138)
    botao_azul = ft.Stack([ft.Container(content = ft.Text('azul', width = 193, height = 193, opacity = 0), on_click = None)], width = 193, height = 193, right=285, bottom=138)

    def selecionar_cor():
        sequencia_cores.append(random.choice(cores))
        for cor in sequencia_cores:
            if cor == 'amarelo':
                amarelo_aceso.opacity = 1
                page.update()
                som_amarelo.play()
                time.sleep(0.4)
                amarelo_aceso.opacity = 0
                page.update()
            if cor == 'vermelho':
                vermelho_aceso.opacity = 1
                page.update()
                som_vermelho.play()
                time.sleep(0.4)
                vermelho_aceso.opacity = 0
                page.update()
            if cor == 'verde':
                verde_aceso.opacity = 1
                page.update()
                som_verde.play()
                time.sleep(0.4)
                verde_aceso.opacity = 0
                page.update()
            if cor == 'azul':
                azul_aceso.opacity = 1
                page.update()
                som_azul.play()
                time.sleep(0.4)
                azul_aceso.opacity = 0
                page.update()
            time.sleep(0.28)
            page.update()

    def funcionamento_do_jogo():
        time.sleep(0.6)
        selecionar_cor()
        botao_clicado_index[0] = 0
        botar_botoes()
        page.update()

    def iniciar_jogo(e):
        page.remove(inicio)
        page.add(jogo)
        time.sleep(1)
        funcionamento_do_jogo()

    def mudar_inicio_butao(e):
        if e.data == 'true':
            inicio_botao.content.content.scale = 7
            inicio_botao.content.width += 10
            inicio_botao.content.height += 10
        else:
            inicio_botao.content.content.scale = 6.5
            inicio_botao.content.width = 600
            inicio_botao.content.height = 200
        page.update()

    inicio_imagem = ft.Image(src = 'Genius_Inicio.png',
            width = 1000, height = 700)
    inicio_botao = ft.Container(content = ft.Container(
        content = ft.Text("Iniciar", color = colors.BLACK, weight=ft.FontWeight.W_700, scale = 6.5),
        width = 600,
        height = 200,
        bgcolor = colors.WHITE,
        border_radius = 100,
        on_click = iniciar_jogo,
        on_hover = mudar_inicio_butao,
        alignment = ft.alignment.center
        ),
            width = 1000,
            height = 700,
            alignment = ft.alignment.center
        )
    genius_imagem = ft.Image(src = 'Genius_Jogo.png',
            width = 1000, height = 700)
    sequencia_atual_texto = ft.Container(ft.Text(f"Sequência atual: {max(sequencia_atual)}", color = colors.BLACK, weight=ft.FontWeight.W_800, scale = 3), alignment = ft.alignment.center, padding = 25)
    maior_sequencia_texto = ft.Container(ft.Text(f"Maior sequência: {max(maior_sequencia)}", color = colors.BLACK, weight=ft.FontWeight.W_800, scale = 3), alignment = ft.alignment.center, bottom=30, left = 431)
    inicio = ft.Stack([inicio_imagem, inicio_botao])
    jogo = ft.Stack([genius_imagem, verde_aceso, vermelho_aceso, azul_aceso, amarelo_aceso, voltar_botao, sequencia_atual_texto, maior_sequencia_texto, botao_amarelo, botao_verde, botao_vermelho, botao_azul])

    page.add(inicio)

ft.app(main)
