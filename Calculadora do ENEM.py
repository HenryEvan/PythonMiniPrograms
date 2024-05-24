import PySimpleGUI as GUI

# Janelas

def janela_calculo():
    GUI.theme('Black')
    layout = [
        [GUI.Text('Nota'), GUI.Text('                    '), GUI.Text('Peso')],
        [GUI.Input(key='nota1', size=(10,1)), GUI.Text('         '), GUI.Input(key='peso1', size=(5,1)), GUI.Text(' '), GUI.Text('Ciências Humanas e suas tecnologias')],
        [GUI.Input(key='nota2', size=(10,1)), GUI.Text('         '), GUI.Input(key='peso2', size=(5,1)), GUI.Text(' '), GUI.Text('Ciências da Natureza e suas tecnologias')],
        [GUI.Input(key='nota3', size=(10,1)), GUI.Text('         '), GUI.Input(key='peso3', size=(5,1)), GUI.Text(' '), GUI.Text('Linguagens, Códigos e suas tecnologias')],
        [GUI.Input(key='nota4', size=(10,1)), GUI.Text('         '), GUI.Input(key='peso4', size=(5,1)), GUI.Text(' '), GUI.Text('Matemática e suas tecnologias')],
        [GUI.Input(key='nota5', size=(10,1)), GUI.Text('         '), GUI.Input(key='peso5', size=(5,1)), GUI.Text(' '), GUI.Text('Redação')],
        [GUI.Text('')],
        [GUI.Text(25*' '), GUI.Button('Calcular', key='calcular', size=(20,1))],
    ]
    return GUI.Window('Calculadora de Média do ENEM', layout=layout, size=(500,250), finalize=True)

# Entradas

janela_1, janela_2 = janela_calculo(), None
GUI.popup("Bem vindo à calculadora de média do ENEM, não se acanhe e coloque sua nota.")
GUI.popup("Caso não defina algum peso, por padrão todos serão 1.")

while True:
    window, event, value = GUI.read_all_windows()
    if (window == janela_1) and (event == GUI.WIN_CLOSED):
        break
    if (event == 'calcular'):
        invalid = 0
        no_peso = 0

        if (value['peso1'] == '') or (value['peso2'] == '') or (value['peso3'] == '') or (value['peso4'] == '') or (value['peso5'] == ''):
            (value['peso1']), (value['peso2']), (value['peso3']), (value['peso4']), (value['peso5']) = 1,1,1,1,1
            no_peso = 1
        
        if (value['nota1'] == '') or (value['nota2'] == '') or (value['nota3'] == '') or (value['nota4'] == '') or (value['nota5'] == ''):
            invalid = 1
            GUI.popup('Você esqueceu de colocar alguma nota, confira novamente.')

        elif (float(value['peso1']) > 1500)  or (float(value['peso2']) > 1500) or (float(value['peso3']) > 1500) or (float(value['peso4']) > 1500) or (float(value['peso5']) > 1500):
            invalid = 1
            GUI.popup('Você colocou o peso além do permitido, confira novamente.')

        elif (float(value['nota1']) > 1500)  or (float(value['nota2']) > 1500) or (float(value['nota3']) > 1500) or (float(value['nota4']) > 1500) or (float(value['nota5']) > 1500):
            invalid = 1
            GUI.popup('Você colocou a nota além do permitido, confira novamente.')
        
        if invalid != 1:
            soma_pesos = float(value['peso1']) + float(value['peso2']) + float(value['peso3']) + float(value['peso4']) + float(value['peso5'])
            resultado_1 = (float(value['nota1']) * float(value['peso1'])) + (float(value['nota2']) * float(value['peso2'])) + (float(value['nota3']) * float(value['peso3'])) + (float(value['nota4']) * float(value['peso4'])) + (float(value['nota5']) * float(value['peso5']))
            resultado_2 = (resultado_1/soma_pesos)

            if no_peso == 0:
                GUI.popup(' Pesos: Sim \n Média: {}'.format(resultado_2))
            if no_peso == 1:
                GUI.popup(' Pesos: Não (1) \n Média: {}'.format(resultado_2))
