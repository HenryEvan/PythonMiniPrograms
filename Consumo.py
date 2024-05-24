import PySimpleGUI as sg

def janela_painel():
    sg.theme('Black')
    layout = [
        [sg.Text('Potência (w)'), sg.Text('             '), sg.Text('Consumo (h/dia)')],
        [sg.Input(key='potencia', size=(10,1)), sg.Text('               '), sg.Input(key='consumo', size=(10,1)), sg.Text(' ')],
        [sg.Text('Consumo (dia/mês)'), sg.Text('   '), sg.Text('Valor da Tarifa (R$/kW)')],
        [sg.Input(key='dias', size=(10,1)), sg.Text('               '), sg.Input(key='tarifa', size=(10,1)), sg.Text(' ')],
        [sg.Text('')],
        [sg.Text('Resultado (R$)')],
        [sg.Output(key='output', size=(15,1)), sg.Text('     '), sg.Button('Calcular', key='calcular', size=(10,1))],
    ]
    return sg.Window('Consumo', layout=layout, finalize=True)

# Exemplos: (660w) x (8horas) x (30 dias) x (R$/kW 0.65) = R$ 102.96

# Menu:

janela1 = janela_painel()

while True:

    window, event, values = sg.read_all_windows()

    if window == janela1 and event == sg.WIN_CLOSED:
        break

    if window == janela1 and event == 'calcular':

        resultado_1 = (float((values['potencia'])) * float((values['consumo'])) * float((values['dias'])))
        resultado = (resultado_1 * float((values['tarifa']))) / 1000
        
        print (' '*39)
        print ('R$ {}'.format(resultado))
        