import PySimpleGUI as sg
import socket

def check_ports(ip):
    for port in [8080, 9090, 80, 90, 443]:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Porta {port} está funcionando!!")
            else:
                print(f"Porta {port} não está funcionando")
        except Exception as e:
            print(f"Erro: {str(e)}")

def button_click(event):
    if event == "BUTTON":
        ip = sg.popup_get_text("IP:", default_text="Coloque seu IP aqui")
        check_ports(ip)

layout = [[sg.Text("=====================================")],
          [sg.Button("Começar!", key="BUTTON")]]

window = sg.Window("Teste de Porta", layout)
while True:
    event, values = window.read()
    print('\n'*59)
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    button_click(event)

window.close()