import PySimpleGUI as sg
from CompoundMath import CompInterest


#sg.theme('grey1')   # Add a touch of color
amount = 0
#layout of the window
layout = [  [sg.Text('Enter the principle: '), sg.InputText(size=(19, 1))],
            [sg.Text('Enter the interest: '), sg.InputText(size=(20, 1))],
            [sg.Text('Enter the time period: '), sg.InputText(size=(17, 1))],
            [sg.Button('Compound')],
            [sg.Button('Cancel')],
            #[sg.Text(amount)]
         ]

# Create the Window
window = sg.Window("Dominik's App", layout = layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    elif event == 'Compound':
        amount = CompInterest(values[0],values[2],values[1])



    #if event budget, open budget window close current window
    #if event interest, open interest window close current window
    #print('You entered ', values[0])

window.close()