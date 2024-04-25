from PySimpleGUI import PySimpleGUI as sg
import os

#layout
sg.theme('Reddit')
os.system('cls')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size = (20,1))],
    [sg.Text('Senha'), sg. Input(key='senha', password_char='*', size = (20,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

#janela
janela = sg.Window('Tela de login', layout)

#ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'magno' and valores['senha'] == '1234':
            print('Bem-vindo a Dev aprender!')